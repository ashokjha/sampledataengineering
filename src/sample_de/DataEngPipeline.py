from sample_de.data.BaseDataCreator import BaseDataCreator
from sample_de.validator.DataValidator import DataValidator
from sample_de.clean.BaseDataCleaner import BaseDataCleaner
from sample_de.process.BaseDataProcessor import BaseDataProcessor
from sample_de.viz.DataVisualizer import DataVisualizer

class DataEnggPipeline:
    """
    5 step Process of Data Engineering
    """

    def __init__(self,  path: str, creator: BaseDataCreator, validator: DataValidator, 
                 cleaner: BaseDataCleaner, processor: BaseDataProcessor, 
                 visualizer: DataVisualizer):
        """_summary_

        Args:
            path (str): Data Path 
            creator (BaseDataCreator): _description_
            validator (DataValidator): _description_
            cleaner (BaseDataCleaner): _description_
            processor (BaseDataProcessor): _description_
            visualizer (DataVisualizer): _description_
        """
        self.dataPath =  path
        print(f"const datasetPath-> {self.dataPath}")
        self.creator = creator
        self.validator = validator 
        self.cleaner = cleaner
        self.processor = processor
        self.visualizer = visualizer

    def run(self):
        # Deligate the pipeline
        print(f"Dataset path => {self.dataPath}")
        data = self.creator.create(self.dataPath)
        print(f'data.   {data}')
        if (self.validator.validate(data) == True) : 
            cleaned = self.cleaner.clean(data)
            processed = self.processor.process(cleaned)
            self.visualizer.visualize(processed)
        else:
            print('Data  is not correct')   
            
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
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
    from sample_de.utils.systemvariable import systemvariablemanager
    load_dotenv()
    dataset_path = os.getenv("DATASET")
    print(f"main-> {dataset_path}")
    stock_dataset_path = os.getenv("STOCK_DATASET")
    depipeline = DataEnggPipeline(stock_dataset_path, 
                                    StockDataCreator(), 
                                    StockDataValidator(), 
                                    StockDataCleaner(),
                                    StockDataProcessor(),
                                    StockDataVisualizer())
    
    depipeline.run()
    del depipeline
    print(dataset_path)
    depipeline = DataEnggPipeline(dataset_path, 
                                    SalesDataCreator(), 
                                    EcomSalesDataValidator(), 
                                    SalesDataCleaner(),
                                    SalesDataProcessor(),
                                    EcomSalesDataVisualizer())    
    depipeline.run()
    del depipeline
