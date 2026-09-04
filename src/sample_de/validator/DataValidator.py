from abc import ABC, abstractmethod
import pandas as pd

class DataValidator(ABC):
    """Base interface to  validate data
    """
    @abstractmethod
    def validate(self, data: pd.DataFrame) -> bool:
        """validate Data
        Args:
            data(pd.DataFrame): 

        Returns:
            True/False:
        """
        pass