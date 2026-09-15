import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import numpy as np
import math


from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc import DataConfigEngine


class CategoricalEngine(BaseChartEngine):
    """<b>Categorical & Comparison Charts</b>:
    Best libraries: <b>Matplotlib</b> or <b>PlotlyVertical</b>
    <ol>
    <li><b>Vertical Bar Chart:</b> Compares discrete categories by height.</li>
    <li><b>Horizontal Bar Chart:</b> Ideal for categories with long text labels.</li>
    <li><b>Stacked Bar Chart:</b> Breaks down categorical bars into smaller sub-segments.</li>
    <li><b>Grouped Bar Chart (Clustered):</b> Places sub-segments side-by-side for direct comparison.</li>
    <li><b>Lollipop Chart:</b> A clean alternative to bar charts using a line and a dot.</li>
    <li><b>Radar Chart (Spider Plot):</b> Compares multiple quantitative variables across categories.</li>
    </ol>
    """

    def __init__(self):
        super().__init__()
        self.dce = DataConfigEngine()
        self.df, self.groupedData, self.radar_df = self.dce.fetchData("Categorical")
        self.charts = []

    def render_all(self) -> list[dict]:
        self.barChart()
        self.horizontalBarChart()
        self.stackedBarChart()
        self.groupedBarChart()
        self.lollipopChart()
        self.radarChart()
        return self.charts

    def barChart(self) -> None:
        # --- 1. Product Verttical  BAR Chart  ---
        color_seq = px.colors.qualitative.Pastel
        fig_s1, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(
            data=self.df,
            x="Quarter",
            y="Sales",
            hue="Product",
            orient="v",
            ax=ax,
            palette="Set2",
        )
        ax.set_title("Static Vertical Bar Chart")

        fig_i1 = px.bar(
            self.df,
            x="Quarter",
            y="Sales",
            color="Product",
            orientation="v",
            # barmode="group",
            title="Interactive Bar Chart",
            color_discrete_sequence=px.colors.qualitative.Pastel,
        )
        self.charts.append(
            {
                "title": "Product Verttical Bar Chart",
                "static": fig_s1,
                "interactive": fig_i1,
                "name": "Product Verttical Bar Chart",
            }
        )

    def horizontalBarChart(self) -> None:
        # --- 2. Horizontal BAR Chart  ---
        color_seq = px.colors.qualitative.Pastel
        fig_s1, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(
            data=self.df,
            x="Sales",
            y="Quarter",
            hue="Product",
            orient="h",
            ax=ax,
            palette="Set2",
        )
        ax.set_title("Static Horizontal Bar Chart")

        fig_i1 = px.bar(
            self.df,
            x="Sales",
            y="Quarter",
            color="Product",
            orientation="h",
            barmode="group",
            title="Interactive Horizontal Bar Chart",
            color_discrete_sequence=px.colors.qualitative.Pastel,
        )
        self.charts.append(
            {
                "title": "Product Horizontal Bar Chart",
                "static": fig_s1,
                "interactive": fig_i1,
                "name": "Product Horizontal Bar Chart",
            }
        )

    def stackedBarChart(self) -> None:
        # --- 3. STACKED BAR Chart ---
        fig_s2, ax = plt.subplots(figsize=(6, 4))
        pivot_df = self.groupedData.pivot_table(
            index="Quarter", columns="Product", values="Sales", aggfunc="sum"
        )
        pivot_df.plot(
            kind="bar",
            stacked=True,
            ax=ax,
            color=["#cb6666", "#ddaa66", "#66dd6c"],
        )
        ax.set_title("Static Stacked Bar Chart")
        plt.xticks(rotation=0)

        fig_i2 = px.bar(
            self.groupedData,
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
                "name": "Stacked Bar Chart",
            }
        )

    def groupedBarChart(self) -> None:
        # 4. Grouped Bar Chart

        fig_gbs, ax = plt.subplots(figsize=(6, 4))

        fig_gbs = px.bar(
            self.groupedData,
            x="Quarter",
            y="Sales",
            color="Product",
            barmode="group",
            title="Quarterly Sales Comparison by Product",
            text_auto=True,
        )

        fig_gbi = px.bar(
            self.groupedData,
            x="Quarter",
            y="Sales",
            color="Product",
            barmode="group",
            title="Quarterly Sales Comparison by Product",
            labels={
                "Sales": "Sales (Units)",
                "Quarter": "Financial Quarter",
            },
            text_auto=".0f",
            hover_data={"Sales": ":$,.0f"},
        )

        fig_gbi.update_layout(
            hovermode="x unified",
            xaxis={"categoryorder": "category ascending"},
            legend_title_text="Products List",
        )
        self.charts.append(
            {
                "title": "Grouped Bar Sales",
                "static": fig_gbs,
                "interactive": fig_gbi,
                "name": "Grouped Bar Sales",
            }
        )

    def lollipopChart(self) -> None:
        # --- 5. LOLLIPOP CHART ---
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
        # --- 6. RADAR CHART ---
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
