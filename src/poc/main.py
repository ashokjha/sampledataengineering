import os
import streamlit as st
from dotenv import load_dotenv


from poc.modules.enum.ChartEnum import ChartType, DisplayMode

from poc.modules.chartEngine import get_chart_engine
from poc.exporter import PdfExporter
from poc.modules.loader import Loader


class Dashboard:
    def __init__(self):
        self.active_charts = {}
        self.view_mode = None
        self.category = None

    def display(self):
        for index, chart in enumerate(self.active_charts):
            st.header(f"{index + 1}. {chart['title']}")
            static_chart = chart.get("static")
            interactive_chart = chart.get("interactive")
            is_static = static_chart is not None
            is_interactive = interactive_chart is not None
            is_static_savefig = is_static and hasattr(static_chart, "savefig")
            match self.view_mode:
                case DisplayMode.BOTH:
                    if is_static and is_interactive:
                        col1, col2 = st.columns(2)
                        with col1:
                            self.displayChart(static_chart, is_static_savefig)
                        with col2:
                            self.displayChart(interactive_chart)
                    else:
                        chart_obj = (
                            static_chart
                            if is_static
                            else interactive_chart if is_interactive else None
                        )
                        if chart_obj is not None:
                            self.displayChart(chart_obj)
                case DisplayMode.INTERCTIVE:
                    self.displayChart(interactive_chart)
                case __:
                    chart_obj = (
                        static_chart
                        if is_static
                        else interactive_chart if is_interactive else None
                    )
                    if chart_obj is not None:
                        self.displayChart(chart_obj, is_static_savefig)
            st.divider()

    def displayChart(self, chartObj, isSavefig=False):
        if isSavefig:
            st.pyplot(chartObj)
        else:
            st.plotly_chart(chartObj, width="stretch")

    def downloadReport(self):
        # download Report
        exporter = PdfExporter()
        reportPath = os.path.join(
            os.getenv("PDFREPORT", "generated"),
            self.category.replace("Engine", "").strip().replace(" ", "_"),
        )
        print(f"Reportpath={reportPath}")
        if not os.path.exists(reportPath):
            os.makedirs(reportPath)
        if st.sidebar.button("Export All Charts to PDF"):
            Loader.show_top_loader()
            with st.empty(), st.spinner("Generating PDF vectors..."):
                reports = exporter.convert_pdf(self.active_charts, reportPath)
                return reports

    def createDashboard(self):
        load_dotenv()
        # 1. UI theme setup
        st.set_page_config(layout="wide", page_title="Python Chart Vault")
        st.title("🧱 Dynamic Routed Chart Vault")

        # 2. sidebar Category Selection
        st.sidebar.header("🗂️ Main Categories")
        self.category = st.sidebar.selectbox(
            "Select Category",
            [
                ChartType.DISTRIBUTION.value,
                ChartType.RELATIONAL.value,
                ChartType.CATEGORIOCAL.value,
                ChartType.THREED.value,
                ChartType.MATRIX.value,
                ChartType.PART2WHOLE.value,
                ChartType.GEO.value,
                ChartType.FINANCIAL.value,
            ],
        )
        self.view_mode = st.sidebar.radio(
            "Display Mode",
            [
                DisplayMode.BOTH.value,
                DisplayMode.INTERCTIVE.value,
                DisplayMode.STATIC.value,
            ],
        )

        # 3. Routing
        engine = get_chart_engine(self.category)

        # Active Charts
        self.active_charts = engine.render_all()

        # Display
        self.display()
        # dowload Reports
        reports = self.downloadReport()
        if reports:
            print(f"Reports : \n {reports} \n")


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.createDashboard()
