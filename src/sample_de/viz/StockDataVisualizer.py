import logging
import pandas as pd
import mplfinance as mpf
import os

from sample_de.viz.DataVisualizer import DataVisualizer
from sample_de.utils.systemvariable import systemvariablemanager
from sample_de.utils.common_util import common_util
from sample_de.utils.translation import TranslationManager


class StockDataVisualizer(DataVisualizer):
    """Salesdatavisual creator

    Args:
        DataVisualizer (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.envreader = systemvariablemanager()
        self.langLocal = common_util.getLangLocal()
        self.translation = TranslationManager()
        self.chartsPath = common_util.getChartPath()        
    
    def visualize(self, data: pd.DataFrame) -> None:
        """Visualize for stock data
            <li><b>Line Chart</b> - Monthly Sales Trend by Subcategory
            <li><b>Box Plot</b > - Price Distribution across Category & Subcategory</li>        
        Args:
            data(pd.DataFrame): 

        Returns:
            None:
        """
        data = data.assign(Date=pd.to_datetime(data['Date'])).set_index('Date')
        print(data)
        self.candlestickChart(data)
        self.advanceCandlestickChart(data)
    

    def candlestickChart(self, data: pd.DataFrame ) -> None:
        """ Create visual for
        <li><b>Lcandle stick chart

        Args:
            data (pd.DataFrame): DataFrame
        """
        chartfilePath = os.path.join(self.chartsPath, f"candle_chart_{self.langLocal}.png")
        
        # Plot and save the candlestick chart
        mpf.plot(
            data, 
            type='candle', 
            style='yahoo',          # Popular green/red theme
            volume=True,            # Show volume bars below
            title=self.translation.get_text('Stock_Performance_Candlestick_Chart', self.langLocal),
            ylabel=self.translation.get_text('Price_Dollar', self.langLocal),
            ylabel_lower=self.translation.get_text('Volume', self.langLocal),
            savefig=chartfilePath
        )
    
    
    def advanceCandlestickChart(self, data: pd.DataFrame ) -> None:
        """ Create visual for
        <li>Advance Lcandle stick chart
        Args:
            data (pd.DataFrame): DataFrame
        """
        # Plot and save the advanced candlestick chart with RSI and MACD
        price_changes = data['Close'].diff()
        gain = (price_changes.where(price_changes > 0, 0)).rolling(window=14).mean()
        loss = (-price_changes.where(price_changes < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        data['RSI'] = 100 - (100 / (1 + rs))
        
        data['EMA12'] = data['Close'].ewm(span=12, adjust=False).mean()
        data['EMA26'] = data['Close'].ewm(span=26, adjust=False).mean()
        data['MACD'] = data['EMA12'] - data['EMA26']
        data['Signal'] = data['MACD'].ewm(span=9, adjust=False).mean()
        
        chartfilePath = os.path.join(self.chartsPath, f"advanced_candle_chart_{self.langLocal}.png")
        plots = [
            mpf.make_addplot(data['RSI'], panel=2, color='blue', ylabel='RSI (14)'),
            mpf.make_addplot(pd.Series(70, index=data.index), panel=2, color='gray', linestyle='--'), 
            mpf.make_addplot(pd.Series(30, index=data.index), panel=2, color='gray', linestyle='--'), 
            mpf.make_addplot(data['MACD'], panel=3, color='black', ylabel='MACD'),
            mpf.make_addplot(data['Signal'], panel=3, color='gray', linestyle='-'),
            mpf.make_addplot(data['MACD'] - data['Signal'], panel=3, type='bar', color='darkgray', alpha=0.7)
        ]
        
        mpf.plot(
            data, 
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
            savefig=chartfilePath
        )
        logging.info(f"Chart created sucessfully in ${chartfilePath}")  
    
        
    
if __name__ == "__main__" :
    # below import required in main only
    from sample_de.data.StockDataCreator import StockDataCreator
    from sample_de.validator.StockDataValidator import StockDataValidator
    from sample_de.clean.StockDataCleaner import StockDataCleaner
    from sample_de.process.StockDataProcessor import StockDataProcessor
    
    stockDataCreator = StockDataCreator()
    data = stockDataCreator.create('data/sampleStock.csv')
    sdvalidator = StockDataValidator()
    sdvalidator.validate(data)  
    stockDataCleaner = StockDataCleaner()
    print(stockDataCleaner.clean(data), end="\n")
    sdp = StockDataProcessor()
    sdp.process(data)
    sdv = StockDataVisualizer()
    sdv.visualize(data)        
        
