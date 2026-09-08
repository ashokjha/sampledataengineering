import os
import matplotlib.pyplot as plt


class PdfExporter:

    def save_static_charts_to_pdf(
        self, figures_dict, reportLocation="generated"
    ) -> list:
        """
        Saves multiple Matplotlib/Seaborn figure objects into single-page PDFs.

        Parameters:
        - figures_dict: A dictionary mapping names to matplotlib figure items
                        e.g., {"histogram": fig1, "boxplot": fig2}
        """
        if not os.path.exists(reportLocation):
            os.makedirs(reportLocation)

        saved_paths = []

        for chart_name, fig in figures_dict.items():
            file_path = os.path.join(reportLocation, f"{chart_name}_static.pdf")

            # Save figure with tight layout to avoid clipping edges
            fig.savefig(file_path, format="pdf", bbox_inches="tight", dpi=300)
            saved_paths.append(file_path)

        return saved_paths

    def save_interactive_charts_to_pdf(self, figures_dict, reportLocation) -> list:
        """
        Converts Plotly figures into vector PDF files using the kaleido engine.

        Parameters:
        - figures_dict: A dictionary mapping names to Plotly figure items
        """
        if not os.path.exists(reportLocation):
            os.makedirs(reportLocation)

        saved_paths = []

        for chart_name, fig in figures_dict.items():
            file_path = os.path.join(reportLocation, f"{chart_name}_interactive.pdf")

            # Write image payload as a scalable vector PDF file
            # fig.write_image(file_path, format="pdf", engine="kaleido")
            fig.write_image(file_path, format="pdf")
            saved_paths.append(file_path)

        return saved_paths

    def convert_pdf(self, reports: list[dict], reportLocation: str) -> list:
        saved_paths = []
        for chart in reports:
            file_path = os.path.join(reportLocation, f"{chart['name']}_static.pdf")
            chart["static"].savefig(
                file_path, format="pdf", bbox_inches="tight", dpi=300
            )
            saved_paths.append(file_path)
            file_path = os.path.join(reportLocation, f"{chart['name']}_interactive.pdf")

            chart["interactive"].write_image(file_path, format="pdf")
            saved_paths.append(file_path)
        return saved_paths
