#!/usr/bin/env python3
"""Compile a modular report configuration into one JSON file."""

from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path
from typing import Any


class ConfigError(ValueError):
    """Raised when a configuration source cannot be compiled."""


def load_json(path: Path) -> Any:
    try:
        with path.open(encoding="utf-8") as source:
            return json.load(source)
    except FileNotFoundError as exc:
        raise ConfigError(f"Included file does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ConfigError(
            f"Invalid JSON in {path}: {exc.msg} (line {exc.lineno})"
        ) from exc


def resolve(value: Any, source: Path, active: set[Path]) -> Any:
    """Resolve $include directives, using the declaring file as the base path."""
    if isinstance(value, dict):
        if set(value) == {"$include"}:
            includes = value["$include"]
            if not isinstance(includes, list) or not all(
                isinstance(item, str) for item in includes
            ):
                raise ConfigError(
                    f"$include in {source} must be an array of file paths"
                )

            resolved: list[Any] = []
            for include in includes:
                include_path = (source.parent / include).resolve()
                if include_path in active:
                    chain = " -> ".join(str(item) for item in (*active, include_path))
                    raise ConfigError(f"Circular $include detected: {chain}")
                resolved.append(resolve_file(include_path, active | {include_path}))

            if all(isinstance(item, list) for item in resolved):
                return [entry for item in resolved for entry in item]
            if len(resolved) == 1:
                return resolved[0]
            raise ConfigError(f"$include in {source} has multiple non-array files")

        return {key: resolve(item, source, active) for key, item in value.items()}

    if isinstance(value, list):
        result: list[Any] = []
        for item in value:
            item = resolve(item, source, active)
            # Includes inside arrays are spliced, which also supports nested fragments.
            result.extend(item if isinstance(item, list) else [item])
        return result

    return value


def resolve_file(path: Path, active: set[Path]) -> Any:
    return resolve(load_json(path), path, active)


def deduplicate_charts(charts: list[Any]) -> list[dict[str, Any]]:
    compiled: list[dict[str, Any]] = []
    positions: dict[str, int] = {}
    for index, chart in enumerate(charts, start=1):
        if not isinstance(chart, dict) or not isinstance(chart.get("chartId"), str):
            raise ConfigError(
                f"charts entry #{index} must be an object with a string chartId"
            )
        chart_id = chart["chartId"]
        if chart_id in positions:
            logging.warning(
                "Duplicate chartId %r: replacing the earlier definition", chart_id
            )
            compiled[positions[chart_id]] = chart
        else:
            positions[chart_id] = len(compiled)
            compiled.append(chart)
    return compiled


def compile_report(master_path: Path) -> dict[str, Any]:
    master_path = master_path.resolve()
    report = resolve_file(master_path, {master_path})
    if not isinstance(report, dict):
        raise ConfigError("Master report must be a JSON object")
    if not isinstance(report.get("charts"), list):
        raise ConfigError("Master report must resolve charts to a JSON array")
    report["charts"] = deduplicate_charts(report["charts"])
    return report


def validate_config(report: dict[str, Any]) -> None:
    """Validate the generated artifact before it reaches the application."""
    for field in ("application", "version"):
        if not isinstance(report.get(field), str) or not report[field].strip():
            raise ConfigError(
                f"Final report field {field!r} must be a non-empty string"
            )

    charts = report.get("charts")
    if not isinstance(charts, list):
        raise ConfigError("Final report field 'charts' must be an array")

    required_adapter_fields = ("modulePath", "className", "method")
    for index, chart in enumerate(charts, start=1):
        if (
            not isinstance(chart, dict)
            or not isinstance(chart.get("chartId"), str)
            or not chart["chartId"].strip()
        ):
            raise ConfigError(
                f"Final report charts entry #{index} requires a non-empty chartId"
            )
        adapter = chart.get("dataAdapter")
        if not isinstance(adapter, dict):
            raise ConfigError(
                f"Final report chart {chart['chartId']!r} requires a dataAdapter object"
            )
        for field in required_adapter_fields:
            if not isinstance(adapter.get(field), str) or not adapter[field].strip():
                raise ConfigError(
                    f"Final report chart {chart['chartId']!r} dataAdapter.{field} must be a non-empty string"
                )
        if not isinstance(adapter.get("parameters"), dict):
            raise ConfigError(
                f"Final report chart {chart['chartId']!r} dataAdapter.parameters must be an object"
            )

    # JSON encoding and decoding catches unsupported Python values before output is created.
    try:
        json.loads(json.dumps(report, allow_nan=False))
    except (TypeError, ValueError, json.JSONDecodeError) as exc:
        raise ConfigError(
            f"Final report cannot be represented as strict JSON: {exc}"
        ) from exc


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a merged reports.json from modular JSON files."
    )
    parser.add_argument(
        "master", nargs="?", type=Path, default=Path("config/masterreport.json")
    )
    parser.add_argument(
        "output", nargs="?", type=Path, default=Path("config/reports.json")
    )
    args = parser.parse_args()

    try:
        report = compile_report(args.master)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        logging.info("Built %s", args.output)
        return 0
    except ConfigError as exc:
        logging.error("Build failed: %s", exc)
        return 1


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    sys.exit(main())
