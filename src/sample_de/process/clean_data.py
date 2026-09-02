import os
import pandas as pd
import logging


class clean_data:
    """
    A class to clean raw e-commerce sales data.
    """
    logging.basicConfig(level=logging.INFO)
    
    def __init__(self, file_path):
        """
        Initializes the clean_data class with the path to the raw CSV file.

        Parameters:
        - file_path: str, path to the raw CSV file.
        """
        self.file_path = file_path

    def clean(self):
        """
        Cleans the raw e-commerce sales data.

        Returns:
        - df: pd.DataFrame, cleaned DataFrame.
        """
        # Load the dataset
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file at {self.file_path} does not exist.")
        df = pd.read_csv(self.file_path)

        # --- Step 2: Data Cleaning ---
        logging.info("--- Cleaning Data ---")
        df.drop_duplicates(inplace=True)
        # Handle missing values in 'Quantity' column by filling with 0
        df['Quantity'] = df['Quantity'].fillna(1)  # Assuming missing quantities are 1
        #Change quantity to integer type
        df['Quantity'] = df['Quantity'].astype(int)
        # Convert 'Date' column to datetime format
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        
        # Drop rows with invalid dates
        df = df.dropna(subset=['Date'])
        
        # Remove duplicate rows based on 'Order_ID'
        df = df.drop_duplicates(subset=['Order_ID'])
        logging.info("Data cleaning completed")
        return df
    
    def __str__(self):
        return f"clean_data(file_path='{self.file_path}')"
    
    def __repr__(self):
        return f"clean_data(file_path='{self.file_path}')"
    


if __name__ == "__main__":
    # Load environment variables from .env file
    from dotenv import load_dotenv
    load_dotenv()
    
    cleaned = clean_data( os.getenv("DATASET"))
    cleaned_df = cleaned.clean()
    print("Cleaned data shape:", cleaned_df.shape)
    print("Cleaned Data:", cleaned_df.head(), "\n")





