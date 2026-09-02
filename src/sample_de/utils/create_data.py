import os
import logging
import random
from datetime import datetime, timedelta
import pandas as pd


class sample_data_creator:
    """A class to create sample datasets for testing purposes.
    Attributes:
        name (str): The name of the dataset creator.
    Methods:
        sample_sales_dataset(dataset_path, num_rows=100): Creates a test e-commerce sales dataset and saves it to a {dataset_path} file.
        sample_stock_dataset(dataset_path, num_rows=100): Creates a test stock dataset and saves it to a {dataset_path} file.
    """
    def __init__(self, name):
        self.name = name

    def create_demo_sales_dataset(self, dataset_path, num_rows=100):
        """
        Creates a test e-commerce sales dataset and saves it to a {dataset_path} file.
        Parameters:
            dataset_path (str): The path where the test dataset will be saved.
            num_rows (int): The number of rows to generate in the dataset.
        Raises:
            ValueError: If the dataset_path is not set or is empty.
        Returns:
            None
        """
        if dataset_path is None or dataset_path.strip() == "":
            raise ValueError("DATASET is not set in the environment variables.")      
        
        categories_pool = {
            "Electronics": ["Laptop", "Smartphone", "Headphones", "Smartwatch"],
            "Clothing": ["Jeans", "T-Shirt", "Jacket", "Sneakers"],
            "Home Appliances": ["Coffee Maker", "Microwave", "Vacuum Cleaner", "Air Purifier"],
        }
        regions_pool = ["North", "East", "West", "South", "Central"]
        data_list = []
        # 360 days ago from today
        start_date = datetime.now() - timedelta(days=360)
        for i in range(num_rows):
            category = random.choice(list(categories_pool.keys()))
            subcategory = random.choice(categories_pool[category])
            product = random.choice(categories_pool[category])
            quantity = random.choice([None, random.randint(1, 50)])
            price_per_unit = round(random.uniform(10.0, 1000.0), 2)
            date = start_date + timedelta(days=random.randint(0, 360))
            region = random.choice(regions_pool)
            data_list.append({
                "Order_ID": i + 1,
                "Date": date.strftime("%Y-%m-%d"),
                "Product": product,
                "Category": category,
                "Subcategory": subcategory,
                "Quantity": quantity,
                "Price_Per_Unit": price_per_unit,
                "Region": region
            })
        pd.DataFrame(data_list).to_csv(dataset_path, index=False)

    def create_demo_stock_dataset(self,dataset_path, num_rows=100):
        """
        Creates a test stock dataset and saves it to a {dataset_path} file.
        Parameters:
            dataset_path (str): The path where the test dataset will be saved.
            num_rows (int): The number of rows to generate in the dataset.
        Raises:
            ValueError: If the dataset_path is not set or is empty.
        Returns:
            None
        """
        if dataset_path is None or dataset_path.strip() == "":
            raise ValueError("DATASET is not set in the environment variables.")      
        
        data_list = []
        # 360 days ago from today
        freq="D"
        days = 360
        start_date = datetime.now() - timedelta(days=360)
        date_range = pd.date_range(start=start_date, periods=days, freq=freq)
        for i in range(num_rows):
            date = start_date + timedelta(days=random.randint(0, 360))
            open_price = round(random.uniform(100.0, 500.0), 2)
            close_price = round(open_price + random.uniform(-10.0, 10.0), 2)
            high_price = round(max(open_price, close_price) + random.uniform(0.0, 5.0), 2)
            low_price = round(min(open_price, close_price) - random.uniform(0.0, 5.0), 2)
            volume = random.randint(1000, 100000)
            data_list.append({
                "Date": date.strftime("%Y-%m-%d"),
                "Open": open_price,
                "High": high_price,
                "Low": low_price,
                "Close": close_price,
                "Volume": volume
            })
        pd.DataFrame(data_list).to_csv(dataset_path, index=False) 

    def __str__(self):
        return f"{self.name}"

    # Equivalent to toString() for debugging
    def __repr__(self):
        return f"SampleDatasetCreator(name='{self.name}')"        
  
       
if __name__ == "__main__":
    from dotenv import load_dotenv 
    load_dotenv()  # Load environment variables from .env file
    sampleDsCreator = sample_data_creator("sample data creator")
    sampleDsCreator.create_demo_sales_dataset(os.getenv("DATASET"), num_rows=100)  # Call the function to create the test dataset with 100 rows 
    sampleDsCreator.create_demo_stock_dataset(os.getenv("STOCK_DATASET"), num_rows=100)  # Call the function to create the test stock dataset with 100 rows 
