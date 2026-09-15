import pandas as pd
import numpy as np
import logging

logger = logging.getLogger("DataAdapter")


class DataAdapter:

    @staticmethod
    def relationalData() -> pd.DataFrame:
        np.random.seed(10)
        dates = pd.date_range(start="2026-01-01", periods=60)
        df = pd.DataFrame(
            {
                "Date": dates,
                "Metric_A": np.cumsum(np.random.normal(loc=0.5, scale=2, size=60)) + 50,
                "Metric_B": np.cumsum(np.random.normal(loc=0.3, scale=1.5, size=60))
                + 30,
            }
        )
        return df

    @staticmethod
    def spatialData() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        """Spacial Data

        Returns:
            tuple[pd.DataFrame,pd.DataFrame]: _description_
        """
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
        # Choropleth Data
        cpdf = pd.read_csv("data/world_economic_data.csv")

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

        return scatterDf, cpdf, conmapdf

    @staticmethod
    def categoricalData() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
        df = pd.DataFrame(
            {
                "Quarter": ["Q1", "Q2", "Q3", "Q4"] * 2,
                "Product": ["Software", "Hardware"] * 4,
                "Sales": [40, 55, 30, 75, 25, 35, 45, 50],
            }
        )

        # Grouped Data
        groupedData = pd.DataFrame(
            {
                "Quarter": [
                    "Q1",
                    "Q1",
                    "Q1",
                    "Q2",
                    "Q2",
                    "Q2",
                    "Q3",
                    "Q3",
                    "Q3",
                    "Q4",
                    "Q4",
                    "Q4",
                ],
                "Product": ["Marketig", "Development", "Sales"] * 4,
                "Sales": [12, 9, 5, 10, 7, 6, 15, 10, 6, 9, 4, 30],
            }
        )

        # Radar Char
        radar_df = pd.DataFrame(
            {
                "Metric": ["Speed", "Reliability", "Design", "Support", "Price"],
                "Score": [85, 90, 70, 80, 65],
            }
        )
        return df, groupedData, radar_df


if __name__ == "__main__":
    df = DataAdapter.parallelCordinates()
