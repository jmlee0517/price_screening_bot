def check_breakout(symbol, daily_df, market_cap, threshold):
    """
    MA10 Breakout + Volume + Price Range Filter
    """

    from indicators.moving_average import calculate_10_month_ma

    if daily_df.empty:
        return None

    # --- MA10 ---
    monthly, ma10 = calculate_10_month_ma(daily_df)

    if ma10.isna().iloc[-1]:
        return None

    latest_close = daily_df['Close'].iloc[-1]
    latest_ma10 = ma10.iloc[-1]
    latest_volume = daily_df['Volume'].iloc[-1]

    difference = latest_close - latest_ma10

    # --- Filters ---
    if (
        0 < difference <= threshold and
        latest_volume >= 1_000_000 and
        2000 < latest_close < 150000 and
        market_cap >= 2_000_000_000_000
    ):
        return {
            "symbol": symbol,
            "close": latest_close,
            "ma10": latest_ma10,
            "volume": latest_volume,
            "difference": difference,
            "market_cap": market_cap
        }

    return None