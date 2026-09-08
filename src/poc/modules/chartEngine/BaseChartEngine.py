from abc import ABC, abstractmethod


class BaseChartEngine(ABC):
    """
    Base chart Engine
    """

    @abstractmethod
    def render_all(self) -> list[dict]:
        """
        To abstract method to implement charts

        Returns:
            list[dict]: List of charts
        """
        pass
