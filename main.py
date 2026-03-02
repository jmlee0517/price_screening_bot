from config.settings import THRESHOLD_WON, MARKET_LIST
from data.fetcher import get_stock_list, get_price_data
from strategy.ma10_breakout import check_breakout

def main():
    print("Starting MA10 Breakout Scanner...")

    stock_df = get_stock_list()

    breakout_stocks = []

    for _, row in stock_df.iterrows():
            symbol = row['Code']
            name = row['Name']

            try:
                price_df = get_price_data(symbol)
                result = check_breakout(symbol, price_df, THRESHOLD_WON)

                if result:
                    result["name"] = name
                    breakout_stocks.append(result)
                    print(f"BUY SIGNAL: {name} ({symbol})")

            except Exception as e:
                print(f"Error processing {symbol}: {e}")

    print("\n=== FINAL RESULT ===")
    for stock in breakout_stocks:
        print(stock)


if __name__ == "__main__":
    main()