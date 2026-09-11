import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import numpy as np


from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc import DataConfigEngine


class GeospatialEngine(BaseChartEngine):
    """<b>Geospatial (Map) Charts</b>:
    Best libraries: <b>Geopandas</b>, <b>Folium</b>, or <b>Plotly Express</b>

    <ul><b>Choropleth Map:</b> Color-codes geographical regions based on a specific data variable.</ul>
    <ul><b>Scatter Map / Dot Map:</b> Places coordinate-based data points directly onto a geographic map.</ul>
    <ul><b>Connection Map:</b> Draws lines between geographical nodes to show routes or shipping paths.</ul>
    """

    def __init__(self):
        super().__init__()
        self.charts = []
        self.dce = DataConfigEngine()
        self.df = self.dce.fetchData("Geo-spatial")

    def render_all(self) -> list[dict]:
        self.scatter_map_or_geo_plot()
        return self.charts

    def scatter_map_or_geo_plot(self) -> None:
        """
        Scatter Map / Geo-Plot
        """
        fig_s1, ax = plt.subplots(figsize=(6, 4))
        ax.scatter(
            self.df["Lon"],
            self.df["Lat"],
            s=self.df["Population_Scale"] * 5,
            color="crimson",
            alpha=0.7,
        )
        for i, txt in enumerate(self.df["City"]):
            ax.annotate(txt, (self.df["Lon"][i] + 1, self.df["Lat"][i]))
        ax.set_title("Static Coordinate Plot (Longitude vs Latitude)")
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")

        # Interactive Plotly OpenStreetMap Mapbox Scatter
        fig_i1 = px.scatter_geo(
            self.df,
            lat="Lat",
            lon="Lon",
            text="City",
            size="Population_Scale",
            title="Interactive Geospatial Bubble Map",
            projection="natural earth",
        )
        self.charts.append(
            {
                "title": "Geospatial Dot Map",
                "static": fig_s1,
                "interactive": fig_i1,
                "name": "Scatter Map or Geo-Plot",
            }
        )
