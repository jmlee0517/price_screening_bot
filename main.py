# main.py

from config.settings import THRESHOLD_WON
from data.fetcher import get_stock_list, get_price_data
from strategy.ma10_breakout import check_breakout

def main():
    print("Starting MA10 Breakout Scanner...")

    # Load stock listings from local CSV
    stock_df = get_stock_list()

    breakout_stocks = []

    # Loop through all stocks
    for _, row in stock_df.iterrows():
        symbol = str(row['Code']).zfill(6)  # Ensure 6-digit code
        name = row['Name']

        try:
            # Fetch price data
            price_df = get_price_data(symbol)
            
            # Check breakout
            result = check_breakout(symbol, price_df, THRESHOLD_WON)

            if result:
                result["name"] = name
                breakout_stocks.append(result)
                print(f"BUY SIGNAL: {name} ({symbol}) | Close: {result['close']} | MA10: {result['ma10']} | Diff: {result['difference']}")

        except Exception as e:
            print(f"Error processing {symbol} ({name}): {e}")

    # Final summary
    print("\n=== FINAL BREAKOUT LIST ===")
    for stock in breakout_stocks:
        print(f"{stock['name']} ({stock['symbol']}): Close={stock['close']}, MA10={stock['ma10']}, Diff={stock['difference']}")

if __name__ == "__main__":
    main()