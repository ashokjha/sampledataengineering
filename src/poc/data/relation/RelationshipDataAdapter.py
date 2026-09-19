import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from typing import Final


class RelationshipDataAdapter:
    load_dotenv()
    DATA_PATH: Final = os.environ.get("POCSAMPLEDATA", "data/tmp") + "/Relational"
    os.makedirs(DATA_PATH, exist_ok=True)

    @staticmethod
    def lineChartData() -> pd.DataFrame:
        # Line Chart
        np.random.seed(10)
        dates = pd.date_range(start="2026-01-01", periods=60)
        lcdf = pd.DataFrame(
            {
                "Date": dates,
                "Metric_A": np.cumsum(np.random.normal(loc=0.5, scale=2, size=60)) + 50,
                "Metric_B": np.cumsum(np.random.normal(loc=0.3, scale=1.5, size=60))
                + 30,
            }
        )
        lcdf.to_csv(
            f"{RelationshipDataAdapter.DATA_PATH}/linechart.csv",
            index=False,
        )
        return lcdf

    @staticmethod
    def scatterData() -> pd.DataFrame:
        # Scatter plot Data
        np.random.seed(10)
        dates = pd.date_range(start="2026-01-01", periods=60)
        scdf = pd.DataFrame(
            {
                "Date": dates,
                "Metric_A": np.cumsum(np.random.normal(loc=0.5, scale=2, size=60)) + 50,
                "Metric_B": np.cumsum(np.random.normal(loc=0.3, scale=1.5, size=60))
                + 30,
            }
        )

        scdf.to_csv(
            f"{RelationshipDataAdapter.DATA_PATH}/scatterData.csv",
            index=False,
        )

        return scdf

    @staticmethod
    def bubbleChartData() -> pd.DataFrame:
        # Bubble Data
        data = {
            "Quarter": [
                "Q1",
                "Q1",
                "Q1",
                "Q1",
                "Q2",
                "Q2",
                "Q2",
                "Q2",
                "Q3",
                "Q3",
                "Q3",
                "Q3",
                "Q4",
                "Q4",
                "Q4",
                "Q4",
            ],
            "Project_Name": ["Alpha", "Beta", "Gamma", "Delta"] * 4,
            "Marketing_Spend": [
                10000,
                25000,
                15000,
                40000,
                12000,
                28000,
                18000,
                42000,
                15000,
                35000,
                22000,
                48000,
                20000,
                45000,
                30000,
                55000,
            ],
            "Revenue": [
                15000,
                48000,
                12000,
                90000,
                22000,
                60000,
                25000,
                105000,
                35000,
                85000,
                45000,
                130000,
                55000,
                120000,
                70000,
                180000,
            ],
            "Team_Size": [3, 8, 4, 12, 4, 9, 5, 14, 5, 12, 6, 15, 6, 15, 8, 18],
            "Status": [
                "Planning",
                "In Progress",
                "Planning",
                "In Progress",
                "In Progress",
                "In Progress",
                "In Progress",
                "In Progress",
                "In Progress",
                "Completed",
                "In Progress",
                "Completed",
                "Completed",
                "Completed",
                "Completed",
                "Completed",
            ],
        }

        bubbleData = pd.DataFrame(data)

        bubbleData.to_csv(
            f"{RelationshipDataAdapter.DATA_PATH}/bubbleChartData.csv",
            index=False,
        )

        return bubbleData

    @staticmethod
    def connScatterData() -> pd.DataFrame:
        # Connected Scatter Plot Data
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
        metric_values = [12, 19, 15, 28, 24, 35, 31, 47, 42, 55]

        connscdf = pd.DataFrame({"Month": months, "Growth_Metric": metric_values})
        connscdf.to_csv(
            f"{RelationshipDataAdapter.DATA_PATH}/connectionScatterData.csv",
            index=False,
        )

        return connscdf

    @staticmethod
    def areaChartData() -> pd.DataFrame:
        # Area Chart Data
        data = {
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Visitors": [1200, 1500, 1100, 1800, 2400, 2100, 1900],
        }
        acdf = pd.DataFrame(data)

        acdf.to_csv(
            f"{RelationshipDataAdapter.DATA_PATH}/areaChartData.csv",
            index=False,
        )

        return acdf

    @staticmethod
    def stackedAreaData() -> pd.DataFrame:
        # Stacked Area chart Data
        data = {
            "Quarter": [
                "2024 Q1",
                "2024 Q2",
                "2024 Q3",
                "2024 Q4",
                "2025 Q1",
                "2025 Q2",
                "2025 Q3",
                "2025 Q4",
                "2026 Q1",
                "2026 Q2",
                "2026 Q3",
                "2026 Q4",
            ],
            "Hardware": [30, 35, 28, 45, 32, 40, 35, 55, 38, 42, 39, 65],
            "Software": [20, 25, 30, 38, 35, 42, 48, 58, 55, 62, 70, 85],
            "Services": [15, 18, 22, 25, 24, 28, 32, 36, 35, 40, 45, 50],
        }

        stackedAreadf = pd.DataFrame(data)

        stackedAreadf.to_csv(
            f"{RelationshipDataAdapter.DATA_PATH}/stackedAreaData.csv",
            index=False,
        )

        return stackedAreadf
