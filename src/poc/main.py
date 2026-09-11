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
            match (self.view_mode):
                case DisplayMode.BOTH:
                    match (self.category):
                        case ChartType.FINANCIAL:
                            st.plotly_chart(chart["interactive"], width="stretch")
                        case __:
                            col1, col2 = st.columns(2)
                            with col1:
                                if hasattr(chart["static"], "savefig") == True:
                                    st.pyplot(chart["static"])
                                else:
                                    st.plotly_chart(chart["static"], width="stretch")
                            with col2:
                                st.plotly_chart(chart["interactive"], width="stretch")

                case DisplayMode.INTERCTIVE:
                    st.plotly_chart(chart["interactive"], width="stretch")

                case __:
                    match (self.category):
                        case ChartType.FINANCIAL:
                            st.plotly_chart(chart["interactive"], width="stretch")
                        case __:
                            if hasattr(chart["static"], "savefig") == True:
                                st.pyplot(chart["static"])
                            else:
                                st.plotly_chart(chart["static"], width="stretch")

            st.divider()

    def createDashboard(self):
        load_dotenv()
        # 1. UI theme setup
        st.set_page_config(layout="wide", page_title="Chart Vault")
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

        # download Report
        exporter = PdfExporter()
        reportPath = os.path.join(
            os.getenv("PDFREPORT", "generated"),
            self.category.replace("Engine", "").strip().replace(" ", "_"),
        )
        if not os.path.exists(reportPath):
            os.makedirs(reportPath)
        if st.sidebar.button("Export All Charts to PDF"):
            Loader.show_top_loader()
            with st.empty(), st.spinner("Generating PDF vectors..."):
                createReports = exporter.convert_pdf(self.active_charts, reportPath)
                print(f"Reports : \n {createReports} \n created successfully")


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.createDashboard()
