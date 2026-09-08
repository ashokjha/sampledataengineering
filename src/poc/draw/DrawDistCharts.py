import os
import ast
from dotenv import load_dotenv
import streamlit as st
from poc.modules.chartEngine.DistributionEngine import Distribution
from poc.exporter.PdfExporter import PdfExporter


class DrawDistCharts:
    load_dotenv()

    def __init__(self):
        self.dist = Distribution()
        self.__exporter = PdfExporter()
        self.__fig_stat_hist = None
        self.__fig_int_hist = None
        self.__fig_stat_box = None
        self.__fig_int_box = None
        self.__fig_stat_vio = None
        self.__fig_int_vio = None
        self.__fig_stat_hist = None
        self.__fig_stat_dens = None
        self.__fig_int_dens = None
        self.__fig_stat_swarm = None
        self.__fig_int_swarm = None
        self.__fig_stat_err = None
        self.__fig_int_err = None

        self.__view_mode = st.sidebar.radio(
            "Dashboard View Mode",
            ["Show Side-by-Side", "Interactive Only", "Static Only"],
        )
        self.__chart_category = st.sidebar.selectbox(
            "Select Category", ast.literal_eval(os.getenv("CHART_CATEGORY", "[]"))
        )

    def draw(self):
        # Set layout
        st.set_page_config(layout="wide", page_title="Python Chart Vault")
        st.title("📊 Python Ultimate Chart Vault")
        st.write(
            "Displaying both **Static (Matplotlib/Seaborn)** and **Interactive (Plotly)** engines."
        )

        # Load data
        df = self.dist.get_sample_data()
        self.__fig_stat_hist, self.__fig_int_hist = self.dist.render_histogram(
            df, "Value"
        )
        self.__fig_stat_box, self.__fig_int_box = self.dist.render_boxplot(
            df, "Category", "Value"
        )
        self.__fig_stat_vio, self.__fig_int_vio = self.dist.render_violinplot(
            df, "Category", "Value"
        )
        self.__fig_stat_dens, self.__fig_int_dens = self.dist.render_density_plot(
            df, "Value"
        )
        self.__fig_stat_swarm, self.__fig_int_swarm = self.dist.render_swarm_plot(
            df, "Category", "Value"
        )
        self.__fig_stat_err, self.__fig_int_err = self.dist.render_error_bar_chart(
            df, "Category", "Value"
        )

        # Sidebar controls
        st.sidebar.header("Navigation")

        # --- PDF Export Action Center ---
        st.sidebar.markdown("---")
        st.sidebar.header("📥 Export Center")

        if st.sidebar.button("Export All Charts to PDF"):
            self.__export()

        match self.__chart_category:
            case "Statistical & Distribution":
                self.__statisticalDist(df)

    def __statisticalDist(self, df):
        # --- CHART 1: HISTOGRAM ---
        st.header("1. Statistical & Distribution Charts")
        # Helper structure to loop dashboard blocks cleanly
        chart_blocks = self.__getDistchartBlocks()
        # Render
        for block in chart_blocks:
            st.subheader(block["title"])
            if self.__view_mode == "Show Side-by-Side":
                col1, col2 = st.columns(2)
                with col1:
                    st.pyplot(block["static"])
                with col2:
                    st.plotly_chart(block["interactive"], use_container_width=True)
            elif self.__view_mode == "Interactive Only":
                st.plotly_chart(block["interactive"], use_container_width=True)
            else:
                st.pyplot(block["static"])
            st.divider()

    def __getDistchartBlocks(self) -> list[dict]:
        """List of dictionary of chart block

        Returns:
            List: List of Dictionary of chart block
        """
        chart_blocks = [
            {
                "title": "Histogram & Density (KDE)",
                "static": self.__fig_stat_hist,
                "interactive": self.__fig_int_hist,
            },
            {
                "title": "Box Plot (Outlier & Quartiles)",
                "static": self.__fig_stat_box,
                "interactive": self.__fig_int_box,
            },
            {
                "title": "Violin Plot (Probability Density Distribution)",
                "static": self.__fig_stat_vio,
                "interactive": self.__fig_int_vio,
            },
            {
                "title": "Density Plot (Continuous Data Shape)",
                "static": self.__fig_stat_dens,
                "interactive": self.__fig_int_dens,
            },
            {
                "title": "Strip / Swarm Plot (Individual Data Points)",
                "static": self.__fig_stat_swarm,
                "interactive": self.__fig_int_swarm,
            },
            {
                "title": "Error Bar Chart (Statistical Variances & Means)",
                "static": self.__fig_stat_err,
                "interactive": self.__fig_int_err,
            },
        ]
        return chart_blocks

    def __export(self):
        """
        export report in PDF
        """
        with st.spinner("Generating PDF vectors..."):
            # Compile asset dictionaries
            static_bundle = {
                "1_histogram": self.__fig_stat_hist,
                "2_boxplot": self.__fig_stat_box,
                "3_violinplot": self.__fig_stat_vio,
                "4_density": self.__fig_stat_dens,
                "5_stripplot": self.__fig_stat_swarm,
                "6_errorbar": self.__fig_stat_err,
            }

            interactive_bundle = {
                "1_histogram": self.__fig_int_hist,
                "2_boxplot": self.__fig_int_box,
                "3_violinplot": self.__fig_int_vio,
                "4_density": self.__fig_int_dens,
                "5_stripplot": self.__fig_int_swarm,
                "6_errorbar": self.__fig_int_err,
            }

            # Run exporter modules
            reportPath = os.path.join(
                os.getenv("PDFREPORT", "generated"), "distribution"
            )
            if not os.path.exists(reportPath):
                os.makedirs(reportPath)
            saved_static = self.__exporter.save_static_charts_to_pdf(
                static_bundle, reportPath
            )
            saved_inter = self.__exporter.save_interactive_charts_to_pdf(
                interactive_bundle, reportPath
            )
            st.sidebar.success(
                f"Saved {len(saved_static) + len(saved_inter)} PDF documents into your '/'/{reportPath}'' directory!"
            )
