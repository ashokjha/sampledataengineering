from abc import ABC, abstractmethod

# ==========================================
# 1. Base Interfaces (3 steps rule)
#    ABC=> AbstractBaseClass
# ==========================================
class DataCleaner(ABC):
    @abstractmethod
    def clean(self, data: dict) -> dict: pass

class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: dict) -> dict: pass

class DataVisualizer(ABC):
    @abstractmethod
    def visualize(self, data: dict): pass


# ==========================================
# 2. Sales Domain Delegates
# ==========================================
class SalesCleaner(DataCleaner):
    def clean(self, data: dict) -> dict:
        print("[SalesCleaner] Filling missing discounts with 0...")
        data["discount"] = data.get("discount", 0.0)
        return data

class SalesProcessor(DataProcessor):
    def process(self, data: dict) -> dict:
        print("[SalesProcessor] Calculating Net Price after discount...")
        data["net_price"] = data["price"] - data["discount"]
        return data

class SalesVisualizer(DataVisualizer):
    def visualize(self, data: dict):
        print(f"[SalesVisualizer] 📊 Drawing Bar Chart for Product: {data['product']} (Net: ${data['net_price']})")


# ==========================================
# 3. Finance Domain Delegates
# ==========================================
class FinanceCleaner(DataCleaner):
    def clean(self, data: dict) -> dict:
        print("[FinanceCleaner] Removing whitespace from Account Numbers...")
        data["account"] = str(data["account"]).strip()
        return data

class FinanceProcessor(DataProcessor):
    def process(self, data: dict) -> dict:
        print("[FinanceProcessor] Checking compliance and risk flags...")
        data["risk_level"] = "HIGH" if data["amount"] > 50000 else "LOW"
        return data

class FinanceVisualizer(DataVisualizer):
    def visualize(self, data: dict):
        print(f"[FinanceVisualizer] 📈 Drawing Trend Line Chart for Account: {data['account']} (Risk: {data['risk_level']})")


# ==========================================
# 4. The Master Pipeline Orchestrator (The Delegator)
# ==========================================
class DataEngineeringPipeline:
    def __init__(self, cleaner: DataCleaner, processor: DataProcessor, visualizer: DataVisualizer):
        # तीनों चरणों के डेलीगेट्स को रनटाइम पर स्वीकार करना
        self.cleaner = cleaner
        self.processor = processor
        self.visualizer = visualizer

    def run(self, raw_data: dict):
        # पूरी पाइपलाइन को डेलीगेट करना
        cleaned = self.cleaner.clean(raw_data)
        processed = self.processor.process(cleaned)
        self.visualizer.visualize(processed)


# ==========================================
# 5. Runtime Execution
# ==========================================
if __name__ == "__main__":
    
    # 🛍️ Sales Pipeline
    raw_sales = {"product": "Laptop", "price": 1000.0} # discount missing है
    sales_pipeline = DataEngineeringPipeline(SalesCleaner(), SalesProcessor(), SalesVisualizer())
    print("\n--- Running Sales Pipeline ---")
    sales_pipeline.run(raw_sales)

    # 💰 Finance Pipeline
    raw_finance = {"account": "  ACT12345  ", "amount": 65000.0}
    finance_pipeline = DataEngineeringPipeline(FinanceCleaner(), FinanceProcessor(), FinanceVisualizer())
    print("\n--- Running Finance Pipeline ---")
    finance_pipeline.run(raw_finance)
