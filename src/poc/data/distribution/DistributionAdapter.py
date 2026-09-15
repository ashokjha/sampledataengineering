import pandas as pd
import numpy as np


class DistributionAdapter:
    ## Distribution Data
    @staticmethod
    def distributionData() -> pd.DataFrame:
        """
          Create Sample Distribution Data
        Returns:
            pd.DataFrama: Distribution Data Set
        """
        np.random.seed(42)
        data = {
            "Value": np.random.normal(loc=50, scale=10, size=500),
            "Category": np.random.choice(["Group A", "Group B", "Group C"], size=500),
        }
        return pd.DataFrame(data)
