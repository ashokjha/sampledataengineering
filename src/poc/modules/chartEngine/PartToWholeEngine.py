import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd

from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc import DataConfigEngine


class PartToWholeEngine(BaseChartEngine):
    """<b>Part-to-Whole & Hierarchical Charts</b>
    Best libraries: <b>Plotly</b>, <b>Matplotlib</b>, or <b>Squarify</b>
    <ul><b>Pie Chart:</b> Shows proportions of a static total (best for ≤ 5 categories).</ul>
    <ul><b>Donut Chart:</b> A pie chart with a hollow center, often cleaner to read.</ul>
    <ul><b>Treemap:</b> Displays hierarchical data using nested rectangles (requires squarify or plotly).</ul>
    <ul><b>Sunburst Chart:</b> Displays hierarchical data spread outwards across concentric rings.</ul>
    """

    def __init__(self):
        super().__init__()
        self.charts = []
        self.dce = DataConfigEngine()
        self.df = self.dce.fetchData("Part2Whole")

    def render_all(self) -> list[dict]:
        self.doNutChart()
        self.treeMap()
        return self.charts

    def doNutChart(self) -> None:
        # 1. Donut Chart
        fig_s1, ax = plt.subplots(figsize=(6, 4))
        ax.pie(
            self.df["Values"],
            labels=self.df["Labels"],
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops=dict(width=0.4, edgecolor="w"),
            colors=sns.color_palette("Pastel1"),
        )
        ax.set_title("Static Donut Chart")

        fig_i1 = px.pie(
            self.df,
            names="Labels",
            values="Values",
            hole=0.4,
            title="Interactive Donut Chart",
        )
        self.charts.append(
            {
                "title": "Donut Proportions",
                "static": fig_s1,
                "interactive": fig_i1,
                "name": "Donut Chart",
            }
        )

    def treeMap(self) -> None:
        # 2. Treemap
        fig_s2, ax = plt.subplots(figsize=(6, 4))
        # Since squarify requires external installation, we can build a clean horizontal stacked block layout for static
        cumulative = 0
        for i, row in self.df.iterrows():
            ax.barh("Total Share", row["Values"], left=cumulative, label=row["Labels"])
            cumulative += row["Values"]
        ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=5)
        ax.set_title("Static Proportional Share Chart")

        fig_i2 = px.treemap(
            self.df, path=["Labels"], values="Values", title="Interactive Treemap"
        )
        self.charts.append(
            {
                "title": "Treemap Hierarchy",
                "static": fig_s2,
                "interactive": fig_i2,
                "name": "Tree Map",
            }
        )
