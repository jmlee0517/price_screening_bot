📈 **KRX MA10 Breakout Screening Bot**
A configurable quantitative stock & ETF screening engine for the Korean market (KRX).

This project scans KRX stocks and ETFs using a 10-Month Moving Average breakout strategy combined with liquidity, price, and market capitalization filters.

🚀 **Strategy Overview**
The scanner identifies instruments that satisfy:

1️⃣ MA10 Breakout
	•	Latest closing price is above the 10-month moving average.
	•	Breakout threshold configurable (THRESHOLD_WON).

2️⃣ Liquidity Filter
	•	Daily trading volume ≥ MIN_VOLUME

3️⃣ Price Range Filter
	•	MIN_PRICE < Close < MAX_PRICE

4️⃣ Market Capitalization Filter
	•	Market cap ≥ MIN_MARKET_CAP

All parameters are configurable via settings.py.

📂 **Project Structure**
price_screening_bot/
│
├── main.py                 # Entry point
├── config/
│   ├── settings.py               # Strategy & universe configuration
│
├── data/
│   ├── fetcher.py          # Data loading layer
│   ├── krx_listing.csv
│   └── krx_etf_listing.csv
│
├── indicators/
│   └── moving_average.py   # MA10 calculation
│
├── strategy/
│   └── ma10_breakout.py         #logic
│
├── utils/
│   └── market_utils.py         #market availability
│
└── results/                # Output CSV files

📊 **Data Source**
	•	Market data fetched using FinanceDataReader
	•	Stock & ETF listing data loaded from locally cached KRX CSV files

Daily OHLCV price data is dynamically downloaded.

▶️ **How To Run**

Activate virtual environment:

source venv/bin/activate

Run scanner:

python main.py
