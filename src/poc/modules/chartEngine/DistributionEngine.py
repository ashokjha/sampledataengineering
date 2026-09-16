import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import numpy as np

from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc import DataConfigEngine


class DistributionEngine(BaseChartEngine):
    """<b>Statistical & Distribution Charts:</b>
    Best libraries: <b>Seaborn</b> or <b>Matplotlib</b>
    <OL>
    <li> <b>Histogram:</b> Visualizes the distribution of a single continuous variable.</li>
    <li> <b>Box Plot:</b> Displays the median, quartiles, and outliers of a dataset.</li>
    <li> <b>Violin Plot:</b> Combines a box plot with a kernel density plot to show data shape.</li>
    <li> <b>Density Plot (KDE):</b> Shows the probability density function of the data.</li>
    <li> <b>Strip / Swarm Plot:</b> Plots every individual data point to show exact distribution.</li>
    <li> <b>Error Bar Chart: </b> Shows error or uncertainty along with the main data points.</li>
    </OL>
    """

    def __init__(self):
        super().__init__()
        np.random.seed(50)
        self.dce = DataConfigEngine()
        self.charts = []

    def render_all(self) -> list[dict]:
        self.distributiondf = self.dce.fetchData("Distribution")

        self.render_histogram(self.distributiondf, "Value")
        self.render_boxplot(self.distributiondf, "Category", "Value")
        self.render_violinplot(self.distributiondf, "Category", "Value")
        self.render_density_plot(self.distributiondf, "Value")
        self.render_swarm_plot(self.distributiondf, "Category", "Value")
        self.render_error_bar_chart(self.distributiondf, "Category", "Value")
        return self.charts

    def render_histogram(self, df, column) -> None:
        """1. Histogram."""
        # 1. Static (Seaborn)
        fig_static, ax = plt.subplots(figsize=(8, 5))
        sns.histplot(
            data=self.distributiondf, x=column, kde=True, ax=ax, color="#1f77b4"
        )
        ax.set_title(f"Static Histogram of {column}")

        # 2. Interactive (Plotly)
        fig_interactive = px.histogram(
            self.distributiondf,
            x=column,
            marginal="rug",
            title=f"Interactive Histogram of {column}",
            color_discrete_sequence=["#1f77b4"],
        )
        chartDct = {
            "title": "Histogram & Density (KDE)",
            "static": fig_static,
            "interactive": fig_interactive,
            "name": "1_histogram",
        }
        self.charts.append(chartDct)

    def render_boxplot(self, df, x_col, y_col) -> None:
        """2. Box Plot."""
        # 1. Static (Seaborn)
        fig_static, ax = plt.subplots(figsize=(8, 5))
        sns.boxplot(data=df, x=x_col, y=y_col, ax=ax, palette="Set2")
        ax.set_title(f"Static Box Plot: {y_col} by {x_col}")

        # 2. Interactive (Plotly)
        fig_interactive = px.box(
            df,
            x=x_col,
            y=y_col,
            color=x_col,
            title=f"Interactive Box Plot: {y_col} by {x_col}",
            color_discrete_sequence=px.colors.qualitative.Set2,
        )
        chartDct = {
            "title": "Box Plot (Outlier & Quartiles)",
            "static": fig_static,
            "interactive": fig_interactive,
            "name": "2_boxplot",
        }
        self.charts.append(chartDct)

    def render_violinplot(self, df, x_col, y_col) -> None:
        """3. Violin ."""

        # 1. Static (Seaborn)
        fig_static, ax = plt.subplots(figsize=(8, 5))
        sns.violinplot(data=df, x=x_col, y=y_col, ax=ax, palette="Pastel1")
        ax.set_title(f"Static Violin Plot: {y_col} by {x_col}")

        # 2. Interactive (Plotly)
        fig_interactive = px.violin(
            df,
            x=x_col,
            y=y_col,
            color=x_col,
            box=True,
            points="all",
            title=f"Interactive Violin Plot: {y_col} by {x_col}",
            color_discrete_sequence=px.colors.qualitative.Pastel1,
        )

        chartDct = {
            "title": "Violin Plot (Probability Density Distribution)",
            "static": fig_static,
            "interactive": fig_interactive,
            "name": "3_violinplot",
        }
        self.charts.append(chartDct)

    def render_density_plot(self, df, column) -> None:
        """4. Density Plot (KDE)."""
        # 1. Static (Seaborn)
        fig_static, ax = plt.subplots(figsize=(8, 5))
        sns.kdeplot(data=df, x=column, fill=True, color="#2ca02c", alpha=0.5, ax=ax)
        ax.set_title(f"Static Density Plot (KDE) of {column}")

        # 2. Interactive (Plotly)
        # Plotly doesn't have a native continuous KDE line, so we use a histogram with probability density
        fig_interactive = px.histogram(
            df,
            x=column,
            histnorm="probability density",
            title=f"Interactive Density Plot of {column}",
            color_discrete_sequence=["#2ca02c"],
        )
        chartDct = {
            "title": "Density Plot (Continuous Data Shape)",
            "static": fig_static,
            "interactive": fig_interactive,
            "name": "4_density",
        }
        self.charts.append(chartDct)

    def render_swarm_plot(self, df, x_col, y_col) -> None:
        """5. Strip/Swarm Plot."""
        # 1. Static (Seaborn Strip Plot - cleaner for larger data than pure Swarm)
        fig_static, ax = plt.subplots(figsize=(8, 5))
        sns.stripplot(
            data=df,
            x=x_col,
            y=y_col,
            jitter=True,
            size=5,
            ax=ax,
            palette="Dark2",
            hue=x_col,
            legend=False,
        )
        ax.set_title(f"Static Strip Plot: {y_col} by {x_col}")

        # 2. Interactive (Plotly Strip)
        fig_interactive = px.strip(
            df,
            x=x_col,
            y=y_col,
            color=x_col,
            title=f"Interactive Strip Plot: {y_col} by {x_col}",
            color_discrete_sequence=px.colors.qualitative.Dark2,
        )

        chartDct = {
            "title": "Strip / Swarm Plot (Individual Data Points)",
            "static": fig_static,
            "interactive": fig_interactive,
            "name": "5_stripplot",
        }
        self.charts.append(chartDct)

    def render_error_bar_chart(self, df, x_col, y_col) -> None:
        """6. Error Bar"""
        # Calculate group aggregates for error calculation
        summary = df.groupby(x_col)[y_col].agg(["mean", "std"]).reset_index()

        # 1. Static (Matplotlib / Seaborn)
        fig_static, ax = plt.subplots(figsize=(8, 5))
        ax.errorbar(
            x=summary[x_col],
            y=summary["mean"],
            yerr=summary["std"],
            fmt="o",
            color="#d62728",
            ecolor="black",
            elinewidth=2,
            capsize=5,
            ms=8,
        )

        ax.set_title(f"Static Error Bar Chart (Mean ± SD) of {y_col}")
        ax.set_xlabel(x_col)
        ax.set_ylabel(f"Mean {y_col}")

        # 2. Interactive (Plotly)
        fig_interactive = px.scatter(
            summary,
            x=x_col,
            y="mean",
            error_y="std",
            title=f"Interactive Error Bar Chart (Mean ± SD) of {y_col}",
            color_discrete_sequence=["#d62728"],
        )
        fig_interactive.update_traces(marker=dict(size=10))
        chartDct = {
            "title": "Error Bar Chart (Statistical Variances & Means)",
            "static": fig_static,
            "interactive": fig_interactive,
            "name": "6_errorbar",
        }
        self.charts.append(chartDct)
