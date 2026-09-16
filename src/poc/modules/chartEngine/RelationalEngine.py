import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc import DataConfigEngine


class RelationEngine(BaseChartEngine):
    """<b>Relational & Trend Charts</b>
    Best libraries:<b> Matplotlib</b>, <b>Seaborn</b>, or <b>Plotly (for interactivity)</b>
    <OL>
    <li><b>Line Chart:</b> Shows trends over a continuous period or time series.</li>
    <li><b>Scatter Plot:</b> Displays the relationship between two continuous variables.</li>
    <li><b>Bubble Chart:</b> A scatter plot where a third variable determines the size of the bubbles.</li>
    <li><b>Connected Scatter Plot:</b> A scatter plot where points are joined chronologically by a line.</li>
    <li><b>Area Chart:</b>A line chart where the area underneath the trend line is filled with color.</li>
    <li><b>Stacked Area Chart:</b> Shows how multiple groups contribute to a total over time.</li>
    </ol>
    """

    def __init__(self):
        super().__init__()
        self.dce = DataConfigEngine()
        self.charts = []

    def render_all(self) -> list[dict]:
        # 1: Line Chart
        lcdf = self.dce.fetchData("Relational_Line")
        self.render_linechart(lcdf)

        # 2. Scatter Plot
        scdf = self.dce.fetchData("Relational_scatter")
        self.render_scatter_plot(scdf)

        # 3. Bubble chart
        bbdf = self.dce.fetchData("Relational_bubble")
        self.render_bubble_chart(bbdf)

        # 4. Connected Scatter Plot
        cscdf = self.dce.fetchData("Relational_conn_scatter")
        self.render_conn_scatter_plot(cscdf)

        # 5. Area Chart
        arcdf = self.dce.fetchData("Relational_area")
        self.render_area_chart(arcdf)

        # 6. Stacked Area Chart
        scardf = self.dce.fetchData("Relational_stacked_area")
        self.render_stacked_area_chart(scardf)

        return self.charts

    def render_linechart(self, lcdf) -> None:
        # 1. Line Chart
        line_fig_s, ax = plt.subplots(figsize=(6, 4))
        sns.lineplot(data=lcdf, x="Date", y="Metric_A", ax=ax, color="#ff7f0e")
        ax.set_title("Static Line Chart")
        plt.xticks(rotation=45)
        line_fig_i = px.line(
            lcdf, x="Date", y="Metric_A", title="Interactive Line Chart"
        )
        chart = {
            "title": "Line Chart Trend",
            "static": line_fig_s,
            "interactive": line_fig_i,
            "name": "Line Chart",
        }
        self.charts.append(chart)

    def render_scatter_plot(self, scdf) -> None:
        # 2. Scatter Plot
        scatter_fig_s, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(data=scdf, x="Metric_A", y="Metric_B", ax=ax, color="#9467bd")
        ax.set_title("Static Scatter Plot")
        scatter_fig_i = px.scatter(
            scdf, x="Metric_A", y="Metric_B", title="Interactive Scatter Plot"
        )
        chart = {
            "title": "Scatter Plot Correlation",
            "static": scatter_fig_s,
            "interactive": scatter_fig_i,
            "name": "Scatter Plot",
        }
        self.charts.append(chart)

    def render_bubble_chart(self, bubbledf: pd.DataFrame) -> None:
        # 3. Bubble Chart
        # Static
        # Create a multi-plot static grid split by Quarter
        bbgrid = sns.relplot(
            data=bubbledf,
            x="Marketing_Spend",
            y="Revenue",
            hue="Status",
            size="Team_Size",
            col="Quarter",  # Creates a subplot column for each quarter
            col_wrap=2,  # Wraps the layout into a 2x2 grid
            sizes=(100, 800),  # Minimum and maximum bubble size restrictions
            alpha=0.7,
            palette="Set1",
            kind="scatter",
            height=4,
            aspect=1.2,
        )

        # Customise formatting and titles
        bbgrid.set_axis_labels("Marketing Budget ($)", "Total Revenue ($)")
        bbgrid.fig.suptitle(
            "Static Multi-Quarter Project Bubble Charts",
            y=1.02,
            fontsize=14,
            weight="bold",
        )

        # plt.show()
        bubble_fig_s = bbgrid.figure

        # Interactive
        bubble_fig_i = px.scatter(
            bubbledf,
            x="Marketing_Spend",
            y="Revenue",
            size="Team_Size",
            color="Status",
            hover_name="Project_Name",
            animation_frame="Quarter",  # The magical timeline component
            animation_group="Project_Name",  # Tracks individual bubble identities across frames
            size_max=50,
            title="Interactive Timeline: Project Growth Matrix (Q1 - Q4)",
            labels={
                "Marketing_Spend": "Marketing Budget Spent ($)",
                "Revenue": "Revenue Achieved ($)",
                "Team_Size": "Active Team Members",
            },
            # Fix the axis limits so the chart dimensions don't jump around wildly during playback
            range_x=[0, 65000],
            range_y=[0, 200000],
        )

        # Layout aesthetics configuration
        bubble_fig_i.update_layout(
            plot_bgcolor="rgba(240, 240, 240, 0.5)", margin=dict(l=40, r=40, t=60, b=40)
        )

        chart = {
            "title": "Bubble Chart",
            "static": bubble_fig_s,
            "interactive": bubble_fig_i,
            "name": "Bubble Chart",
        }
        self.charts.append(chart)

    def render_conn_scatter_plot(self, cscdf: pd.DataFrame) -> None:
        # 4. Connected Scatter Plot
        # Static
        # Set figure size and style
        csc_fig_s = plt.figure(figsize=(9, 5))
        plt.style.use(
            "seaborn-v0_8-whitegrid"
        )  # Optional: Adds a clean grid background

        # Plot the connected scatter plot
        plt.plot(
            cscdf["Month"],
            cscdf["Growth_Metric"],
            marker="o",  # Circle markers for points
            linestyle="-",  # Solid line connecting points
            color="#1f77b4",  # Custom professional blue color
            linewidth=2,  # Thinness/thickness of the connecting line
            markersize=8,  # Visual weight of the individual scatter points
            markerfacecolor="red",  # Contrasting marker color
        )

        # Customize titles and labels
        plt.title(
            "Monthly Growth Projection (Static Layout)",
            fontsize=14,
            fontweight="bold",
            pad=15,
        )
        plt.xlabel("Timeline", fontsize=12)
        plt.ylabel("User Count (Thousands)", fontsize=12)

        # Display the static chart
        plt.tight_layout()

        # Interactive
        csc_fig_i = px.line(
            cscdf,
            x="Month",
            y="Growth_Metric",
            title="Monthly Growth Projection (Interactive Layout)",
            markers=True,  # This forces markers to appear on top of the line
            labels={"Growth_Metric": "User Count (K)", "Month": "Timeline"},
        )

        # Fine-tune the visuals (marker sizes, line color, hover formatting)
        csc_fig_i.update_traces(
            marker=dict(size=10, color="red", symbol="circle"),
            line=dict(width=3, color="#1f77b4"),
            hovertemplate="<b>Month:</b> %{x}<br><b>Users:</b> %{y}K<extra></extra>",
        )

        # Apply a clean, modern template alignment
        csc_fig_i.update_layout(
            title_font_size=18,
            hovermode="x unified",  # Triggers tooltips for matching X value positions
            template="plotly_white",
        )
        chart = {
            "title": "Monthly Growth Projection Connected Scatter plot",
            "static": csc_fig_s,
            "interactive": csc_fig_i,
            "name": "Monthly Growth Projection Connected Scatter plot",
        }
        self.charts.append(chart)

    def render_area_chart(self, acdf: pd.DataFrame) -> None:
        # 5. Area Chart Plot
        # Static
        # 1. Initialize the layout
        ac_fig_s = plt.figure(figsize=(8, 5))

        # 2. Plot the line outline and fill the area beneath it
        plt.plot(
            acdf["Day"], acdf["Visitors"], color="SlateBlue", alpha=0.6, linewidth=2
        )
        plt.fill_between(acdf["Day"], acdf["Visitors"], color="SkyBlue", alpha=0.4)

        # 3. Add labels, title, and clean styling
        plt.title(
            "Weekly Website Traffic (Static View)",
            fontsize=14,
            fontweight="bold",
            loc="left",
        )
        plt.xlabel("Day of the Week", fontsize=12)
        plt.ylabel("Number of Visitors", fontsize=12)
        plt.grid(axis="y", linestyle="--", alpha=0.5)

        # 4. Display the static plot
        plt.tight_layout()

        # Interactive
        # 1. Generate the interactive area plot
        ac_fig_i = px.area(
            acdf,
            x="Day",
            y="Visitors",
            title="Weekly Website Traffic (Interactive View)",
        )

        # 2. Customise traces and aesthetics
        ac_fig_i.update_traces(
            line_color="SlateBlue",
            fillcolor="rgba(135, 206, 235, 0.4)",  # Semi-transparent SkyBlue using RGBA
        )

        # 3. Enhance layout details
        ac_fig_i.update_layout(
            title_font_size=16,
            xaxis_title="Day of the Week",
            yaxis_title="Number of Visitors",
            template="plotly_white",
        )
        chart = {
            "title": "Weekly Website Traffic Area Chart",
            "static": ac_fig_s,
            "interactive": ac_fig_i,
            "name": "Weekly Website Traffic Area Chart",
        }
        self.charts.append(chart)

    def render_stacked_area_chart(self, stardf: pd.DataFrame) -> None:
        # 6. stackedAreaData
        # static
        # Initialize figure and axes
        star_fig_s, ax = plt.subplots(figsize=(10, 6), dpi=100)

        # Colors for the layers
        colors = ["#2b5c8f", "#4682b4", "#6baed6"]

        # Plotting the stacked area chart
        ax.stackplot(
            stardf["Quarter"],
            stardf["Hardware"],
            stardf["Software"],
            stardf["Services"],
            labels=["Hardware", "Software", "Services"],
            colors=colors,
            alpha=0.85,
        )

        # Customizing the visual aesthetics
        ax.set_title(
            "Company Revenue Stream Breakdown (2024 - 2026)",
            fontsize=14,
            pad=15,
            weight="bold",
        )
        ax.set_xlabel("Timeline (Quarters)", fontsize=11, labelpad=10)
        ax.set_ylabel("Revenue (in $ Millions)", fontsize=11, labelpad=10)

        # Grid lines for easier numerical reading
        ax.grid(axis="y", linestyle="--", alpha=0.3)

        # Repositioning legend to avoid overlapping data layers
        ax.legend(loc="upper left", frameon=True, facecolor="white", edgecolor="none")

        # Clean layout and display
        plt.xticks(rotation=45)
        plt.tight_layout()

        # interactive
        # Generate interactive area plot
        star_fig_i = px.area(
            stardf,
            x="Quarter",
            y=["Hardware", "Software", "Services"],
            title="Interactive Revenue Tracking by Segment",
            labels={"value": "Revenue (Millions)", "variable": "Department"},
            color_discrete_sequence=["#2b5c8f", "#4682b4", "#6baed6"],
        )

        # Refine hover behaviors and structural styling
        star_fig_i.update_layout(
            hovermode="x unified",  # Shows all segment values simultaneously on crosshair hover
            xaxis_title="Timeline (Quarters)",
            yaxis_title="Revenue (in $ Millions)",
            title_font_size=18,
            legend_title_text="Segments",
        )

        chart = {
            "title": "Company Revenue Stream Breakdown (2024 - 2026) Stacked Area Chart",
            "static": star_fig_s,
            "interactive": star_fig_i,
            "name": "Company Revenue Stream Breakdown (2024 - 2026) Stacked Area Chart",
        }
        self.charts.append(chart)
