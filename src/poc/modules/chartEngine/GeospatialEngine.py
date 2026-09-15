import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import pandas as pd
import numpy as np


from poc.modules.chartEngine.BaseChartEngine import BaseChartEngine
from poc import DataConfigEngine


class GeospatialEngine(BaseChartEngine):
    """<b>Geospatial (Map) Charts</b>:
    Best libraries: <b>Geopandas</b>, <b>Folium</b>, or <b>Plotly Express</b>
    <OL>
    <li><b>Choropleth Map:</b> Color-codes geographical regions based on a specific data variable.</li>
    <li><b>Scatter Map / Dot Map:</b> Places coordinate-based data points directly onto a geographic map.</li>
    <li><b>Connection Map:</b> Draws lines between geographical nodes to show routes or shipping paths.</li>
    </OL>
    """

    def __init__(self):
        super().__init__()
        self.charts = []
        self.dce = DataConfigEngine()
        self.scattdf, self.chpledf, self.conmapdf = self.dce.fetchData("Geo-spatial")

    def render_all(self) -> list[dict]:
        self.choropleth_map(self.chpledf)
        self.scatter_map_or_geo_plot(self.scattdf)
        self.connectionMap(self.conmapdf)
        return self.charts

    def choropleth_map(self, chpdf: pd.DataFrame) -> None:
        """
        1. Choropleth Map
        """
        # fig_static, ax = plt.subplots(figsize=(8, 5))
        fig = px.choropleth(
            chpdf,
            locations="Country",
            locationmode="country names",
            color="Per_Capita_Income_USD",
            hover_name="Country",
            hover_data={
                "Per_Capita_Income_USD": ":$,.0f",
                "Economy_GDP_USD_Trillion": ":$.2f T",
                "Population": ":,.0f",
                "Country": False,
            },
            color_continuous_scale="Viridis",
            labels={
                "Per_Capita_Income_USD": "Per Capita Income (USD)",
                "Economy_GDP_USD_Trillion": "GDP (Trillion USD)",
                "Population": "Total Population",
            },
            title="<b>Global Interactive Map: Economic & Population Overview</b>",
        )

        fig.update_layout(
            title_font_size=20,
            title_x=0.5,
            margin={"r": 0, "t": 60, "l": 0, "b": 0},
            geo=dict(
                showframe=False,
                showcoastlines=True,
                projection_type="equirectangular",  #  "orthographic/equirectangular"
            ),
        )
        self.charts.append(
            {
                "title": "Global Interactive Map: Economic & Population Overview",
                "static": None,
                "interactive": fig,
                "name": "Scatter Map or Geo-Plot",
            }
        )

    def scatter_map_or_geo_plot(self, scattdf: pd.DataFrame) -> None:
        """
        2. Scatter Map / Geo-Plot
        """
        fig_s1, ax = plt.subplots(figsize=(6, 4))
        ax.scatter(
            scattdf["Lon"],
            scattdf["Lat"],
            s=scattdf["Population_Scale"] * 5,
            color="crimson",
            alpha=0.7,
        )
        for i, txt in enumerate(self.scattdf["City"]):
            ax.annotate(txt, (scattdf["Lon"][i] + 1, scattdf["Lat"][i]))
        ax.set_title("Static Coordinate Plot (Longitude vs Latitude)")
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")

        # Interactive Plotly OpenStreetMap Mapbox Scatter
        fig_i1 = px.scatter_geo(
            scattdf,
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

    def connectionMap(self, connectionMapDf: pd.DataFrame) -> None:
        """
        3. <b>Connection Map</b>
        """
        fig = go.Figure()
        for i in range(len(connectionMapDf)):
            fig.add_trace(
                go.Scattergeo(
                    locationmode="country names",
                    lon=[
                        connectionMapDf["Origin_Lon"][i],
                        connectionMapDf["Dest_Lon"][i],
                    ],
                    lat=[
                        connectionMapDf["Origin_Lat"][i],
                        connectionMapDf["Dest_Lat"][i],
                    ],
                    mode="lines",
                    line=dict(width=2, color="red"),
                    opacity=0.6,
                    hoverinfo="skip",
                )
            )

        fig.add_trace(
            go.Scattergeo(
                locationmode="country names",
                lon=connectionMapDf["Dest_Lon"],
                lat=connectionMapDf["Dest_Lat"],
                hovertext=connectionMapDf["Dest_Country"],
                mode="markers",
                marker=dict(
                    size=10,
                    color="blue",
                    line=dict(width=1, color="rgba(102, 102, 102)"),
                ),
                customdata=connectionMapDf[
                    ["Population", "Per_Capita_Income_USD", "Economy_GDP_USD_Trillion"]
                ],
                hovertemplate=(
                    "<b>%{hovertext}</b><br><br>"
                    + "Population: %{customdata[0]:,.0f}<br>"
                    + "Per Capita Income: $%{customdata[1]:,.0f}<br>"
                    + "GDP: $%{customdata[2]:.2f} T<br>"
                    + "<extra></extra>"
                ),
            )
        )

        fig.update_layout(
            title_text="<b>Global Interactive Connection Map with Economic Data</b>",
            title_x=0.5,
            showlegend=False,
            geo=dict(
                scope="world",
                projection_type="equirectangular",
                showland=True,
                landcolor="rgb(243, 243, 243)",
                countrycolor="rgb(204, 204, 204)",
            ),
            margin={"r": 0, "t": 50, "l": 0, "b": 0},
        )

        self.charts.append(
            {
                "title": "Global Interactive Connection Map with Economic Data",
                "static": None,
                "interactive": fig,
                "name": "Global Interactive Connection Map with Economic Data",
            }
        )
