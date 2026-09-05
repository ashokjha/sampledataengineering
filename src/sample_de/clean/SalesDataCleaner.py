
import logging
import pandas as pd
from sample_de.clean.BaseDataCleaner import BaseDataCleaner



class SalesDataCleaner(BaseDataCleaner):
    """Sales Data Cleaner

    Args:
        BaseDataCleaner (_type_): _description_
    """
    
    def __init__(self):
        super().__init__()
    
    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """To clean data
        Args:
            dataFrame: Panda DataFrame

        Returns:
            data: pandas DataFrame
        """
        #df = pd.DataFrame(data)
        logging.info(f"--- Cleaning Data --- size {df.size}")
        df.drop_duplicates(inplace=True)
        # Handle missing values in 'Quantity' column by filling with 0
        df['Quantity'] = df['Quantity'].fillna(1)  # Assuming missing quantities are 1
        #Change quantity to integer type
        df['Quantity'] = df['Quantity'].astype(int)
        # Convert 'Date' column to datetime format
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        
        # Drop rows with invalid dates
        df.dropna(subset=['Date'], inplace=True)
        
        # Remove duplicate rows based on 'Order_ID'
        df.drop_duplicates(subset=['Order_ID'], inplace=True)
        logging.info(f"Data cleaning completed {df.size}")
        return df
        
if __name__ == "__main__" :
    from sample_de.data.SalesDataCreator import SalesDataCreator
    from sample_de.validator.EcomSalesDataValidator import EcomSalesDataValidator
    salesDataCreator = SalesDataCreator()
    data = salesDataCreator.create('data/sample_Stock_remove.csv')
    ecdvalidator = EcomSalesDataValidator()
    ecdvalidator.validate(data)
    sdcleaner = SalesDataCleaner()
    print(f"original date shape: {data.shape}", end="\n")
    #kept if implementation does not do inpllace cleaning
    cleanedData = sdcleaner.clean(data)
    print(f"cleaned data shape : {cleanedData.shape}", end="\n")
    print(f"original date shape: {data.shape}", end="\n")      
    #print(f"cleaned data shape {cleanedData}}, end="\n")
    
    
     