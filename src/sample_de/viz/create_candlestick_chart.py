import os
import pandas as pd
import mplfinance as mpf

from sample_de.utils.common_util import common_util
from sample_de.utils.translation import TranslationManager

class candle_stick_chart:
    """_summary_
    """
    def __init__(self, datasetpath):
        self.datasetpath = datasetpath
        self.translation = TranslationManager()
        self.langLocal = common_util.getLangLocal()
        self.chartLocation = common_util.getChartPath()
    
    
    def create_candlestick_chart(self):
        """
        Creates a candlestick chart from the stock dataset and saves it as an image.
        Raises:
            ValueError: If the dataset_path is not set or is empty.
        Returns:
            None
        """
        if self.datasetpath is None or self.datasetpath.strip() == "":
            raise ValueError("STOCK_DATASET is not set in the environment variables.")
        
        # Load the stock dataset
        stock_data = pd.read_csv(self.datasetpath, parse_dates=['Date'], index_col='Date')
        # Ensure the DataFrame has the required columns
        required_columns = {'Open', 'High', 'Low', 'Close', 'Volume'}
        if not required_columns.issubset(stock_data.columns):
            raise ValueError(f"The dataset must contain the following columns: {required_columns}")

        chartPath = os.path.join(self.chartLocation, f"candle_chart_{self.langLocal}.png")
        
        # Plot and save the candlestick chart
        mpf.plot(
            stock_data, 
            type='candle', 
            style='yahoo',          # Popular green/red theme
            volume=True,            # Show volume bars below
            title=self.translation.get_text('Stock_Performance_Candlestick_Chart', self.langLocal),
            ylabel=self.translation.get_text('Price_Dollar', self.langLocal),
            ylabel_lower=self.translation.get_text('Volume', self.langLocal),
            savefig=chartPath
        )
        
        print(f"📈 Candlestick chart successfully saved at {self.chartLocation}")
        
    def create_advanced_candlestick_chart(self): 
        """
        Creates an advanced candlestick chart with RSI and MACD indicators from the stock dataset and saves it as an image.
        Raises:
            ValueError: If the dataset_path is not set or is empty.
        Returns:
            None
        """
        if self.datasetpath is None or self.datasetpath.strip() == "":
            raise ValueError("STOCK_DATASET is not set in the environment variables.")
        
        # Load the stock dataset
        stock_data = pd.read_csv(self.datasetpath, parse_dates=['Date'], index_col='Date')
        
        # Ensure the DataFrame has the required columns
        required_columns = {'Open', 'High', 'Low', 'Close', 'Volume'}
        if not required_columns.issubset(stock_data.columns):
            raise ValueError(f"The dataset must contain the following columns: {required_columns}")

        # Plot and save the advanced candlestick chart with RSI and MACD
        price_changes = stock_data['Close'].diff()
        gain = (price_changes.where(price_changes > 0, 0)).rolling(window=14).mean()
        loss = (-price_changes.where(price_changes < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        stock_data['RSI'] = 100 - (100 / (1 + rs))
        
        stock_data['EMA12'] = stock_data['Close'].ewm(span=12, adjust=False).mean()
        stock_data['EMA26'] = stock_data['Close'].ewm(span=26, adjust=False).mean()
        stock_data['MACD'] = stock_data['EMA12'] - stock_data['EMA26']
        stock_data['Signal'] = stock_data['MACD'].ewm(span=9, adjust=False).mean()
        
        chartPath = os.path.join(self.chartLocation, f"advanced_candle_chart_{self.langLocal}.png")
        plots = [
            mpf.make_addplot(stock_data['RSI'], panel=2, color='blue', ylabel='RSI (14)'),
            mpf.make_addplot(pd.Series(70, index=stock_data.index), panel=2, color='gray', linestyle='--'), 
            mpf.make_addplot(pd.Series(30, index=stock_data.index), panel=2, color='gray', linestyle='--'), 
            mpf.make_addplot(stock_data['MACD'], panel=3, color='black', ylabel='MACD'),
            mpf.make_addplot(stock_data['Signal'], panel=3, color='gray', linestyle='-'),
            mpf.make_addplot(stock_data['MACD'] - stock_data['Signal'], panel=3, type='bar', color='darkgray', alpha=0.7)
        ]
        
        mpf.plot(
            stock_data, 
            type='candle', 
            style='classic',
            volume=True,            
            addplot=plots,          
            main_panel=0,
            volume_panel=1,
            num_panels=4,           
            panel_ratios=(4, 1, 2, 2), 
            title='Classic B&W Analytics (MA, RSI, MACD)',
            figsize=(12, 10),       
            savefig=chartPath
        )
       