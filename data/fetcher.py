import pandas as pd
from datetime import datetime, timedelta
import FinanceDataReader as fdr

STOCK_CACHE_PATH = "data/krx_listing.csv"
ETF_CACHE_PATH = "data/krx_etf_listing.csv"

def get_stock_list():
    """Load stock listings from local CSV"""
    return pd.read_csv(STOCK_CACHE_PATH)

def get_etf_list():
    """Load ETF listing from local CSV"""
    return pd.read_csv(ETF_CACHE_PATH)

def get_universe(include_krx=True, include_etf=True):
    dfs=[]

    if include_krx:
        dfs.append(get_stock_list())

    if include_etf:
        dfs.append(get_etf_list())

    if not dfs:
        raise ValueError("At least one of INCLUDE_KRX or INCLUDE_ETF must be True")
    
    return pd.concat(dfs, ignore_index=True)

def get_price_data(symbol, years=3):
    """Fetch daily OHLCV data for a stock"""
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365 * years)
    df = fdr.DataReader(symbol, start_date, end_date)
    return df