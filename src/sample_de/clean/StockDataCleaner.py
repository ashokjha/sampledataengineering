import pandas as pd

from sample_de.clean.BaseDataCleaner import BaseDataCleaner

class StockDataCleaner(BaseDataCleaner):
    """
    Stock Data cleaner
    """
    def __init__(self):
        super().__init__()
    
    def clean(self, data: pd.DataFrame) -> pd.DataFrame:
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
    from sample_de.validator.StockDataValidator import StockDataValidator
    stockDataCreator = StockDataCreator()
    data = stockDataCreator.create('data/sampleStock.csv')
    sdvalidator = StockDataValidator()
    sdvalidator.validate(data)
    stockDataCleaner = StockDataCleaner()
    print(stockDataCleaner.clean(data), end="\n")
    
     