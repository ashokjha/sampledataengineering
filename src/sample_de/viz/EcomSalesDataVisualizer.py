import logging
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import calendar

from sample_de.viz.DataVisualizer import DataVisualizer
from sample_de.utils.systemvariable import systemvariablemanager
from sample_de.utils.common_util import common_util
from sample_de.utils.translation import TranslationManager


class EcomSalesDataVisualizer(DataVisualizer):
    """Salesdatavisual creator

    Args:
        DataVisualizer (_type_): _description_
    """
    def __init__(self):
        super().__init__()
        self.envreader = systemvariablemanager()
        self.langLocal = common_util.getLangLocal()
        self.reportTheme = self.envreader.get_env("REPORT_THEME", "whitegrid")
        self.palette = self.envreader.get_env("PALETTE","viridis")
        self.translation = TranslationManager()
        self.chartsPath = common_util.getChartPath()        
    
    def visualize(self, data: pd.DataFrame) -> None:
        """Visualize Data
        Args:
            data(pd.DataFrame): 

        Returns:
            None:
        """
        logging.info("Visualizations (Creating Charts) ---")
        # setting: Charts to look nice set Seaborn style
        sns.set_theme(style=self.reportTheme)
        self.monthlySalesTrendAndPriceDist(data)
        self.revenueAndMonthlySalesTrend(data)
    
    def monthlySalesTrendAndPriceDist(self, data: pd.DataFrame ) -> None:
        """ Create visual for
        <li><b>Line Chart</b> - Monthly Sales Trend by Subcategory
        <li><b>Box Plot</b > - Price Distribution across Category & Subcategory</li>

        Args:
            data (pd.DataFrame): DataFrame
        """
                #Line and Box Chart
        fig, axes = plt.subplots(2, 1, figsize=(14, 12))
        # -------------------------------------------------------------
        # Chart 1: Line Chart - Monthly Sales Trend by Subcategory
        # -------------------------------------------------------------
        #Group the data by Month and Subcategory, summing the Total_Sales 
        trend_data = data.groupby(["Month", "Subcategory"])["Total_Sales"].sum().reset_index()
        sns.lineplot(
            ax=axes[0],
            data=trend_data,
            x="Month",
            y="Total_Sales",
            hue="Subcategory",  # create a line for each Subcategory
            marker="o",
            linewidth=2
        )
        axes[0].set_title(self.translation.get_text("Monthly_Sales_Trend_by_Subcategory", self.langLocal), 
                          fontsize=14, fontweight="bold")
        axes[0].set_xlabel(self.translation.get_text("Month_Timeline", self.langLocal), fontsize=12)
        axes[0].set_ylabel(self.translation.get_text("Total_Sales", self.langLocal), fontsize=12)
        axes[0].legend(title=self.translation.get_text("Subcategories", self.langLocal), 
                       bbox_to_anchor=(1.02, 1), loc='upper left')
        
         # -------------------------------------------------------------
        # Char 2: Box Plot - Price Distribution across Category & Subcategory
        # -------------------------------------------------------------
        print("Creating box plot...")
        # Set the Sales Value according to 'Full_Category' to sort the values for proper display in the boxplot
        df_sorted = data.sort_values("Category")
        sns.boxplot(
            ax=axes[1],
            data=df_sorted,
            x="Full_Category",  # 'Main Category -> Subcategory' 
            y="Price_Per_Unit", # Price distribution 
            hue="Category",     # Different colors for each main category
            palette="Set2"     # Use a different color palette for better distinction
        )
        axes[1].set_title(self.translation.get_text("Price_Distribution_by_Category_and_Subcategory", self.langLocal), fontsize=14, fontweight="bold")
        axes[1].set_xlabel(self.translation.get_text("Category", self.langLocal) + " -> " + self.translation.get_text("SubCategory", self.langLocal), fontsize=12)
        axes[1].set_ylabel(self.translation.get_text("Price_Per_Unit", self.langLocal), fontsize=12)

        # Rotate x-axis labels by 45 degrees so that text does not overlap and is clearly readable
        axes[1].set_xticklabels(axes[1].get_xticklabels(), rotation=45, ha="right")
        axes[1].legend(title=self.translation.get_text("Main_Categories", self.langLocal))

        # Adjust layout to prevent overlapping
        plt.tight_layout()
        # Save the figure to a file
        plt.savefig(os.path.join(self.chartsPath, f"sales_visualizations_{self.langLocal}.png"))
        # plt.show()       
            
    
    def revenueAndMonthlySalesTrend(self, data: pd.DataFrame ) -> None:
        """Create visual for
        <li> Category-wise Revenue (Bar Chart)</li>
        <li>Monthly Sales Trend (Line Chart)

        Args:
            data (pd.DataFrame): _description_
        """
        category_sales = data.groupby("Category")["Total_Sales"].sum().reset_index()
       # Create a large figure (Canvas) with 2 charts
        plt.figure(figsize=(10, 6))

        # Chart 1: Category-wise Revenue (Bar Chart)
        plt.subplot(1, 2, 1)
        sns.barplot(
            data=category_sales,
            x=self.translation.get_text("Category", self.langLocal),
            y=self.translation.get_text("Total_Sales", self.langLocal),
            palette=self.palette,
        )
        plt.title(self.translation.get_text("Revenue_by_Product_Category", self.langLocal), fontsize=14, fontweight="bold")
        plt.xlabel(self.translation.get_text("xlabel", self.langLocal), fontsize=12)
        plt.ylabel(self.translation.get_text("ylabel", self.langLocal), fontsize=12)

        # Chart 2: Monthly Sales Trend (Line Chart)
        monthly_sales = (
            data.groupby("Month")["Total_Sales"]
            .sum()
            .reindex(list(calendar.month_abbr)[1:]) #Abbreviated Month Names. For full month names, use list(calendar.month_name)[1:]
            .reset_index()
        )

        plt.subplot(1, 2, 2)
        sns.lineplot(
            data=monthly_sales,
            x="Month",
            y="Total_Sales",
            marker="o",
            linewidth=2.5,
            color="b",
        )
        
        plt.title(self.translation.get_text("Monthly_Sales_Trend", self.langLocal), fontsize=14, fontweight="bold")
        plt.xlabel(self.translation.get_text("xlabel", self.langLocal), fontsize=12)
        plt.ylabel(self.translation.get_text("ylabel", self.langLocal), fontsize=12)

        # Adjust layout to prevent overlapping
        plt.tight_layout()
        plt.savefig(os.path.join(self.chartsPath, f"sales_visualizations_category_{self.langLocal}.png"))
        print(f"Visualization saved as sales_visualizations_category_{self.langLocal}.png => " + self.langLocal)
        # Show the charts on the screen
        #plt.show()
        
    
if __name__ == "__main__" :
    # below import required in main only
    from sample_de.data.SalesDataCreator import SalesDataCreator
    from sample_de.clean.SalesDataCleaner import SalesDataCleaner
    from sample_de.process.SalesDataProcessor import SalesDataProcessor
     
    salesDataCreator = SalesDataCreator()
    data = salesDataCreator.create_data('data/sample_Stock_remove.csv')
    sdc = SalesDataCleaner()
    sdc.clean_data(data)
    sdp = SalesDataProcessor()
    sdp.process(data) 
    esdv = EcomSalesDataVisualizer()
    esdv.visualize(data)
           
        
