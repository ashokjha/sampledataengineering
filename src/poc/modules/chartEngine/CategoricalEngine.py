import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np
import math


from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc.data.DataCreator import DataCreator


class CategoricalEngine(BaseChartEngine):
    """<b>Categorical & Comparison Charts</b>:
    Best libraries: <b>Matplotlib</b> or <b>PlotlyVertical</b>
    <ul><b>Bar Chart:</b> Compares discrete categories by height.</ul>
    <ul><b>Horizontal Bar Chart:</b> Ideal for categories with long text labels.</ul>
    <ul><b>Stacked Bar Chart:</b> Breaks down categorical bars into smaller sub-segments.</ul>
    <ul><b>Grouped Bar Chart (Clustered):</b> Places sub-segments side-by-side for direct comparison.</ul>
    <ul></b>Lollipop Chart:</b> A clean alternative to bar charts using a line and a dot.</ul>
    <ul><b>Radar Chart (Spider Plot):</b> Compares multiple quantitative variables across categories.</ul>
    """

    def __init__(self):
        super().__init__()
        self.df, self.radar_df = DataCreator.categoricalData()
        self.charts = []

    def render_all(self) -> list[dict]:
        self.barChart()
        self.stackedBarChart()
        self.lollipopChart()
        self.radarChart()
        return self.charts

    def barChart(self) -> None:
        # --- 1. BAR CHART  ---
        color_seq = px.colors.qualitative.Pastel
        fig_s1, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(
            data=self.df,
            x="Quarter",
            y="Sales",
            hue="Product",
            ax=ax,
            palette="Set2",
        )
        ax.set_title("Static Grouped Bar Chart")

        fig_i1 = px.bar(
            self.df,
            x="Quarter",
            y="Sales",
            color="Product",
            barmode="group",
            title="Interactive Grouped Bar Chart",
            color_discrete_sequence=px.colors.qualitative.Pastel,
        )
        self.charts.append(
            {
                "title": "Grouped Bar Analysis",
                "static": fig_s1,
                "interactive": fig_i1,
                "name": "Bar Chart",
            }
        )

    def stackedBarChart(self) -> None:
        # --- 2. STACKED BAR CHART ---
        fig_s2, ax = plt.subplots(figsize=(6, 4))
        pivot_df = self.df.pivot_table(
            index="Quarter", columns="Product", values="Sales", aggfunc="sum"
        )
        pivot_df.plot(kind="bar", stacked=True, ax=ax, color=["#cb6666", "#ddaa66"])
        ax.set_title("Static Stacked Bar Chart")
        plt.xticks(rotation=0)

        fig_i2 = px.bar(
            self.df,
            x="Quarter",
            y="Sales",
            color="Product",
            barmode="stack",
            title="Interactive Stacked Bar Chart",
        )
        self.charts.append(
            {
                "title": "Stacked Bar Composition",
                "static": fig_s2,
                "interactive": fig_i2,
                "name": "Stsacked Bar Chart",
            }
        )

    def lollipopChart(self) -> None:
        # --- 3. LOLLIPOP CHART ---
        fig_s3, ax = plt.subplots(figsize=(6, 4))
        sub_df = self.df[self.df["Product"] == "Software"]
        ax.hlines(
            y=sub_df["Quarter"],
            xmin=0,
            xmax=sub_df["Sales"],
            color="skyblue",
            linewidth=2,
        )
        ax.scatter(sub_df["Sales"], sub_df["Quarter"], color="blue", s=80, zorder=3)
        ax.set_title("Static Lollipop Chart (Software Sales)")
        ax.set_xlabel("Sales")

        fig_i3 = px.scatter(
            sub_df, x="Sales", y="Quarter", title="Interactive Lollipop Chart"
        )
        fig_i3.update_traces(
            mode="lines+markers",
            line=dict(color="skyblue", width=4),
            marker=dict(color="blue", size=12),
        )
        self.charts.append(
            {
                "title": "Lollipop Chart Metrics",
                "static": fig_s3,
                "interactive": fig_i3,
                "name": "Lollipop Chart",
            }
        )

    def radarChart(self) -> None:
        # --- 4. RADAR CHART ---
        fig_s4 = plt.figure(figsize=(6, 4))
        ax = fig_s4.add_subplot(111, polar=True)

        categories = list(self.radar_df["Metric"])
        N = len(categories)

        angles = [n / N * 2 * math.pi for n in range(N)]
        scores = list(self.radar_df["Score"]).copy()

        plt.xticks(angles, categories)

        angles_closed = angles + [angles[0]]
        scores_closed = scores + [scores[0]]

        ax.plot(
            angles_closed, scores_closed, linewidth=1, linestyle="solid", color="purple"
        )
        ax.fill(angles_closed, scores_closed, "purple", alpha=0.1)
        ax.set_title("Static Radar Chart", y=1.1)

        # Interactive Plotly कोड
        fig_i4 = px.line_polar(
            self.radar_df,
            r="Score",
            theta="Metric",
            line_close=True,
            title="Interactive Radar Chart",
        )
        fig_i4.update_traces(fill="toself")

        self.charts.append(
            {
                "title": "Radar Performance Metrics",
                "static": fig_s4,
                "interactive": fig_i4,
                "name": "Radar Chart",
            }
        )
