import pandas as pd
import os
from dotenv import load_dotenv
from typing import Final


class Part2WholeDataAdapter:
    load_dotenv()
    DATA_PATH: Final = os.environ.get("POCSAMPLEDATA", "data/tmp") + "/P2W"
    os.makedirs(DATA_PATH, exist_ok=True)

    @staticmethod
    def pieChartData() -> pd.DataFrame:
        data = {
            "Brand": ["Tata", "Mahindra", "MG Motor", "BYD", "Hyundai", "Others"],
            "Market_Share": [65, 12, 10, 5, 5, 3],  # in %
        }
        pie_df = pd.DataFrame(data)
        pie_df.to_csv(
            f"{Part2WholeDataAdapter.DATA_PATH}/PieData.csv",
            index=False,
        )
        return pie_df

    @staticmethod
    def donutData() -> pd.DataFrame:
        donutdf = pd.DataFrame(
            {
                "Labels": ["Tech Support", "Marketing", "Sales", "R&D", "HR"],
                "Values": [25, 15, 30, 20, 10],
            }
        )
        donutdf.to_csv(
            f"{Part2WholeDataAdapter.DATA_PATH}/donudata.csv",
            index=False,
        )
        return donutdf

    @staticmethod
    def treemapData() -> pd.DataFrame:
        treemapdf = pd.DataFrame(
            {
                "Labels": ["Tech Support", "Marketing", "Sales", "R&D", "HR"],
                "Values": [25, 15, 30, 20, 10],
            }
        )

        treemapdf.to_csv(
            f"{Part2WholeDataAdapter.DATA_PATH}/treemap.csv",
            index=False,
        )

        return treemapdf

    @staticmethod
    def sunburstData() -> pd.DataFrame:
        sunburstdata = {
            "Department": [
                "Electronics",
                "Electronics",
                "Electronics",
                "Clothing",
                "Clothing",
                "Home",
                "Home",
            ],
            "Category": [
                "Smartphones",
                "Smartphones",
                "Laptops",
                "Apparel",
                "Apparel",
                "Kitchen",
                "Furniture",
            ],
            "Region": ["North", "South", "North", "North", "East", "West", "South"],
            "Sales": [50000, 35000, 75000, 30000, 45000, 20000, 25000],
        }
        sunburstdf = pd.DataFrame(sunburstdata)

        sunburstdf.to_csv(
            f"{Part2WholeDataAdapter.DATA_PATH}/sunburstdata.csv",
            index=False,
        )
        return sunburstdf
