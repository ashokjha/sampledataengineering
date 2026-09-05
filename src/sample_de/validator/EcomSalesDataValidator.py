from sample_de.validator.DataValidator import DataValidator
import pandas as pd

class EcomSalesDataValidator(DataValidator):
    """Sales data validator
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
        pass
    
if __name__ == "__main__":    
    from sample_de.data.SalesDataCreator import SalesDataCreator
    sdcreator = SalesDataCreator()
    data = sdcreator.create('data/sample_ecommerce_sales_remove.csv')
    esdv = EcomSalesDataValidator()
    esdv.validate(data)  