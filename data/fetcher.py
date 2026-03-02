import pandas as pd
from datetime import datetime, timedelta
import FinanceDataReader as fdr

CACHE_PATH = "data/krx_listing.csv"

def get_stock_list():
    """Load stock listings from local CSV"""
    return pd.read_csv(CACHE_PATH)

def get_price_data(symbol, years=3):
    """Fetch daily OHLCV data for a stock"""
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365 * years)
    df = fdr.DataReader(symbol, start_date, end_date)
    return df