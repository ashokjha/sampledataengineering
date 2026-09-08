from typing import Dict, Type

from poc.modules.enum.ChartEnum import ChartType
from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc.modules.chartEngine.DistributionEngine import DistributionEngine
from poc.modules.chartEngine.RelationalEngine import RelationEngine
from poc.modules.chartEngine.CategoricalEngine import CategoricalEngine
from poc.modules.chartEngine.ThreeDChartsEngine import ThreeDChartEngine
from poc.modules.chartEngine.MatrixEngine import MatrixEngine
from poc.modules.chartEngine.PartToWholeEngine import PartToWholeEngine
from poc.modules.chartEngine.GeospatialEngine import GeospatialEngine

# 1. राउटर डिक्शनरी: चार्ट टाइप को सीधे उसकी इंजन क्लास से मैप करें
ENGINE_ROUTER: Dict[ChartType, Type] = {
    ChartType.DISTRIBUTION: DistributionEngine,
    ChartType.RELATIONAL: RelationEngine,
    ChartType.CATEGORIOCAL: CategoricalEngine,
    ChartType.THREED: ThreeDChartEngine,
    ChartType.MATRIX: MatrixEngine,
    ChartType.PART2WHOLE: PartToWholeEngine,
    ChartType.GEO: GeospatialEngine,
}


def get_engine_router(chart_type: ChartType) -> BaseChartEngine:
    """Chart Engine Based on Chart Type
    Args:
        chart_type (ChartType): _description_

    Raises:
        ValueError: _description_

    Returns:
        BaseChartEngine: _description_
    """
    engine_class = ENGINE_ROUTER.get(chart_type)

    if not engine_class:
        raise ValueError(f"No routing engine found for: {chart_type}")

    return engine_class()  # यहाँ इंजन क्लास का ऑब्जेक्ट (Instance) बनता है
