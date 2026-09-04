import pandas as pd
from sample_de.process.BaseDataProcessor import BaseDataProcessor
from sample_de.utils.systemvariable import systemvariablemanager
from sample_de.db.persist_in_csv import persist_in_csv

class StockDataProcessor(BaseDataProcessor):
    """
    Stock Data Processor
    """
    def __init__(self):
        super().__init__()
        self.envreader = systemvariablemanager()
    
    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        """To process Data
        Args:
            data(pd.DataFrame): 

        Returns:
            processedData(pd.DataFrame):
        """
        persistInCSV=persist_in_csv()
        persistInCSV.persist(data, self.envreader.get_env("CLEANED_STOCK_DATASET"))        
        return data
        
if __name__ == "__main__" :
    from sample_de.data.StockDataCreator import StockDataCreator
    from sample_de.clean.StockDataCleaner import StockDataCleaner
    
    stockDataCreator = StockDataCreator()
    data = stockDataCreator.create_data('data/sampleStock.csv')
    stockDataCleaner = StockDataCleaner()
    print(stockDataCleaner.clean_data(data), end="\n")
    sdp = StockDataProcessor()
    sdp.process(data)
    
     