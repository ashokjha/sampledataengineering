import pandas as pd
from pandas.plotting import parallel_coordinates
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import poc.data.threeD.ThreeDAdapter

from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc import DataConfigEngine


class ThreeDChartEngine(BaseChartEngine):
    """<b>3D & Advanced Technical Charts</b>
    Best libraries: <b>Plotly</b> or <b>Matplotlib (mplot3d)</b>
    <ol>
    <li><b>3D Scatter Plot:</b> Plots data points across X, Y, and Z axes.</li>
    <li><b>3D Surface Plot:</b> Generates a continuous three-dimensional terrain map of data.</li>
    <li><b>Parallel Coordinates Plot:</b> Visualizes high-dimensional, multivariate data profiles.</li>
    <li><b>Word Cloud:</b> Displays text data where the size of each word reflects its frequency
    (requires <b>wordcloud</b>).</li>
    """

    def __init__(self):
        super().__init__()
        self.charts = []
        self.dce = DataConfigEngine()

    def render_all(self) -> list[dict]:
        # 1. 3D Scatter
        self.scatterDf = self.dce.fetchData("3D_Scatter")
        self.threeDScatter(self.scatterDf)

        # 2. 3D Surface
        self.X, self.Y, self.surfacedf = self.dce.fetchData("3D_Surface")
        self.threeDSuface(self.X, self.Y, self.surfacedf)

        # 3. 3D Parallel Cordinates
        self.parralelCrdDf = self.dce.fetchData("3D_Par_Cord")
        self.threedParallelCordinates(self.parralelCrdDf)

        # 4 word cloud
        self.wordCloudDf = self.dce.fetchData("3D_Word_Cloud")

        self.wordCloud(self.wordCloudDf)

        return self.charts

    def wordCloud(self, datawithFreeq: pd.DataFrame) -> None:
        num_words = len(datawithFreeq)
        # 2. Distribute coordinates evenly across a 3D Sphere
        phi = np.pi * (np.sqrt(5.0) - 1.0)
        x_coords, y_coords, z_coords = [], [], []

        # Static
        for i in range(num_words):
            y = 1 - (i / float(num_words - 1)) * 2  # y goes from 1 to -1
            radius = np.sqrt(1 - y * y)  # radius at y

            theta = phi * i  # golden angle increment

            x = np.cos(theta) * radius
            z = np.sin(theta) * radius

            x_coords.append(x)
            y_coords.append(y)
            z_coords.append(z)

        # 3. Plotting the Static 3D Word Cloud
        fig3dSwc = plt.figure(figsize=(10, 8))
        ax = fig3dSwc.add_subplot(111, projection="3d")

        # Hide grid lines and axes for a cleaner look
        ax.grid(False)
        ax.set_axis_off()

        # Color mapping based on word order
        colors = plt.cm.viridis(np.linspace(0, 1, num_words))

        # Draw each word in 3D space
        for i, (word, freq) in enumerate(datawithFreeq):
            # Scale font size dynamically based on frequency weight
            font_size = 10 + (freq / max(w[1] for w in datawithFreeq)) * 30

            ax.text(
                x_coords[i],
                y_coords[i],
                z_coords[i],
                word,
                size=font_size,
                color=colors[i],
                ha="center",
                va="center",
                zorder=1,
            )

        # Set equal bounds to preserve the sphere shape
        ax.set_xlim([-1.2, 1.2])
        ax.set_ylim([-1.2, 1.2])
        ax.set_zlim([-1.2, 1.2])

        plt.title("Static 3D Word Cloud", fontsize=16)

        # interactive
        x_coords.clear()
        y_coords.clear()
        z_coords.clear()

        for i in range(num_words):
            y = 1 - (i / float(num_words - 1)) * 2
            radius = np.sqrt(1 - y * y)
            theta = phi * i

            x_coords.append(np.cos(theta) * radius)
            y_coords.append(y)
            z_coords.append(np.sin(theta) * radius)
        # Separate words, frequencies, sizes, and colors for plotting
        words = [w[0] for w in datawithFreeq]
        frequencies = [w[1] for w in datawithFreeq]
        max_freq = max(frequencies)
        min_freq = min(frequencies)

        normalized = [(x - min_freq) / (max_freq - min_freq) for x in frequencies]

        # 2. Get a sample colorscale from Plotly Express (e.g., Viridis or Plasma)
        colorscale = px.colors.sequential.Viridis

        # Map text sizes dynamically
        text_sizes = [15 + (f / max_freq) * 45 for f in frequencies]
        color_strings = px.colors.sample_colorscale(colorscale, normalized)

        # 3. Create the Plotly figure

        fig3diwc = go.Figure(
            data=[
                go.Scatter3d(
                    x=x_coords,
                    y=y_coords,
                    z=z_coords,
                    mode="text",
                    text=words,
                    hoverinfo="text",
                    hovertext=[
                        f"Word: {w}<br>Frequency: {f}" for w, f in datawithFreeq
                    ],
                    textposition="middle center",
                    textfont=dict(color=color_strings),
                )
            ]
        )
        chart = {
            "title": "3D Word Cloud",
            "static": fig3dSwc,
            "interactive": fig3diwc,
            "name": "3D Word Cloud",
        }
        self.charts.append(chart)

    def threedParallelCordinates(self, parralelCrdData: pd.DataFrame) -> None:
        """3. 3D Parallel cordinates Plot
        Args:
            parralelCrdData (pd.DataFrame): _description_
        """
        # Static
        fig3DParallelStatic = plt.figure(figsize=(10, 5))
        ax = parallel_coordinates(
            parralelCrdData,
            class_column="Category",
            cols=["Price_USD", "Horsepower", "Fuel_Efficiency_MPG", "Safety_Rating"],
            colormap="Set1",
            linewidth=2.5,
        )

        plt.title("Custom Car Dataset - Static Parallel Coordinates", fontsize=14)
        plt.xlabel("Features")
        plt.ylabel("Values")
        plt.grid(True, alpha=0.3)
        plt.figimage
        # Interactive
        fig3DParallelInt = px.parallel_coordinates(
            parralelCrdData,
            color="Category_ID",
            dimensions=[
                "Price_USD",
                "Horsepower",
                "Fuel_Efficiency_MPG",
                "Safety_Rating",
            ],
            color_continuous_scale=px.colors.diverging.Tealrose,
            labels={
                "Price_USD": "Price ($)",
                "Horsepower": "HP",
                "Fuel_Efficiency_MPG": "MPG",
                "Safety_Rating": "Safety (1-5)",
            },
        )
        fig3DParallelInt.update_layout(
            coloraxis_colorbar=dict(
                title="Category",
                tickvals=[0, 1, 2, 3],
                ticktext=["Economy", "Sedan", "Sports", "Luxury"],
            ),
            title="Custom Car Dataset - Interactive Parallel Coordinates",
        )
        chart = {
            "title": "3D Parallel Cordinates",
            "static": fig3DParallelStatic,
            "interactive": fig3DParallelInt,
            "name": "3D Parallel Cordinates",
        }
        self.charts.append(chart)

    def threeDSuface(self, X: np.ndarray, Y: np.ndarray, surface: np.ndarray) -> None:
        """2.3D Surface
        Args:
            X (np.ndarray): _description_
            Y (np.ndarray): _description_
            surface (np.ndarray): _description_
        """
        # Static
        # 1. Set up the 3D axes
        fig3ss = plt.figure(figsize=(8, 6))
        ax = plt.axes(projection="3d")

        # 2. Create the surface plot
        surf = ax.plot_surface(X, Y, surface, cmap="viridis", edgecolor="none")

        # 3. Customize labels and look
        ax.set_title("Static 3D Surface Plot")
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.set_zlabel("Z Axis")
        fig3ss.colorbar(surf, shrink=0.5, aspect=10)  # Add a color scale bar

        # Interactive
        # 1. Build the interactive figure
        fig3is = go.Figure(data=[go.Surface(z=surface, x=X, y=Y, colorscale="Viridis")])

        # 2. Set layout options
        fig3is.update_layout(
            title="Interactive 3D Surface Plot",
            scene=dict(
                xaxis_title="X Axis", yaxis_title="Y Axis", zaxis_title="Z Axis"
            ),
            autosize=False,
            width=800,
            height=800,
            margin=dict(l=65, r=50, b=65, t=90),
        )
        chart = {
            "title": "3D Surface",
            "static": fig3ss,
            "interactive": fig3is,
            "name": "3D Surface",
        }
        self.charts.append(chart)

    def threeDScatter(self, df: pd.DataFrame) -> None:
        # 1. 3D Scatter
        fig_s1 = plt.figure(figsize=(6, 4))
        ax = fig_s1.add_subplot(111, projection="3d")
        ax.scatter(df["X"], df["Y"], df["Z"], c=df["Z"], cmap="viridis")
        ax.set_title("Static 3D Scatter Plot")

        fig_i1 = px.scatter_3d(
            df, x="X", y="Y", z="Z", color="Z", title="Interactive 3D Scatter"
        )
        chart = {
            "title": "3D Scatter Cluster",
            "static": fig_s1,
            "interactive": fig_i1,
            "name": "3D Scatter",
        }
        self.charts.append(chart)
