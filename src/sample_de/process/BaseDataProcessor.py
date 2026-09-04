from abc import ABC, abstractmethod
import pandas as pd

# ==========================================
# 1. Base Interface to create Data
#    ABC=> AbstractBaseClass
# ==========================================
class BaseDataProcessor(ABC):
    """Base interface to process data
    """
    @abstractmethod
    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        """To process Data
        Args:
            data(pd.DataFrame): 

        Returns:
            processedData(pd.DataFrame):
        """
        pass