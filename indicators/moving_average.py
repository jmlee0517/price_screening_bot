import pandas as pd

def calculate_10_month_ma(daily_df):
    """
    Convert daily data to monthly close and calculate 10-month MA.
    """

    if daily_df.empty:
        return None

    # Use 'ME' for month-end instead of 'M'
    monthly = daily_df['Close'].resample('ME').last()

    ma10 = monthly.rolling(window=10).mean()

    return monthly, ma10