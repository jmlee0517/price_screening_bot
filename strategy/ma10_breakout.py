def check_breakout(symbol, daily_df, threshold):
    """
    Check if latest close has surpassed 10-month MA + threshold.
    """
    from indicators.moving_average import calculate_10_month_ma

    if daily_df.empty:
        return None

    monthly, ma10 = calculate_10_month_ma(daily_df)

    if ma10.isna().iloc[-1]:
        return None  # not enough data

    latest_close = daily_df['Close'].iloc[-1]
    latest_ma10 = ma10.iloc[-1]

    difference = latest_close - latest_ma10

    if 0 < difference <= threshold:
        return {
            "symbol": symbol,
            "close": latest_close,
            "ma10": latest_ma10,
            "difference": difference
        }

    return None