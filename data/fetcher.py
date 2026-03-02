import FinanceDataReader as fdr
import pandas as pd
import os
import time
from datetime import datetime, timedelta

CACHE_PATH = "data/krx_listing.csv"
REFRESH_DAYS = 7


def get_stock_list():
    """
    Load KRX listing from local cache.
    Auto-refresh if older than REFRESH_DAYS.
    """
    if os.path.exists(CACHE_PATH):
        modified_time = datetime.fromtimestamp(os.path.getmtime(CACHE_PATH))
        if datetime.now() - modified_time < timedelta(days=REFRESH_DAYS):
            print("Loading stock list from local cache...")
            return pd.read_csv(CACHE_PATH)

    print("Downloading fresh KRX listing...")
    df = fdr.StockListing("KRX")
    time.sleep(1)
    df.to_csv(CACHE_PATH, index=False)

    return df


def get_price_data(symbol, years=3):
    """
    Fetch daily OHLCV data for a stock.
    """
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365 * years)

    df = fdr.DataReader(symbol, start_date, end_date)
    return df