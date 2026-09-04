from abc import ABC, abstractmethod
import pandas as pd

# ==========================================
# 1. Base Interface to create Data
#    ABC=> AbstractBaseClass
# ==========================================
class BaseDataCleaner(ABC):
    """Base interface to clean data
    """
    @abstractmethod
    def clean_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """To clean data
        Args:
            dataFrame: Panda DataFrame

        Returns:
            data: panda DataFrame
        """
        pass