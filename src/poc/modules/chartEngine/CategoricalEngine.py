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
        # self.df1, self.groupedData, self.radar_df = self.dce.fetchData("Categorical")
        self.charts = []

    def render_all(self) -> list[dict]:
        # 1. Vertical Bar
        verticalBarDf = self.dce.fetchData("Categorical-vertical")
        self.barChart(verticalBarDf)

        # 2. Horizontal Bar
        horizontalDf = self.dce.fetchData("Categorical-horizontal")
        self.horizontalBarChart(horizontalDf)

        # 3. Stacked Bar
        stackedDf = self.dce.fetchData("Categorical-stacked")
        self.stackedBarChart(stackedDf)

        # 4. Grouped Bar
        groupedDf = self.dce.fetchData("Categorical-grouped")
        self.groupedBarChart(groupedDf)

        # 5. Lollipop
        lollipopDf = self.dce.fetchData("Categorical-lollipop")
        self.lollipopChart(lollipopDf)

        # 6. Radar
        radarDf = self.dce.fetchData("Categorical-radar")
        self.radarChart(radarDf)
        return self.charts

    def barChart(self, verticaldf: pd.DataFrame) -> None:
        # --- 1. Product Verttical  BAR Chart  ---
        color_seq = px.colors.qualitative.Pastel
        vertbar_fig_s, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(
            data=verticaldf,
            x="Quarter",
            y="Sales",
            hue="Product",
            orient="v",
            ax=ax,
            palette="Set2",
        )
        ax.set_title("Static Vertical Bar Chart")

        vertical_bar_fig_i = px.bar(
            verticaldf,
            x="Quarter",
            y="Sales",
            color="Product",
            orientation="v",
            barmode="group",
            title="Interactive Bar Chart",
            color_discrete_sequence=px.colors.qualitative.Pastel,
        )
        self.charts.append(
            {
                "title": "Product Verttical Bar Chart",
                "static": vertbar_fig_s,
                "interactive": vertical_bar_fig_i,
                "name": "Product Verttical Bar Chart",
            }
        )

    def horizontalBarChart(self, horizDf: pd.DataFrame) -> None:
        # --- 2. Horizontal BAR Chart  ---
        color_seq = px.colors.qualitative.Pastel
        horizontal_fig_s, ax = plt.subplots(figsize=(6, 4))
        sns.barplot(
            data=horizDf,
            x="Sales",
            y="Quarter",
            hue="Product",
            orient="h",
            ax=ax,
            palette="Set2",
        )
        ax.set_title("Static Horizontal Bar Chart")

        horizontal_fig_i = px.bar(
            horizDf,
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
                "static": horizontal_fig_s,
                "interactive": horizontal_fig_i,
                "name": "Product Horizontal Bar Chart",
            }
        )

    def stackedBarChart(self, stackedDf: pd.DataFrame) -> None:
        # --- 3. STACKED BAR Chart ---
        stacked_fig_s, ax = plt.subplots(figsize=(6, 4))
        pivot_df = stackedDf.pivot_table(
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

        stacked_fig_i = px.bar(
            stackedDf,
            x="Quarter",
            y="Sales",
            color="Product",
            barmode="stack",
            title="Interactive Stacked Bar Chart",
        )
        self.charts.append(
            {
                "title": "Stacked Bar Composition",
                "static": stacked_fig_s,
                "interactive": stacked_fig_i,
                "name": "Stacked Bar Chart",
            }
        )

    def groupedBarChart(self, groupedDf: pd.DataFrame) -> None:
        # 4. Grouped Bar Chart

        fig_gbs, ax = plt.subplots(figsize=(6, 4))

        fig_gbs = px.bar(
            groupedDf,
            x="Quarter",
            y="Sales",
            color="Product",
            barmode="group",
            title="Quarterly Sales Comparison by Product",
            text_auto=True,
        )

        fig_gbi = px.bar(
            groupedDf,
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

    def lollipopChart(self, lollipopDf: pd.DataFrame) -> None:
        # --- 5. LOLLIPOP CHART ---
        # Initialize figure and axes
        lollipop_fig_s, ax = plt.subplots(figsize=(9, 5), dpi=100)

        # 1. Draw the stems (lines)
        ax.hlines(
            y=lollipopDf["Category"],
            xmin=0,
            xmax=lollipopDf["Sales"],
            color="#cccccc",  # Subtle grey stem to avoid visual noise
            linewidth=2,
        )

        # 2. Draw the candies (circles)
        ax.scatter(
            lollipopDf["Sales"],
            lollipopDf["Category"],
            color="#1f77b4",  # Primary accent color
            s=120,  # Size of the circle
            zorder=3,  # Forces circles to stay on top of the lines
        )

        # Customizing the visual aesthetics
        ax.set_title(
            "Top Product Categories by Sales Volume", fontsize=14, pad=15, weight="bold"
        )
        ax.set_xlabel("Sales (in Thousands)", fontsize=11, labelpad=10)

        # Add value labels inside or next to the circles for scannability
        for index, value in enumerate(lollipopDf["Sales"]):
            ax.text(
                value + 3,
                index,
                f"{value}k",
                va="center",
                fontsize=10,
                weight="semibold",
            )

        # Clean layout and remove extra borders (spines)
        ax.spines[["top", "right", "bottom"]].set_visible(False)
        ax.xaxis.set_visible(
            False
        )  # Hide X-axis since labels are directly on the points

        plt.tight_layout()

        # Interactive
        # Generate interactive lollipop plot
        lollipop_fig_i = px.scatter(
            lollipopDf,
            x="Sales",
            y="Category",
            title="Interactive Product Sales Performance",
            labels={"Sales": "Sales (Thousands)", "Category": "Product Category"},
        )

        # Draw the stems using error bars extending backwards to 0
        lollipop_fig_i.update_traces(
            marker=dict(size=14, color="#1f77b4", opacity=1),
            error_x=dict(
                type="data",
                symmetric=False,
                arrayminus=lollipopDf[
                    "Sales"
                ],  # Tells the line to extend all the way left to 0
                array=[0] * len(lollipopDf),  # No extension to the right
                color="#cccccc",
                thickness=2,
                width=0,  # Removes the crossbar cap at the end
            ),
        )

        # Refine hover behaviors and layout styling
        lollipop_fig_i.update_layout(
            hovermode="y",
            xaxis=dict(
                showgrid=True,
                gridcolor="#f0f0f0",
                range=[0, lollipopDf["Sales"].max() * 1.1],
            ),
            yaxis=dict(title=""),
            plot_bgcolor="white",
            title_font_size=18,
        )

        self.charts.append(
            {
                "title": "Lollipop Chart Metrics",
                "static": lollipop_fig_s,
                "interactive": lollipop_fig_i,
                "name": "Lollipop Chart",
            }
        )
        """
        lollipop_fig_s, ax = plt.subplots(figsize=(6, 4))
        sub_df = lollipopDf[lollipopDf["Product"] == "Software"]
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

        # Interactive
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
                "static": lollipop_fig_s,
                "interactive": fig_i3,
                "name": "Lollipop Chart",
            }
        )
        """

    def radarChart(self, radarDf: pd.DataFrame) -> None:
        # --- 6. RADAR CHART ---
        radar_fig_s = plt.figure(figsize=(6, 4))
        ax = radar_fig_s.add_subplot(111, polar=True)

        categories = list(radarDf["Metric"])
        N = len(categories)

        angles = [n / N * 2 * math.pi for n in range(N)]
        scores = list(radarDf["Score"]).copy()

        plt.xticks(angles, categories)

        angles_closed = angles + [angles[0]]
        scores_closed = scores + [scores[0]]

        ax.plot(
            angles_closed, scores_closed, linewidth=1, linestyle="solid", color="purple"
        )
        ax.fill(angles_closed, scores_closed, "purple", alpha=0.1)
        ax.set_title("Static Radar Chart", y=1.1)

        # Interactive Plotly कोड
        radar_fig_i = px.line_polar(
            radarDf,
            r="Score",
            theta="Metric",
            line_close=True,
            title="Interactive Radar Chart",
        )
        radar_fig_i.update_traces(fill="toself")

        self.charts.append(
            {
                "title": "Radar Performance Metrics",
                "static": radar_fig_s,
                "interactive": radar_fig_i,
                "name": "Radar Chart",
            }
        )
