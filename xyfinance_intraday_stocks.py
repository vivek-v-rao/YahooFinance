""" get historical intraday stock data from Yahoo Finance """
import time
t0 = time.time()
import os
from datetime import date, timedelta
import yfinance as yf

today_str = date.today().strftime("%Y%m%d")
print(today_str) 

print("program:", os.path.basename(__file__))
ndays_prior = 58 # of days of 5-minute data you can get from Yahoo is limited
start = (date.today() - timedelta(days=ndays_prior)).strftime("%Y-%m-%d")
end = None

interval = "5m" # can be "1m"
print("start:", start)
print("end:", end)
print("interval:", interval)
if interval == "1m":
    out_dir = os.path.join("stocks", "1_minute_prices", today_str)
    os.makedirs(out_dir, exist_ok=True)
    period = "5d"
    start = None
    end = None
elif interval == "5m":
    out_dir = os.path.join("stocks", "5_minute_prices",today_str)
    os.makedirs(out_dir, exist_ok=True)
    period = "max"
print("period:", period)
dict_num_obs = {}
ticker_file = "etf_symbols.txt"
max_sym = None
symbols = open(ticker_file, "r").readlines()
symbols = [symbol.strip() for symbol in symbols][:max_sym]
for symbol in symbols:
    xx = yf.Ticker(symbol)
    df_prices = xx.history(period=period, interval=interval,
        start=start, end=end)
    nobs = df_prices.shape[0]
    dict_num_obs[symbol] = nobs
    print("\nsymbol, #obs =", symbol, nobs)
    if nobs > 0:
        print(df_prices.iloc[[0, -1], :].to_string())
        df_prices.to_csv(os.path.join(out_dir, symbol + ".csv"))

print("\n%12s"%"symbol", "%8s"%"#obs")
for symbol, nobs in dict_num_obs.items():
    print("%12s"%symbol, "%8d"%nobs)
    
print("\n#symbols:", len(dict_num_obs))
print("wrote to", out_dir)
print("time elapsed (s):", "%0.2f"%(time.time() - t0))
