# main.py
import os
import pandas as pd
from datetime import datetime
from config.settings import THRESHOLD_WON
from data.fetcher import get_stock_list, get_price_data
from strategy.ma10_breakout import check_breakout

def main():
    buySignals = []
    print("Starting MA10 + Volume + Price Filter Scanner...")

    stock_df = get_stock_list()

    found_signal = False

    for _, row in stock_df.iterrows():
        symbol = str(row['Code']).zfill(6)
        name = row['Name']
        market_cap = int(str(row['MarketCap']).replace(",", ""))

        try:
            price_df = get_price_data(symbol)
            result = check_breakout(symbol, price_df, market_cap, THRESHOLD_WON)

            if result:
                buySignals.append({
                    "Name": name,
                    "Symbol": symbol,
                    "Close": result["close"],
                    "MA10": result["ma10"],
                    "Difference": result["difference"],
                    "Volume": result["volume"],
                    "MarketCap": result["market_cap"]
                })

                print(
                    f"BUY SIGNAL: {name} ({symbol}) | "
                    f"Close: {result['close']} | "
                    f"MA10: {result['ma10']} | "
                    f"Diff: {result['difference']:.2f} | "
                    f"Volume: {result['volume']:,}"
                )

        except Exception as e:
            print(f"Error processing {symbol} ({name}): {e}")

    if not buySignals:
        print("No stocks found matching the criteria.")
    else:
        df_buySignals = pd.DataFrame(buySignals)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        timestamp = datetime.now().strftime("%Y-%m-%d")
        filename = f"screened_results_{timestamp}.csv"

        output_path = os.path.join(base_dir, "results", filename)
        
        df_buySignals.to_csv(output_path, index=False)

        print(f"\nTotal Signals Found: {len(buySignals)}")
        print("Results saved to the results folder.")

if __name__ == "__main__":
    main()