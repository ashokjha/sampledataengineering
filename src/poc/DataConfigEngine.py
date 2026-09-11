import os
from dotenv import load_dotenv
import json
import importlib
from typing import Any, List


class DataConfigEngine:
    _instance = None  # Stores the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Create the instance if it doesn't exist yet
            cls._instance = super().__new__(cls)
            load_dotenv()
            cls.__DATA_ENV_FILE = os.getenv("DATA_FETCHER_CONFIG", "sample.json")
            with open(cls.__DATA_ENV_FILE, "r") as f:
                cls.__config = json.load(f)
        return cls._instance

    def _dynamic_import(self, module_path: str, class_name: str) -> Any:
        try:
            module = importlib.import_module(module_path)
            return getattr(module, class_name)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(
                f"Module '{module_path}' or class '{class_name}' not found। error: {e}"
            )

    def fetchData(self, chart_id: str, runtime_params: dict[str, Any] = None):
        # Find the requested chart block
        chart_meta = next(
            (c for c in self.__config["charts"] if c["chartId"] == chart_id), None
        )
        if not chart_meta:
            raise ValueError(f"Chart ID '{chart_id}' not found in configuration.")

        fetcher_info = chart_meta["dataFetcher"]
        fetcher_class = self._dynamic_import(
            fetcher_info["modulePath"], fetcher_info["className"]
        )
        fetcher_method = getattr(fetcher_class, fetcher_info["method"])
        query_params = fetcher_info.get("parameters", {})

        final_query_params = {**query_params}
        if runtime_params:
            final_query_params.update(runtime_params)

        # Data Mapping TODO
        return fetcher_method(**final_query_params)


if __name__ == "__main__":
    dc = DataConfigEngine()
    print(dc.fetchData("distribution"))
    print(dc.fetchData("distributionNoExist"))
