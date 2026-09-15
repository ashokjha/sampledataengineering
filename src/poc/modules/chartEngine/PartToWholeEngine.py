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

    def render_all(self) -> list[dict]:
        # 1. Pie chart
        piechrtdf = self.dce.fetchData("Part2Whole_Pie")
        self.pieChart(piechrtdf)

        # 2. Donut Data
        dndf = self.dce.fetchData("Part2Whole_Donut")
        self.doNutChart(dndf)

        # 3. Tree Map
        treemapdf = self.dce.fetchData("Part2Whole_treemap")
        self.treeMap(treemapdf)

        # 4. Sunburst Chart

        return self.charts

    def pieChart(self, pie_df: pd.DataFrame) -> None:
        """1. Pie Chart

        Args:
            pie_df (pd.DataFrame): _description_
        """
        explode = [0.1, 0, 0, 0, 0, 0]

        piech_fig_s, ax = plt.subplots(figsize=(8, 8))

        ax.pie(
            pie_df["Market_Share"],
            labels=pie_df["Brand"],
            autopct="%1.1f%%",
            startangle=140,
            explode=explode,
            colors=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#7f7f7f"],
        )
        plt.title("EV Market Share - Static View", fontsize=16, fontweight="bold")

        # Interactive
        piech_fig_i = px.pie(
            pie_df,
            values="Market_Share",
            names="Brand",
            title="EV Market Share - Interactive View",
            color_discrete_sequence=px.colors.sequential.RdBu,
        )

        piech_fig_i.update_traces(textinfo="percent+label")
        self.charts.append(
            {
                "title": "Pie Chart",
                "static": piech_fig_s,
                "interactive": piech_fig_i,
                "name": "Pie Chart",
            }
        )

    def doNutChart(self, dndf: pd.DataFrame) -> None:
        # 2. Donut Chart
        fig_dndf_s, ax = plt.subplots(figsize=(6, 4))
        ax.pie(
            dndf["Values"],
            labels=dndf["Labels"],
            autopct="%1.1f%%",
            startangle=90,
            wedgeprops=dict(width=0.4, edgecolor="w"),
            colors=sns.color_palette("Pastel1"),
        )
        ax.set_title("Static Donut Chart")

        fig_dndf_i = px.pie(
            dndf,
            names="Labels",
            values="Values",
            hole=0.4,
            title="Interactive Donut Chart",
        )
        self.charts.append(
            {
                "title": "Donut Proportions",
                "static": fig_dndf_s,
                "interactive": fig_dndf_i,
                "name": "Donut Chart",
            }
        )

    def treeMap(self, treeDf: pd.DataFrame) -> None:
        # 3. Treemap
        fig_treemap_s, ax = plt.subplots(figsize=(6, 4))
        # Since squarify requires external installation, we can build a clean horizontal stacked block layout for static
        cumulative = 0
        for i, row in treeDf.iterrows():
            ax.barh("Total Share", row["Values"], left=cumulative, label=row["Labels"])
            cumulative += row["Values"]
        ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=5)
        ax.set_title("Static Proportional Share Tree Map Chart")

        fig_treemap_i = px.treemap(
            treeDf, path=["Labels"], values="Values", title="Interactive Treemap"
        )
        self.charts.append(
            {
                "title": "Treemap Hierarchy",
                "static": fig_treemap_s,
                "interactive": fig_treemap_i,
                "name": "Tree Map",
            }
        )
