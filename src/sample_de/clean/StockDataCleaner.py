import pandas as pd

from sample_de.clean.BaseDataCleaner import BaseDataCleaner

class StockDataCleaner(BaseDataCleaner):
    """
    Stock Data cleaner
    """
    def __init__(self):
        super().__init__()
    
    def clean_data(self, data: pd.DataFrame) -> pd.DataFrame:
        """To clean data
        Args:
            dataFrame: Panda DataFrame

        Returns:
            data: panda DataFrame
        """
        #TODO
        return data
        
if __name__ == "__main__" :
    from sample_de.data.StockDataCreator import StockDataCreator
    stockDataCreator = StockDataCreator()
    data = stockDataCreator.create_data('data/sampleStock.csv')
    stockDataCleaner = StockDataCleaner()
    print(stockDataCleaner.clean_data(data), end="\n")
    
     