import yfinance as yf
import pandas as pd
import numpy as np

ticker = "QUAL"  
start_date = "2019-01-01"
end_date = "2024-12-31"


risk_free_by_year = {
    2019: 0.023,
    2020: 0.009,
    2021: 0.001,
    2022: 0.018,
    2023: 0.045,
    2024: 0.0469
}


df = yf.download(ticker, start=start_date, end=end_date, interval="1d", auto_adjust=True, progress=False)

if df.empty:
    print(" Données indisponibles pour", ticker)
else:
    df = df.resample("M").last()
    returns = df["Close"].pct_change().dropna()

    sharpe_by_year = {}
    for year in range(2019, 2025):
        r = returns[returns.index.year == year]
        if len(r) >= 6:
            avg_r = r.mean() * 12
            std_r = r.std() * np.sqrt(12)
            rf = risk_free_by_year[year]
            sharpe = (avg_r - rf) / std_r
            sharpe_by_year[year] = round(sharpe, 3)

    print(f"Ratio de Sharpe annuel pour {ticker} :")
    print(pd.Series(sharpe_by_year))
