import pandas as pd
import numpy as np


class ThreeDAdapter:
    # 1. 3D Scatter Plot
    @staticmethod
    def threeDdata() -> pd.DataFrame:
        """
        3D Scatter Plot

        Returns:
            pd.DataFrame: _description_
        """
        np.random.seed(5)
        df = pd.DataFrame(
            {
                "X": np.random.normal(0, 1, 100),
                "Y": np.random.normal(0, 1, 100),
                "Z": np.random.normal(0, 1, 100),
            }
        )
        return df

    # 2. 3D Surface Data
    @staticmethod
    def surfaceData() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        3D Surface Data

        Returns:
            tuple[np.ndarray, np.ndarray, np.ndarray]: _description_
        """
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        surface = np.sin(np.sqrt(X**2 + Y**2))
        return X, Y, surface

    # 3. 3D Parallel Coordinates Data
    @staticmethod
    def parallelCordinates() -> tuple[pd.DataFrame]:
        """
        3D Parallel Coordinates Data

        Returns:
            tuple[pd.DataFrame]: _description_
        """
        data = {
            "Car_Model": ["Model A", "Model B", "Model C", "Model D", "Model E"],
            "Price_USD": [22000, 45000, 35000, 60000, 18000],
            "Horsepower": [140, 350, 180, 400, 120],
            "Fuel_Efficiency_MPG": [35, 18, 28, 15, 38],
            "Safety_Rating": [4, 5, 4, 5, 3],
            "Category": ["Economy", "Sports", "Sedan", "Luxury", "Economy"],
        }
        pcData = pd.DataFrame(data)
        category_mapping = {"Economy": 0, "Sedan": 1, "Sports": 2, "Luxury": 3}
        pcData["Category_ID"] = pcData["Category"].map(category_mapping)
        return pcData

    # 4. 3D Word cloud Data
    @staticmethod
    def worldCloud() -> dict:
        """
        3D word Cloud

        Returns:
            dict: word with frquency dictionaty
        """
        wordDict = [
            ("Python", 100),
            ("Data", 85),
            ("Science", 80),
            ("3D", 75),
            ("Cloud", 70),
            ("Interactive", 65),
            ("Static", 60),
            ("Matplotlib", 55),
            ("Plotly", 50),
            ("Visualization", 48),
            ("Code", 45),
            ("AI", 42),
            ("Machine", 40),
            ("Learning", 40),
            ("Algorithm", 35),
            ("Array", 30),
            ("Matrix", 25),
        ]
        return wordDict
