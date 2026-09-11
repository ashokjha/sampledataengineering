import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc import DataConfigEngine


class ThreeDChartEngine(BaseChartEngine):
    """<b>3D & Advanced Technical Charts</b>
    Best libraries: <b>Plotly</b> or <b>Matplotlib (mplot3d)</b>
    <ul><b>3D Scatter Plot:</b> Plots data points across X, Y, and Z axes.</ul>
    <ul><b>3D Surface Plot:</b> Generates a continuous three-dimensional terrain map of data.</ul>
    <ul><b>Parallel Coordinates Plot:</b> Visualizes high-dimensional, multivariate data profiles.</ul>
    <ul><b>Word Cloud:</b> Displays text data where the size of each word reflects its frequency
    (requires <b>wordcloud</b>).
    """

    def __init__(self):
        super().__init__()
        self.charts = []
        self.dce = DataConfigEngine()
        self.df = self.dce.fetchData("3D")

    def render_all(self) -> list[dict]:
        # 1. 3D Scatter
        self.threeDScatter(self.df)
        return self.charts

    def threeDScatter(self, data: pd.DataFrame) -> None:
        # 1. 3D Scatter
        fig_s1 = plt.figure(figsize=(6, 4))
        ax = fig_s1.add_subplot(111, projection="3d")
        ax.scatter(
            self.df["X"], self.df["Y"], self.df["Z"], c=self.df["Z"], cmap="viridis"
        )
        ax.set_title("Static 3D Scatter Plot")

        fig_i1 = px.scatter_3d(
            self.df, x="X", y="Y", z="Z", color="Z", title="Interactive 3D Scatter"
        )
        chart = {
            "title": "3D Scatter Cluster",
            "static": fig_s1,
            "interactive": fig_i1,
            "name": "3D Scatter",
        }
        self.charts.append(chart)
