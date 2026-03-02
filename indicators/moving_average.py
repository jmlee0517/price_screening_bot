import pandas as pd

def calculate_10_month_ma(daily_df):
    """
    Convert daily data to monthly close and calculate 10-month MA.
    """
    if daily_df.empty:
        return None

    monthly = daily_df['Close'].resample('M').last()
    ma10 = monthly.rolling(window=10).mean()

    return monthly, ma10