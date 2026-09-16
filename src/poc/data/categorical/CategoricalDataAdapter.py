import pandas as pd


class CategoricalDataAdapter:
    @staticmethod
    def verticalbarData() -> pd.DataFrame:
        verticaldf = pd.DataFrame(
            {
                "Quarter": ["Q1", "Q2", "Q3", "Q4"] * 2,
                "Product": ["Software", "Hardware"] * 4,
                "Sales": [40, 55, 30, 75, 25, 35, 45, 50],
            }
        )
        return verticaldf

    @staticmethod
    def horizontalbarData() -> pd.DataFrame:
        horizontaldf = pd.DataFrame(
            {
                "Quarter": ["Q1", "Q2", "Q3", "Q4"] * 2,
                "Product": ["Software", "Hardware"] * 4,
                "Sales": [40, 55, 30, 75, 25, 35, 45, 50],
            }
        )
        return horizontaldf

    @staticmethod
    def stackedbarData() -> pd.DataFrame:
        # Grouped Data
        stackeddf = pd.DataFrame(
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
        return stackeddf

    @staticmethod
    def groupedbarData() -> pd.DataFrame:
        # Grouped Data
        groupedDf = pd.DataFrame(
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
        return groupedDf

    @staticmethod
    def lollipopData() -> pd.DataFrame:
        data = {
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

        lollipopdf = pd.DataFrame(data)
        # Sorting ascending makes horizontal lollipop charts look best from top to bottom
        lollipopdf = lollipopdf.sort_values(by="Sales", ascending=True)
        return lollipopdf

    @staticmethod
    def radarData() -> pd.DataFrame:
        radar_df = pd.DataFrame(
            {
                "Metric": ["Speed", "Reliability", "Design", "Support", "Price"],
                "Score": [85, 90, 70, 80, 65],
            }
        )
        return radar_df
