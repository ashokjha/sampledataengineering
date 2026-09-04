import os
import locale
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import calendar
import logging
from sample_de.utils.common_util import common_util
from sample_de.utils.translation import TranslationManager
from sample_de.utils.systemvariable import systemvariablemanager

class sales_and_revenue:
    """ Sales and Revenue visualization
    """
    def __init__(self, data):
        """  
        Args:
            data (_type_): : The processed DataFrame
        """
        self.data = data
        self.envreader = systemvariablemanager()
        self.langLocal = common_util.getLangLocal()
        self.reportTheme = os.environ.get("REPORT_THEME", "whitegrid")
        self.palette = os.environ.get("PALETTE","")
        self.translation = TranslationManager()
        self.chartsPath = common_util.getChartPath()
    
    def create_visualizations(self):
        """
        Create visualizations for the processed data.

        Args:
            df (pd.DataFrame): The processed DataFrame containing sales data.
        """

        # ---  Data Visualization ---
        logging.info("Visualizations (Creating Charts) ---")
        # setting: Charts to look nice set Seaborn style
        sns.set_theme(style=self.reportTheme)
        #Line and Box Chart
        fig, axes = plt.subplots(2, 1, figsize=(14, 12))

        # -------------------------------------------------------------
        # Chart 1: Line Chart - Monthly Sales Trend by Subcategory
        # -------------------------------------------------------------
        #Group the data by Month and Subcategory, summing the Total_Sales 
        trend_data = self.data.groupby(["Month", "Subcategory"])["Total_Sales"].sum().reset_index()
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
        df_sorted = self.data.sort_values("Category")
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

        # लेआउट को सुव्यवस्थित करें ताकि कोई भी टेक्स्ट आपस में न टकराए
        # correct the layout to correct sny cross cutting line(s)
        plt.tight_layout()
        # Save the figure to a file
        plt.savefig(os.path.join(self.chartsPath, f"sales_visualizations_{self.langLocal}.png"))
        # plt.show()



    def create_visualizations_category(self, category_sales):
        """
        Create visualizations for the processed data.
        Args:
            category_sales (pd.DataFrame): DataFrame containing category-wise sales data.
        """
        # ---Data Visualization ---
        logging.info("Visualizations (Creating Bar and Line Charts) ---")
        # setting: Charts to look nice set Seaborn style
        sns.set_theme(style=self.reportTheme)

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
            self.data.groupby("Month")["Total_Sales"]
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
 

if __name__ == "__main__":
    from dotenv import load_dotenv
    from sample_de.utils.create_data import sample_data_creator
    from sample_de.process.clean_data import clean_data
    from sample_de.process.process_data import process_data
    envreader = systemvariablemanager()
    # Example usage
    # Create a sample dataset for testing purposes
    dataCreator = sample_data_creator("Saless Data Creator")
    dataCreator.create_demo_sales_dataset(envreader.get_env(("DATASET"),90))
    #create_sample_dataset(os.getenv("DATASET"))
    # Clean the data
    print("Cleaning data from:", envreader.get_env(("DATASET")))
    cleanedDataSet = clean_data(envreader.get_env(("DATASET"))).clean()
    print("Cleaned data shape:", cleanedDataSet.shape)
    processData = process_data(cleanedDataSet)
    processeddataresult, categorysalesresult = processData.process_data_category()
    print("Processed data shape:", processeddataresult.shape)
    # Create visualizations
    salesAndRev = sales_and_revenue(processeddataresult)
    salesAndRev.create_visualizations()
    #salesAndRev.create_visualizations_category(categorysalesresult)
    print("Data loaded successfully. Here's a preview:")
    print(processeddataresult.head())
    