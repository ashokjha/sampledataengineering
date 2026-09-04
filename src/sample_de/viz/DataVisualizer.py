from abc import ABC, abstractmethod
import pandas as pd

class DataVisualizer(ABC):
    """Base interface to  Visualize data
    """
    @abstractmethod
    def visualize(self, data: pd.DataFrame) -> None:
        """Visualize Data
        Args:
            data(pd.DataFrame): 

        Returns:
            None:
        """
        pass
