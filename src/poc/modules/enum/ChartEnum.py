from enum import StrEnum


class ChartType(StrEnum):
    DISTRIBUTION = "Distribution Engine"
    RELATIONAL = "Relational Engine"
    CATEGORIOCAL = "Categorical Engine"
    THREED = "3D Engine"
    MATRIX = "Matrix And Relationship Engine"
    PART2WHOLE = "Part-To-Whole Engine"
    GEO = "Geo Spatial Engine"


class DisplayMode(StrEnum):
    BOTH = "Side-by-Side"
    INTERCTIVE = "Interactive Only"
    STATIC = "Static Only"
