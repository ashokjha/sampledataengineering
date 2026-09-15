import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import dash_bio as dashbio
import holoviews as hv
from holoviews import opts
from mpl_chord_diagram import chord_diagram
import pandas as pd
import numpy as np

from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc import DataConfigEngine


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
        self.dce = DataConfigEngine()

    def render_all(self) -> list[dict]:
        # 1. HeatMap
        heatmapDf = self.dce.fetchData("Matrix_Heatmap")
        self.heatMap(heatmapDf)

        # 2. clustur
        clusterDf = self.dce.fetchData("Matrix_Cluster")
        self.clusterMap(clusterDf)

        # 3. Sankey
        sankeyFlowDf = self.dce.fetchData("Matrix_Sankey_Flow")
        self.plotlySankeysankey(sankeyFlowDf)

        # 4. Chord
        chord_matrix_df = self.dce.fetchData("Matrix_Chord")
        self.chordDiagram(chord_matrix_df)

        return self.charts

    def heatMap(self, heatMapData: pd.DataFrame) -> None:
        """
        1. Heat Map
        """
        fig_s1, ax = plt.subplots(figsize=(6, 4))
        sns.heatmap(heatMapData, annot=True, cmap="coolwarm", ax=ax, cbar=True)
        ax.set_title("Static Heatmap Matrix")
        fig_i1 = px.imshow(
            heatMapData,
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

    def clusterMap(self, clusturDf: pd.DataFrame) -> None:
        """
        2. Clustermap
        """
        # Generate the static clustered heatmap
        g = sns.clustermap(
            clusturDf,
            cmap="viridis",  # Colormap
            linewidths=0.5,  # Grid line width
            annot=True,  # Display data values inside cells
            figsize=(8, 8),  # Plot dimensions
        )

        # Customize title (Accessing underlying matplotlib figure structure)
        g.figure.suptitle("Static Seaborn Clustermap", y=1.02, fontsize=16)

        # Create the interactive clustergram
        clustfig_i = dashbio.Clustergram(
            data=clusturDf.values,
            row_labels=list(clusturDf.index),
            column_labels=list(clusturDf.columns),
            color_map="Viridis",
            height=600,
            width=600,
        )

        # Update layout features
        clustfig_i.update_layout(title="Interactive Plotly Clustergram")
        self.charts.append(
            {
                "title": "Interactive Plotly Clustergram",
                "static": g.figure,
                "interactive": clustfig_i,
                "name": "Interactive Plotly Clustergram",
            }
        )

    def plotlySankeysankey(self, sankeydf: pd.DataFrame) -> None:
        """
        3. Relationship / Flow Chart (Plotly Sankey Template)
        """
        fig_sankey_s, ax = plt.subplots(figsize=(6, 4))
        # Static matrix replacement grid representation
        ax.scatter(
            sankeydf["Source"],
            sankeydf["Target"],
            s=sankeydf["Value"] * 20,
            color="teal",
            alpha=0.6,
        )
        ax.set_title("Static Flow Weight Scatter Grid")

        # Interactive Sankey Diagram
        all_nodes = list(set(sankeydf["Source"]).union(set(sankeydf["Target"])))
        node_indices = {node: idx for idx, node in enumerate(all_nodes)}

        fig_sankey_i = px.scatter(
            sankeydf,
            x="Source",
            y="Target",
            size="Value",
            color="Value",
            title="Interactive Bubble Relationship Grid",
        )
        self.charts.append(
            {
                "title": "Entity Relationship Grid",
                "static": fig_sankey_s,
                "interactive": fig_sankey_i,
                "name": "Plotly Sankey",
            }
        )

    def chordDiagram(self, chordDf: pd.DataFrame) -> None:
        """
        4. Chord Diagram
        """
        # Static
        chord_fig_s, ax = plt.subplots(figsize=(10, 10))
        chord_diagram(
            chordDf.values,
            names=chordDf.columns.tolist(),
            ax=ax,
            cmap="tab20",
            alpha=0.75,
            pad=2,
        )

        plt.title("Static Chord Diagram", fontsize=16, pad=35, fontweight="bold")

        # Interactive
        # hv.extension("bokeh")

        chord_fig_i = dashbio.Clustergram(
            data=chordDf.values,  # 2D NumPy array / list of lists
            row_labels=chordDf.index.tolist(),  # रो (Row) लेबल्स की लिस्ट
            column_labels=chordDf.columns.tolist(),  # कॉलम (Column) लेबल्स की लिस्ट
            color_map="Viridis",
            height=700,
            width=700,
        )

        chord_fig_i.update_layout(
            title="Interactive Business Matrix (Plotly/Dash)",
        )

        """

        df_inline_links = chordDf.stack().reset_index()
        df_inline_links.columns = ["source", "target", "value"]
        df_inline_links = df_inline_links[df_inline_links["value"] > 0]

        chord = hv.Chord(df_inline_links)

        chord.opts(
            opts.Chord(
                title="Interactive Chord Diagram (From df_matrix)",
                cmap="Category20",
                edge_cmap="Category20",
                edge_color=hv.dim("source").str(),
                node_color=hv.dim("index").str(),
                labels="index",
                width=700,
                height=700,
            )
        )
        """

        self.charts.append(
            {
                "title": "Chord Diagram Static",
                "static": chord_fig_s,
                "interactive": chord_fig_i,
                "name": "Chord Diagram",
            }
        )
