import logging
import pandas as pd

from sample_de.viz.DataVisualizer import DataVisualizer
from sample_de.utils.systemvariable import systemvariablemanager
from sample_de.utils.common_util import common_util
from sample_de.utils.translation import TranslationManager


class StockDataVisualizer(DataVisualizer):
    """Salesdatavisual creator

    Args:
        DataVisualizer (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.envreader = systemvariablemanager()
        self.langLocal = common_util.getLangLocal()
        self.reportTheme = self.envreader.environ.get("REPORT_THEME", "whitegrid")
        self.palette = self.envreader.environ.get("PALETTE","")
        self.translation = TranslationManager()
        self.chartsPath = common_util.getChartPath()        
    
    def visualize(self, data: pd.DataFrame) -> None:
        """Visualize Data
        Args:
            data(pd.DataFrame): 

        Returns:
            None:
        """
        pass
    
    def monthlySalesTrendAndPriceDist(self, data: pd.DataFrame ) -> None:
        """ Create visual for
        <li><b>Line Chart</b> - Monthly Sales Trend by Subcategory
        <li><b>Box Plot</b > - Price Distribution across Category & Subcategory</li>

        Args:
            data (pd.DataFrame): DataFrame
        """
        pass
    
    
    def monthlySalesTrendAndPriceDist(self, data: pd.DataFrame ) -> None:
        pass
        
    
if __name__ == "__main__" :
    # below import required in main only
    from sample_de.data.SalesDataCreator import SalesDataCreator
    from sample_de.clean.SalesDataCleaner import SalesDataCleaner
    from sample_de.process.SalesDataProcessor import SalesDataProcessor
     
    salesDataCreator = SalesDataCreator()
    data = salesDataCreator.create_data('data/sample_Stock_remove.csv')
    sdc = SalesDataCleaner()
    sdc.clean_data(data)
    sdp = SalesDataProcessor()
    sdp.process(data)        
        
