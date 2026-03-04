# main.py

from config.settings import THRESHOLD_WON
from data.fetcher import get_stock_list, get_price_data
from strategy.ma10_breakout import check_breakout

def main():
    print("Starting MA10 + Volume + Price Filter Scanner...")

    stock_df = get_stock_list()

    found_signal = False

    signal_count = 0

    for _, row in stock_df.iterrows():
        symbol = str(row['Code']).zfill(6)
        name = row['Name']
        market_cap = int(str(row['MarketCap']).replace(",", ""))

        try:
            price_df = get_price_data(symbol)
            result = check_breakout(symbol, price_df, market_cap, THRESHOLD_WON)

            if result:
                signal_count += 1

                print(
                    f"BUY SIGNAL: {name} ({symbol}) | "
                    f"Close: {result['close']} | "
                    f"MA10: {result['ma10']} | "
                    f"Diff: {result['difference']:.2f} | "
                    f"Volume: {result['volume']:,}"
                )

        except Exception as e:
            print(f"Error processing {symbol} ({name}): {e}")

    if signal_count == 0:
        print("No stocks found matching the criteria.")
    else:
        print(f"\nTotal signals found: {signal_count}")

if __name__ == "__main__":
    main()