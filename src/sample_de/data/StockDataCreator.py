from sample_de.data.BaseDataCreator import BaseDataCreator
from datetime import datetime, timedelta
import random
import pandas as pd


class StockDataCreator(BaseDataCreator):
    """
    Stock Data Creator
    """
    
    def __init__(self):
        super().__init__()
    
    def create_data(self, dataset_path:str) -> pd.DataFrame:
        """
        Creates a test stock dataset and saves it to a {dataset_path} file.
        Parameters:
            dataset_path (str): The path where the test dataset will be saved.
        Raises:
            ValueError: If the dataset_path is not set or is empty.
        Returns:
            DataFrame:
        """
        if dataset_path is None or dataset_path.strip() == "":
            raise ValueError("DATASET is not set in the environment variables.")      
        
        data_list = []
        # 360 days ago from today
        freq = "D"
        days = 360
        num_rows = 50
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
        df = pd.DataFrame(data_list)    
        df.to_csv(dataset_path, index=False) 
        return df
        
if __name__ == "__main__" :
    stockDataCreator = StockDataCreator()
    stockDataCreator.create_data('data/sample_Stock_remove.csv')
     