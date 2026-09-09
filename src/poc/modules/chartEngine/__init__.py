from poc.modules.enum.ChartEnum import ChartType
from .BaseChartEngine import BaseChartEngine
from .CategoricalEngine import CategoricalEngine
from .MatrixEngine import MatrixEngine
from .PartToWholeEngine import PartToWholeEngine
from .GeospatialEngine import GeospatialEngine
from .ThreeDChartsEngine import ThreeDChartEngine
from .RelationalEngine import RelationEngine
from .DistributionEngine import DistributionEngine
from .FinancialEngine import FinancialEngine


# Get Chart Engine
def get_chart_engine(chart_type: ChartType) -> BaseChartEngine:
    engines_map = {
        ChartType.DISTRIBUTION: DistributionEngine,
        ChartType.RELATIONAL: RelationEngine,
        ChartType.CATEGORIOCAL: CategoricalEngine,
        ChartType.THREED: ThreeDChartEngine,
        ChartType.MATRIX: MatrixEngine,
        ChartType.PART2WHOLE: PartToWholeEngine,
        ChartType.GEO: GeospatialEngine,
        ChartType.FINANCIAL: FinancialEngine,
    }

    if chart_type not in engines_map:
        raise ValueError(
            f"❌ Unknown Chart Engine type: '{chart_type}'. Available options: {list(engines_map.keys())}"
        )

    return engines_map[chart_type]()


__all__ = [
    "BaseChartEngine",
    "CategoricalEngine",
    "MatrixEngine",
    "PartToWholeEngine",
    "GeospatialEngine",
    "ThreeDChartEngine",
    "RelationEngine",
    "DistributionEngine",
    "get_chart_engine",
]
