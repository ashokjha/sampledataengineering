import pandas as pd
import os
from dotenv import load_dotenv
from typing import Final
from poc.utils.data.GenerateData import generate_data


class GeoDataAdapter:
    load_dotenv()
    DATA_PATH: Final = os.environ.get("POCSAMPLEDATA", "data/tmp") + "/Geo"
    os.makedirs(f"{DATA_PATH}/Geo", exist_ok=True)

    def choroplethData() -> pd.DataFrame:
        # Choropleth Data
        cpdf = pd.read_csv("data/world_economic_data.csv")
        return cpdf

    def scatterData():
        scatterDf = pd.DataFrame(
            {
                "City": [
                    "New York",
                    "Los Angeles",
                    "Chicago",
                    "Houston",
                    "Phoenix",
                    "Kolkata",
                    "Bela",
                    "New Delhi",
                ],
                "Lat": [
                    40.7128,
                    34.0522,
                    41.8781,
                    29.7604,
                    33.4484,
                    22.56263,
                    26.5907,
                    28.6139,
                ],
                "Lon": [
                    -74.0060,
                    -118.2437,
                    -87.6298,
                    -95.3698,
                    -112.0740,
                    88.36304,
                    86.15765,
                    77.2089,
                ],
                "Population_Scale": [83, 39, 27, 23, 16, 78, 0.0089, 99],
            }
        )

        scatterDf.to_csv(
            f"{GeoDataAdapter.DATA_PATH}/Geo_Scatter_data.csv",
            index=False,
        )

        return scatterDf

    def connectionData():
        # Connection Map Data
        origcmdata = pd.read_csv("data/world_country_data.csv")
        origin_country = "United States"
        filtered_data = origcmdata[origcmdata["Country"] != origin_country]
        datdct = {
            "Origin_Country": origin_country,
            "Origin_Lat": origcmdata.iat[0, 4],
            "Origin_Lon": origcmdata.iat[0, 5],
            "Dest_Country": filtered_data["Country"],
            "Dest_Lat": filtered_data["Latitude"],
            "Dest_Lon": filtered_data["Longitude"],
            "Population": filtered_data["Population"],
            "Per_Capita_Income_USD": filtered_data["Per_Capita_Income_USD"],
            "Economy_GDP_USD_Trillion": filtered_data["Economy_GDP_USD_Trillion"],
        }
        conmapdf = pd.DataFrame(datdct).reset_index(drop=True)

        conmapdf.to_csv(
            f"{GeoDataAdapter.DATA_PATH}/geoConnectionMapData.csv",
            index=False,
        )
        return conmapdf
