import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import numpy as np

from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc.data.DataCreator import DataCreator


class MatrixEngine(BaseChartEngine):
    """<b>Matrix & Relationship Charts</b>
    Best libraries: <b>Seaborn</b> or </b>Holoviews</b>
    <ul><b>Heatmap:</b> Uses a color-coded grid to plot two-dimensional categorical data
    (e.g., correlation matrices).</ul>
    <ul><b>Clustermap:</b> A heatmap that uses hierarchical clustering to group similar rows and columns.</ul>
    <ul><b>Sankey Diagram:</b> Visualizes flows and volumes from one set of values to another.</ul>
    <ul><b>Chord Diagram:</b> Shows inter-relationships between entities in a circular layout.</ul>
    """

    def __init__(self):
        super().__init__()
        self.charts = []
        self.df_matrix, self.df_flow = DataCreator.matrixAndRelationData()

    def render_all(self) -> list[dict]:
        self.heatMap()
        self.plotlySankeysankey()
        return self.charts

    def heatMap(self) -> None:
        """
        Heat Map
        """
        fig_s1, ax = plt.subplots(figsize=(6, 4))
        sns.heatmap(self.df_matrix, annot=True, cmap="coolwarm", ax=ax, cbar=True)
        ax.set_title("Static Heatmap Matrix")
        fig_i1 = px.imshow(
            self.df_matrix,
            text_auto=True,
            color_continuous_scale="RdBu_r",
            title="Interactive Heatmap",
        )
        self.charts.append(
            {
                "title": "Heatmap Correlation Matrix",
                "static": fig_s1,
                "interactive": fig_i1,
                "name": "HeatMap",
            }
        )

    def plotlySankeysankey(self) -> None:
        """
        Relationship / Flow Chart (Plotly Sankey Template)
        """
        fig_s2, ax = plt.subplots(figsize=(6, 4))
        # Static matrix replacement grid representation
        ax.scatter(
            self.df_flow["Source"],
            self.df_flow["Target"],
            s=self.df_flow["Value"] * 20,
            color="teal",
            alpha=0.6,
        )
        ax.set_title("Static Flow Weight Scatter Grid")

        # Interactive Sankey Diagram
        all_nodes = list(set(self.df_flow["Source"]).union(set(self.df_flow["Target"])))
        node_indices = {node: idx for idx, node in enumerate(all_nodes)}

        fig_i2 = px.scatter(
            self.df_flow,
            x="Source",
            y="Target",
            size="Value",
            color="Value",
            title="Interactive Bubble Relationship Grid",
        )
        self.charts.append(
            {
                "title": "Entity Relationship Grid",
                "static": fig_s2,
                "interactive": fig_i2,
                "name": "Plotly Sankey",
            }
        )
