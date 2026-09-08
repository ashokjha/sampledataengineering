import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc.data.DataCreator import DataCreator


class RelationEngine(BaseChartEngine):
    """<b>Relational & Trend Charts</b>
    Best libraries:<b> Matplotlib</b>, <b>Seaborn</b>, or <b>Plotly (for interactivity)</b>
    <ul><b>Line Chart:</b> Shows trends over a continuous period or time series.</ul>
    <ul><b>Scatter Plot:</b> Displays the relationship between two continuous variables.</ul>
    <ul><b>Bubble Chart:</b> A scatter plot where a third variable determines the size of the bubbles.</ul>
    <ul><b>Connected Scatter Plot:</b> A scatter plot where points are joined chronologically by a line.</ul>
    <ul><b>Area Chart:</b>A line chart where the area underneath the trend line is filled with color.</ul>
    <ul><b>Stacked Area Chart:</b> Shows how multiple groups contribute to a total over time.</ul>
    """

    def __init__(self):
        super().__init__()
        np.random.seed(10)
        self.df = DataCreator.relationalData()
        self.charts = []

    def render_all(self) -> list[dict]:
        # 1: Line Chart
        self.render_linechart(self.df)

        # 2. Scatter Plot
        self.render_scatter_plot(self.df)

        return self.charts

    def render_linechart(self, df) -> None:
        # 1. Line Chart
        fig_s1, ax = plt.subplots(figsize=(6, 4))
        sns.lineplot(data=self.df, x="Date", y="Metric_A", ax=ax, color="#ff7f0e")
        ax.set_title("Static Line Chart")
        plt.xticks(rotation=45)
        fig_i1 = px.line(
            self.df, x="Date", y="Metric_A", title="Interactive Line Chart"
        )
        chart = {
            "title": "Line Chart Trend",
            "static": fig_s1,
            "interactive": fig_i1,
            "name": "Line Chart",
        }
        self.charts.append(chart)

    def render_scatter_plot(self, df) -> None:
        # 2. Scatter Plot
        fig_s2, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(
            data=self.df, x="Metric_A", y="Metric_B", ax=ax, color="#9467bd"
        )
        ax.set_title("Static Scatter Plot")
        fig_i2 = px.scatter(
            self.df, x="Metric_A", y="Metric_B", title="Interactive Scatter Plot"
        )
        chart = {
            "title": "Scatter Plot Correlation",
            "static": fig_s2,
            "interactive": fig_i2,
            "name": "Scatter Plot",
        }
        self.charts.append(chart)
