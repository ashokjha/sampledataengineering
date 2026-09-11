import os
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import streamlit as st

from poc.modules.chartEngine import BaseChartEngine
from poc import DataConfigEngine


class FinancialEngine(BaseChartEngine):
    """
    Pure Plotly-based Financial Chart Engine that handles both interactive dashboard
    rendering and static report image generation with an all-black terminal UI.
    """

    def __init__(self):
        self.plotly_template = "plotly_dark"
        self.bg_color = "#000000"  # Pure Black Background
        self.grid_color = "#222222"  # Dark Grey Gridlines
        self.period = "4mo"
        self.interval = "1wk"
        self.ticker_symbol = "^NSEI"
        self.external_context = {
            "ticker": self.ticker_symbol,
            "interval": self.interval,
            "period": self.period,
        }
        self.dce = DataConfigEngine()
        self.data = self.dce.fetchData("Financial", self.external_context)
        self.charts = []

    def render_all(self) -> list[dict]:
        # save_path = f"charts/{self.ticker_symbol}_static_chart.png"
        # fig_s1, save_path = self.render_static(
        #    save_path=save_path, title=f"{self.ticker_symbol} - Static View"
        # )

        fig_i1 = self.render_interactive(title=f"{self.ticker_symbol} - Market Analsis")
        title = f"Market Analysis of {self.ticker_symbol} [Interval: {self.interval}, period: {self.period}]"
        name = f"Market Analysis of {self.ticker_symbol}_{self.interval}_{self.period}"
        self.charts.append(
            {
                "title": title,
                "interactive": fig_i1,
                "name": name,
            }
        )
        return self.charts

    def _generate_plotly_figure(
        self, title: str, show_volume: bool, moving_averages: tuple
    ) -> go.Figure:
        """
        Create both static and interactive।
        """
        fig = make_subplots(
            rows=2,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0.06,
            subplot_titles=(title, "Volume Metrics"),
            row_width=[0.3, 0.7],
        )

        # 1. Candlestick Trace (Modern Terminal Green & Red)
        fig.add_trace(
            go.Candlestick(
                x=self.data.index,
                open=self.data["Open"],
                high=self.data["High"],
                low=self.data["Low"],
                close=self.data["Close"],
                name="OHLC",
                increasing_line_color="#26a69a",
                decreasing_line_color="#ef5350",
            ),
            row=1,
            col=1,
        )

        # 2. Moving Averages
        for ma in moving_averages:
            if len(self.data) >= ma:
                ma_series = self.data["Close"].rolling(window=ma).mean()
                fig.add_trace(
                    go.Scatter(
                        x=self.data.index,
                        y=ma_series,
                        name=f"SMA {ma}",
                        line=dict(width=1.5),
                    ),
                    row=1,
                    col=1,
                )

        # 3. Volume Trace
        if show_volume and "Volume" in self.data.columns:
            volume_colors = [
                "#26a69a" if c >= o else "#ef5350"
                for o, c in zip(self.data["Open"], self.data["Close"])
            ]
            fig.add_trace(
                go.Bar(
                    x=self.data.index,
                    y=self.data["Volume"],
                    name="Volume",
                    marker_color=volume_colors,
                    opacity=0.8,
                ),
                row=2,
                col=1,
            )

        # 4. Pure Black Layout Customization
        fig.update_layout(
            template=self.plotly_template,
            paper_bgcolor=self.bg_color,
            plot_bgcolor=self.bg_color,
            xaxis_rangeslider_visible=False,
            margin=dict(t=60, b=30, l=30, r=30),
            height=600,
            showlegend=True,
        )

        # Customize the grid
        fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor=self.grid_color)
        fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor=self.grid_color)

        return fig

    def render_interactive(self, **kwargs) -> go.Figure:
        title = kwargs.get("title", "Market Analytics (Interactive View)")
        show_volume = kwargs.get("volume", True)
        moving_averages = kwargs.get("mav", (5, 20))

        return self._generate_plotly_figure(title, show_volume, moving_averages)

    def render_static(self, save_path: str = None, **kwargs) -> tuple[go.Figure, str]:
        title = kwargs.get("title", "Market Analytics (Static Blueprint View)")
        show_volume = kwargs.get("volume", True)
        moving_averages = kwargs.get("mav", (5, 20))

        fig = self._generate_plotly_figure(title, show_volume, moving_averages)

        if not save_path:
            save_path = "charts/financial_static_chart.png"

        os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)

        fig.write_image(save_path, scale=2)
        # st.image(save_path, use_container_width=True)
        # return save_path
        return fig, save_path


if __name__ == "__main__":
    fe = FinancialEngine()
    fe.render_all()
