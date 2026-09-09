import pandas as pd
import numpy as np


class DataCreator:

    @staticmethod
    def distributionData() -> pd.DataFrame:
        """
          Create Sample Distribution Data
        Returns:
            pd.DataFrama: _description_
        """
        np.random.seed(42)
        data = {
            "Value": np.random.normal(loc=50, scale=10, size=500),
            "Category": np.random.choice(["Group A", "Group B", "Group C"], size=500),
        }
        return pd.DataFrame(data)

    @staticmethod
    def threeDdata() -> pd.DataFrame:
        np.random.seed(5)
        df = pd.DataFrame(
            {
                "X": np.random.normal(0, 1, 100),
                "Y": np.random.normal(0, 1, 100),
                "Z": np.random.normal(0, 1, 100),
            }
        )
        return df

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
    def spatialData() -> pd.DataFrame:
        df = pd.DataFrame(
            {
                "City": [
                    "New York",
                    "Los Angeles",
                    "Chicago",
                    "Houston",
                    "Phoenix",
                    "Kolkata",
                    "New Delhi",
                ],
                "Lat": [40.7128, 34.0522, 41.8781, 29.7604, 33.4484, 22.56263, 28.6139],
                "Lon": [
                    -74.0060,
                    -118.2437,
                    -87.6298,
                    -95.3698,
                    -112.0740,
                    88.36304,
                    77.2089,
                ],
                "Population_Scale": [83, 39, 27, 23, 16, 78, 99],
            }
        )
        return df

    @staticmethod
    def matrixAndRelationData() -> tuple[pd.DataFrame, pd.DataFrame]:
        np.random.seed(42)
        # Create a correlation-like matrix dataset
        data = np.random.rand(5, 5)
        cols = ["Feature A", "Feature B", "Feature C", "Feature D", "Feature E"]
        df_matrix = pd.DataFrame(data, columns=cols, index=cols)

        # Long-form data for flow/relationship visualizations
        df_flow = pd.DataFrame(
            {
                "Source": ["A", "A", "B", "B", "C"],
                "Target": ["X", "Y", "X", "Z", "Y"],
                "Value": [10, 20, 15, 5, 25],
            }
        )
        return df_matrix, df_flow

    @staticmethod
    def categoricalData() -> tuple[pd.DataFrame, pd.DataFrame]:
        df = pd.DataFrame(
            {
                "Quarter": ["Q", "Q", "Q", "Q"] * 2,
                "Product": [
                    "Software",
                    "Software",
                    "Software",
                    "Software",
                    "Hardware",
                    "Hardware",
                    "Hardware",
                    "Hardware",
                ],
                "Sales": [40, 55, 30, 75, 25, 35, 45, 50],
            }
        )

        # Radar Char
        radar_df = pd.DataFrame(
            {
                "Metric": ["Speed", "Reliability", "Design", "Support", "Price"],
                "Score": [85, 90, 70, 80, 65],
            }
        )
        return df, radar_df
