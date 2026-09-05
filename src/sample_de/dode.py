import os
from dotenv import load_dotenv
import logging
import logging.config
import pathlib
import json

from sample_de.DataEngPipeline import DataEnggPipeline
from sample_de.data.SalesDataCreator import SalesDataCreator
from sample_de.data.StockDataCreator import StockDataCreator
from sample_de.validator.EcomSalesDataValidator import EcomSalesDataValidator
from sample_de.validator.StockDataValidator import StockDataValidator
from sample_de.clean.SalesDataCleaner import SalesDataCleaner
from sample_de.clean.StockDataCleaner import StockDataCleaner
from sample_de.process.SalesDataProcessor import SalesDataProcessor
from sample_de.process.StockDataProcessor import StockDataProcessor
from sample_de.viz.EcomSalesDataVisualizer  import EcomSalesDataVisualizer
from sample_de.viz.StockDataVisualizer import StockDataVisualizer

from sample_de.utils.create_data import sample_data_creator
from sample_de.process.clean_data import clean_data
from sample_de.process.process_data import process_data
from sample_de.viz.create_candlestick_chart import candle_stick_chart
from sample_de.viz.analysis_visual import sales_and_revenue
class Dode:
    """
    A class to handle the data processing pipeline.
    This class is responsible for setting up logging, loading environment variables,
    creating sample datasets, cleaning and processing data, and generating visualizations.
    """
    def __init__(self):
        load_dotenv()  # Load environment variables from .env file
        self.dataset_path = os.getenv("DATASET")
        self.stock_dataset_path = os.getenv("STOCK_DATASET")
        self.dataset_creator = sample_data_creator(name="Test Dataset Creator")
        self.setup_logging()

    def setup_logging(self):
        """
        Sets up logging configuration from logging.json file.
        """
        with open("logging.json", "r") as f:
            config = json.load(f)
            log_file_path = config.get("handlers", {}).get("file", {}).get("filename")
            print("🔄 [SYSTEM] Log file path:", log_file_path)
            if log_file_path:
                log_dir = pathlib.Path(log_file_path).parent
                log_dir.mkdir(parents=True, exist_ok=True)
            logging.config.dictConfig(config)

    def execute(self):
        """
        Runs the entire data processing pipeline:
            <ul>Creates sample datasets.</ul>
            <ul> validate data </ul>
            <ul> Cleans the data.</ul>
            <ul> Processes the cleaned data.</ul>
            <ul> Generates visualizations.</ul>
        """
        
        depipeline = DataEnggPipeline(self.stock_dataset_path, 
                                        StockDataCreator(), 
                                        StockDataValidator(), 
                                        StockDataCleaner(),
                                        StockDataProcessor(),
                                        StockDataVisualizer())
        
        depipeline.run()
        del depipeline
        depipeline = DataEnggPipeline(self.dataset_path, 
                                        SalesDataCreator(), 
                                        EcomSalesDataValidator(), 
                                        SalesDataCleaner(),
                                        SalesDataProcessor(),
                                        EcomSalesDataVisualizer())
        depipeline.run()
            
            
            
        
    
    def run_pipeline(self):
        """
        Runs the entire data processing pipeline:
        <ul>Creates sample datasets.</ul>
        <ul> validate data </ul>
        <ul> Cleans the data.</ul>
        <ul> Processes the cleaned data.</ul>
        <ul> Generates visualizations.</ul>
        """
        
        
        logging.info("Creating sample dataset at: %s", self.dataset_path)
        
        
        
        
        self.dataset_creator.create_demo_sales_dataset(self.dataset_path, num_rows=100)
        
        logging.info("Cleaning data from: %s", self.dataset_path)
        cleanedDataSet = clean_data(self.dataset_path)
        self.cleaned_df = cleanedDataSet.clean()
        logging.info("Cleaned data shape: %s", self.cleaned_df.shape)
        
        logging.info("Processing cleaned data...")
        dataProcessor = process_data(self.cleaned_df)
        processedData, categorysales = dataProcessor.process_data_category()
        logging.info("Processed data shape: %s", processedData.shape)
        logging.info("Category sales shape: %s", categorysales.shape)
        salesRevchart = sales_and_revenue(processedData) 
        salesRevchart.create_visualizations_category(categorysales)   
        processing_results = dataProcessor.process()
        logging.info("Processed data shape: %s", processing_results.shape)
        salesRevchart.data = processing_results
        salesRevchart.create_visualizations()    
        
        logging.info("Creating sample stock dataset at: %s", self.stock_dataset_path)
        self.dataset_creator.create_demo_stock_dataset(self.stock_dataset_path, num_rows=25)
        candlestickChart=candle_stick_chart(self.stock_dataset_path)
        candlestickChart.create_candlestick_chart()
        candlestickChart.create_advanced_candlestick_chart()
    
    
    def __str__(self):
        return f"Dode(dataset_path='{self.dataset_path}', stock_dataset_path='{self.stock_dataset_path}')"
    
    def __repr__(self):
        return f"Dode(dataset_path='{self.dataset_path}', stock_dataset_path='{self.stock_dataset_path}')"
    
if __name__ == "__main__":
    dode = Dode()
    #dode.run_pipeline()
    dode.execute()
