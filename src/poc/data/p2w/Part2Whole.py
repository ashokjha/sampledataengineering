import pandas as pd


class Part2Whole:
    @staticmethod
    def pieChartData() -> pd.DataFrame:
        data = {
            "Brand": ["Tata", "Mahindra", "MG Motor", "BYD", "Hyundai", "Others"],
            "Market_Share": [65, 12, 10, 5, 5, 3],  # प्रतिशत (%) में
        }

        pie_df = pd.DataFrame(data)
        return pie_df

    @staticmethod
    def donutData() -> pd.DataFrame:
        df = pd.DataFrame(
            {
                "Labels": ["Tech Support", "Marketing", "Sales", "R&D", "HR"],
                "Values": [25, 15, 30, 20, 10],
            }
        )
        return df

    @staticmethod
    def treemapData() -> pd.DataFrame:
        df = pd.DataFrame(
            {
                "Labels": ["Tech Support", "Marketing", "Sales", "R&D", "HR"],
                "Values": [25, 15, 30, 20, 10],
            }
        )
        return df

    @staticmethod
    def sunburstData() -> pd.DataFrame:
        data = {
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

        df_sales = pd.DataFrame(data)
        return df_sales
