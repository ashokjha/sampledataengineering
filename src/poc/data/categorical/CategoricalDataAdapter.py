import os
from dotenv import load_dotenv
from typing import Final
import pandas as pd

from poc.utils.data.GenerateData import generate_data


class CategoricalDataAdapter:
    load_dotenv()
    DATA_PATH: Final = os.environ.get("POCSAMPLEDATA", "data/tmp") + "/Categorical"
    os.makedirs(DATA_PATH, exist_ok=True)

    @staticmethod
    def verticalbarData() -> pd.DataFrame:
        columns = {
            "Quarter": ["Q1", "Q2", "Q3", "Q4"] * 2,
            "Product": ["Software", "Hardware"] * 4,
            "ROI": [40, 55, 30, 75, 25, 35, 45, 50],
        }
        verticaldf = generate_data(20, columns)

        verticaldf.to_csv(
            f"{CategoricalDataAdapter.DATA_PATH}/verticalbar.csv",
            index=False,
        )

        return verticaldf

    @staticmethod
    def horizontalbarData() -> pd.DataFrame:
        columns = {
            "Quarter": ["Q1", "Q2", "Q3", "Q4"] * 2,
            "Product": ["Software", "Hardware"] * 4,
            "Sales": [40, 55, 30, 75, 25, 35, 45, 50],
        }
        horizontaldf = generate_data(20, columns)

        horizontaldf.to_csv(f"{CategoricalDataAdapter.DATA_PATH}/horizontal.csv")
        return horizontaldf

    @staticmethod
    def stackedbarData() -> pd.DataFrame:
        # Grouped Data
        columns = {
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
        stackeddf = generate_data(20, columns)

        stackeddf.to_csv(f"{CategoricalDataAdapter.DATA_PATH}/stackedbar.csv")
        return stackeddf

    @staticmethod
    def groupedbarData() -> pd.DataFrame:
        # Grouped Data
        columns = {
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
        groupedDf = generate_data(12, columns)

        groupedDf.to_csv(f"{CategoricalDataAdapter.DATA_PATH}/grouped.csv")
        return groupedDf

    @staticmethod
    def lollipopData() -> pd.DataFrame:
        columns = {
            "Category": [
                "Electronics",
                "Home & Kitchen",
                "Apparel",
                "Books",
                "Beauty",
                "Sports",
            ],
            "Sales": [145, 120, 95, 80, 65, 40],
        }

        # lollipopdf = pd.DataFrame(data)
        lollipopdf = generate_data(6, columns)

        # Sorting ascending makes horizontal lollipop charts look best from top to bottom
        lollipopdf = lollipopdf.sort_values(by="Sales", ascending=True)
        # os.makedirs(f"{CategoricalDataAdapter.DATA_PATH}/Horizontal", exist_ok=True)
        lollipopdf.to_csv(f"{CategoricalDataAdapter.DATA_PATH}/LollipopData.csv")
        return lollipopdf

    @staticmethod
    def radarData() -> pd.DataFrame:
        columns = {
            "Metric": ["Speed", "Reliability", "Design", "Support", "Price"],
            "Score": [85, 90, 70, 80, 65],
        }
        radar_df = generate_data(5, columns)
        radar_df.to_csv(f"{CategoricalDataAdapter.DATA_PATH}/radarData.csv")
        return radar_df


if __name__ == "__main__":
    columns = {
        "Quarter": ["Q1", "Q2", "Q3", "Q4"] * 2,
        "Product": ["Software", "Hardware"] * 4,
        "ROI": [40, 55, 30, 75, 25, 35, 45, 50],
    }
    verticaldf = generate_data(20, columns)
    print(verticaldf)
