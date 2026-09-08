import os
import streamlit as st
from dotenv import load_dotenv


from poc.modules.enum.ChartEnum import ChartType, DisplayMode

from poc.modules.router.EngineRouter import get_engine_router
from poc.exporter.PdfExporter import PdfExporter
from poc.modules.loader.WIP import Loader


class Dashboard:
    def __init__(self):
        pass

    def createDashboard(self):
        load_dotenv()
        # 1. UI theme setup
        st.set_page_config(layout="wide", page_title="Chart Vault")
        st.title("🧱 Dynamic Routed Chart Vault")

        # 2. sidebar Category Selection
        st.sidebar.header("🗂️ Main Categories")
        category = st.sidebar.selectbox(
            "Select Category",
            [
                ChartType.DISTRIBUTION.value,
                ChartType.RELATIONAL.value,
                ChartType.CATEGORIOCAL.value,
                ChartType.THREED.value,
                ChartType.MATRIX.value,
                ChartType.PART2WHOLE.value,
                ChartType.GEO.value,
            ],
        )
        view_mode = st.sidebar.radio(
            "Display Mode",
            [
                DisplayMode.BOTH.value,
                DisplayMode.INTERCTIVE.value,
                DisplayMode.STATIC.value,
            ],
        )

        # 3. Routing
        engine = get_engine_router(category)

        # Active Charts
        active_charts = engine.render_all()

        for index, chart in enumerate(active_charts):
            st.header(f"{index + 1}. {chart['title']}")
            if view_mode == "Side-by-Side":
                col1, col2 = st.columns(2)
                with col1:
                    st.pyplot(chart["static"])
                with col2:
                    st.plotly_chart(chart["interactive"], use_container_width=True)
            elif view_mode == "Interactive Only":
                st.plotly_chart(chart["interactive"], use_container_width=True)
            else:
                st.pyplot(chart["static"])

            st.divider()
        # download Report
        exporter = PdfExporter()
        reportPath = os.path.join(
            os.getenv("PDFREPORT", "generated"),
            category.replace("Engine", "").strip().replace(" ", "_"),
        )
        if not os.path.exists(reportPath):
            os.makedirs(reportPath)
        if st.sidebar.button("Export All Charts to PDF"):
            Loader.show_top_loader()
            with st.empty(), st.spinner("Generating PDF vectors..."):
                createReports = exporter.convert_pdf(active_charts, reportPath)
                print(f"Reports : \n {createReports} \n created successfully")


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.createDashboard()
