import os
from dotenv import load_dotenv
import pandas as pd
import numpy as np
from typing import Final
from poc.utils.data.GenerateData import generate_data


class DistributionAdapter:
    load_dotenv()
    DATA_PATH: Final = os.environ.get("POCSAMPLEDATA", "data/tmp") + "/Distribution"
    os.makedirs(DATA_PATH, exist_ok=True)

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
            "Category": np.random.choice(["Sky", "Surface", "Blackwhole"], size=500),
        }

        distributiondf = pd.DataFrame(data)

        distributiondf.to_csv(
            f"{DistributionAdapter.DATA_PATH}/distributiondata.csv",
            index=False,
        )

        return pd.DataFrame(data)
