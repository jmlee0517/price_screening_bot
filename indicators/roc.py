def calculate_roc(close_series, period):
    """
    Calculate Rate of Change (ROC)

    ROC = (Current Price / Price N periods ago - 1) * 100
    """
    roc = (close_series / close_series.shift(period) - 1) * 100
    return roc