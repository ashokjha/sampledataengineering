import logging
import pandas as pd

from sample_de.process.BaseDataProcessor import BaseDataProcessor
from sample_de.utils.systemvariable import systemvariablemanager
from sample_de.db.persist_in_csv import persist_in_csv


class SalesDataProcessor(BaseDataProcessor):
    """Sales Data Processor

    Args:
        BaseDataProcessor (_type_): _description_
    """
    
    def __init__(self):
        super().__init__()
        self.envreader = systemvariablemanager()
    
    
    def process(self, data: pd.DataFrame) -> pd.DataFrame:
        """Process Sales Data
        Args:
            data(pd.DataFrame): 

        Returns:
            processedData(pd.DataFrame):
        """
        logging.info("--- Processinging Data ---")
        if data is None or data.empty:
            logging.info("Input data is empty. Returning empty list.")
            return data
        # Total Revenue calculation
        data["Total_Sales"] = data["Quantity"] * data["Price_Per_Unit"]

        # Month extraction from the 'Date' column
        data["Month"] = data["Date"].dt.strftime("%b")  # e.g.: Jan, Feb, Mar
        logging.info("Data processing completed.")
        data["Full_Category"] = data["Category"] + " -> " + data["Subcategory"]
        # --- Data Analysis and Aggregation ---
        logging.info("--- Data Analysis and Summary ---")
        # How many units were sold?
        grand_total = data["Total_Sales"].sum()
        logging.info(f"Grand Total (Total Revenue): ${grand_total:,}")
        # Which product had the highest quantity sold?
        product_qty = (
            data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
        )
        logging.info("Product-wise Quantity Sold:")
        logging.info(product_qty)
        persistInCSV=persist_in_csv()
        persistInCSV.persist(data, self.envreader.get_env("CLEANED_ESALES_DATASET"))
        return data
        
if __name__ == "__main__" :
    # below import required in main only
    from sample_de.data.SalesDataCreator import SalesDataCreator
    from sample_de.clean.SalesDataCleaner import SalesDataCleaner
     
    salesDataCreator = SalesDataCreator()
    data = salesDataCreator.create_data('data/sample_Stock_remove.csv')
    sdc = SalesDataCleaner()
    sdc.clean_data(data)
    sdp = SalesDataProcessor()
    sdp.process(data)
    
    
     