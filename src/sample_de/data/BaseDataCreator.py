from abc import ABC, abstractmethod
import pandas as pd

# ==========================================
# 1. Base Interface to create Data
#    ABC=> AbstractBaseClass
# ==========================================
class BaseDataCreator(ABC):
    """Base interface to create data
    """
    @abstractmethod
    def create(self, path: str) -> pd.DataFrame:
        """To Read or create Data
        Args:
            path (str): Data Path

        Returns:
           Dataframe: dataframe
        """
        pass