from sample_de.utils.systemvariable import systemvariablemanager
import logging
from sample_de.db.persist_in_csv import persist_in_csv
from sample_de.utils.create_data import sample_data_creator
from sample_de.process.clean_data import clean_data

class process_data:
    """
    A class to process cleaned e-commerce sales data.
    """

    def __init__(self, cleaned_df):
        """
        Initializes the process_data class with the cleaned DataFrame.

        Parameters:
        - cleaned_df: pd.DataFrame, cleaned DataFrame.
        """
        self.data = cleaned_df
        self.envreader = systemvariablemanager()

    def process(self):
        """
        Process the input data and return the processed data.
        Args:
            None
        Returns:
            list: A list of dictionaries representing the processed data.
        """
        logging.info("--- Data Manipulation and Feature Engineering ---")
        if self.data is None or self.data.empty:
            logging.info("Input data is empty. Returning empty list.")
            return [], []
        
        # Total Revenue calculation
        self.data["Total_Sales"] = self.data["Quantity"] * self.data["Price_Per_Unit"]

        # Month extraction from the 'Date' column
        self.data["Month"] = self.data["Date"].dt.strftime("%b")  # e.g.: Jan, Feb, Mar
        logging.info("Data processing completed.")
        self.data["Full_Category"] = self.data["Category"] + " -> " + self.data["Subcategory"]

        # --- Data Analysis and Aggregation ---
        logging.info("--- Data Analysis and Summary ---")

        # a) How many units were sold?
        grand_total = self.data["Total_Sales"].sum()
        logging.info(f"Grand Total (Total Revenue): ${grand_total:,}")
        
        # b) How much revenue came from each category?
        #category_sales = self.data.groupby("Category")["Total_Sales"].sum().reset_index()
        #logging.info("Category-wise Sales:")
        #logging.info(category_sales)
        # c) Which product had the highest quantity sold?
        product_qty = (
            self.data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
        )
        logging.info("Product-wise Quantity Sold:")
        logging.info(product_qty)
        persistInCSV=persist_in_csv()
        persistInCSV.persist(self.data, self.envreader.get_env("CLEANED_DATASET_SUBCAT"))
        return self.data

    def process_data_category(self):
        """
        Process the input data and return the processed data.
        
        Args:
            None.    

        Returns:
            list: A list of dictionaries representing the processed data.
        """
        logging.info("--- Data Manipulation and Feature Engineering ---")
        if self.data is None or self.data.empty:
            logging.info("Input data is empty. Returning empty list.")
            return [], []
        
        # Total Revenue calculation
        self.data["Total_Sales"] = self.data["Quantity"] * self.data["Price_Per_Unit"]

        # Month extraction from the 'Date' column
        self.data["Month"] = self.data["Date"].dt.strftime("%b")  # e.g.: Jan, Feb, Mar
        logging.info("Data processing completed.")

        # --- Data Analysis and Aggregation ---
        logging.info("--- Data Analysis and Summary ---")

        # a) How many units were sold?
        grand_total = self.data["Total_Sales"].sum()
        logging.info(f"Grand Total (Total Revenue): ${grand_total:,}")
        
        # b) How much revenue came from each category?
        category_sales = self.data.groupby("Category")["Total_Sales"].sum().reset_index()
        logging.info("Category-wise Sales:")
        logging.info(category_sales)
        # c) Which product had the highest quantity sold?
        product_qty = (
            self.data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
        )
        logging.info("Product-wise Quantity Sold:")
        logging.info(product_qty)
        persistData = persist_in_csv()
        persistData.persist(self.data, self.envreader.get_env("CLEANED_DATASET"))
        #self.data.to_csv(oself.envreader.get_env("CLEANED_DATASET"), index=False)
        return self.data, category_sales
    
    def __str__(self):
        return f"process_data(data={self.data.shape[0]} rows)"
    
    def __repr__(self):
        return f"process_data(data={self.data.shape[0]} rows)"
    

if __name__ == "__main__":
    load_dotenv()
    # Create a sample dataset for testing purposes
    # Example usage
    demoData = sample_data_creator("Demo Data Creator")
    demoData.create_demo_sales_dataset(os.getenv("DATASET"), num_rows=100)
    cleaned_data = clean_data(os.getenv("DATASET"))
    dataProcessor = process_data(cleaned_data.clean())
    processedData = dataProcessor.process()
    print(f"Processed Data: {processedData} \n")
    processedData, categorysales = dataProcessor.process_data_category()
    print(f"Processed Data: {processedData} \n Category Sales: {categorysales}")
