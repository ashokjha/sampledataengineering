from sample_de.validator.DataValidator import DataValidator
import pandas as pd

class StockDataValidator(DataValidator):
    """ Stock Data Validator
    """
    def __init__(self):
        super().__init__()
        
    def validate(self, data: pd.DataFrame) -> bool:
        """validate Data
        Args:
            data(pd.DataFrame): 

        Returns:
            True/False:
        """
        required_columns = {'Open', 'High', 'Low', 'Close', 'Volume'}
        if data is None or data.empty or not required_columns.issubset(data.columns):
            raise ValueError(f"The dataset must contain the following columns: {required_columns}")        
        return True
    
if __name__ == "__main__":
    from sample_de.data.StockDataCreator import StockDataCreator
    stockDataCreator = StockDataCreator()
    data = stockDataCreator.create_data('data/sampleStock.csv')    
    esdv = StockDataValidator()
    esdv.validate(data)    