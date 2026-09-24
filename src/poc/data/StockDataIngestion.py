# poc/modules/chartEngine/StockDataIngestion.py
import os
import yfinance as yf
import pandas as pd
import logging
from dotenv import load_dotenv
from typing import Final

logger = logging.getLogger("StockDataIngestion")


class StockDataIngestion:
    """
    Service to fetch and validate financial market data using yfinance.
    """

    load_dotenv()
    DATA_PATH: Final = os.environ.get("POCSAMPLEDATA", "data/tmp") + "/Financial"
    os.makedirs(DATA_PATH, exist_ok=True)

    @staticmethod
    def fetch_ticker_data(
        ticker: str, period: str = "3mo", interval: str = "1d"
    ) -> pd.DataFrame:
        """
        downloads from yfinance set index to DatetimeIndex
        period: '1mo', '3mo', '1y', 'ytd'
        interval: '1d', '1h', '5m'
        """
        logger.info(
            f"Fetching data for ticker: {ticker} (Period: {period}, Interval: {interval})"
        )

        try:
            df = yf.download(ticker, period=period, interval=interval)

            if df.empty:
                raise ValueError(
                    f"No data returned for ticker '{ticker}'. Please check the symbol."
                )

            required_cols = ["Open", "High", "Low", "Close", "Volume"]
            if not all(col in df.columns for col in required_cols):
                raise KeyError(
                    f"Missing required financial columns in fetched data. Expected: {required_cols}"
                )

            df.index = pd.to_datetime(df.index)
            df.index.name = "Date"

            # 1. Flatten the MultiIndex if it exists
            if isinstance(df.columns, pd.MultiIndex):
                # df.columns = df.columns.droplevel(1)  # Drops the '^NSEI' ticker level'
                df.columns = df.columns.get_level_values(0)
            # 2. Force every column to be a float
            df = df.astype(float)

            df.to_csv(f"{StockDataIngestion.DATA_PATH}/stockdata.csv")
            logger.info(f"Successfully ingested {len(df)} rows of data for {ticker}.")
            return df

        except Exception as e:
            logger.error(f"Failed to fetch data from yfinance: {str(e)}")
            raise e
