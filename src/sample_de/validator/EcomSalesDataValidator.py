from sample_de.validator.DataValidator import DataValidator
import pandas as pd

class EcomSalesDataValidator(DataValidator):
    """Sales data validator
    """
    def validate(self, data: pd.DataFrame) -> bool:
        """validate Data
        Args:
            data(pd.DataFrame): 

        Returns:
            True/False:
        """
        pass
    
if __name__ == "__main__":
    esdv = EcomSalesDataValidator()
    esdv.validate(None)  