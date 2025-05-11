import pandas as pd
import numpy as np
import yfinance as yf


lrgf_liquid = pd.read_csv('LRGF_liquid_filtered.csv')


tickers = lrgf_liquid['Ticker'].tolist()
price_data = yf.download(tickers, start='2019-01-01', end='2024-12-31', group_by='ticker', auto_adjust=True)


close_prices = pd.concat(
    [price_data[ticker]['Close'].rename(ticker) for ticker in tickers if ticker in price_data.columns], axis=1)
volumes = pd.concat(
    [price_data[ticker]['Volume'].rename(ticker) for ticker in tickers if ticker in price_data.columns], axis=1)


benchmark = yf.download('LRGF', start='2019-01-01', end='2024-12-31', auto_adjust=True)
benchmark['Daily Return'] = benchmark['Close'].pct_change()


years = list(range(2019, 2025))
risk_free_rates = {
    2019: 0.023, 2020: 0.009, 2021: 0.001,
    2022: 0.018, 2023: 0.045, 2024: 0.0469
}

approx_shares_outstanding = 1e9
results = []


for year in years:
    print(f"\n🔎 Traitement de l'année {year}...")

    year_close = close_prices.loc[str(year)]
    year_volume = volumes.loc[str(year)]

    
    avg_volumes = year_volume.mean()
    avg_turnover = avg_volumes / approx_shares_outstanding
    filtered = avg_volumes[(avg_volumes > 500000) & (avg_turnover > 0.005)]
    filtered_tickers = filtered.index.tolist()

    if len(filtered_tickers) == 0:
        print(f"Aucun titre valide en {year} après filtrage.")
        continue

    year_returns = year_close[filtered_tickers].pct_change().dropna()

    
    filtered_weights = lrgf_liquid[lrgf_liquid['Ticker'].isin(filtered_tickers)].set_index('Ticker')['New Weight']
    filtered_weights = filtered_weights / filtered_weights.sum()

    for m in set(filtered_tickers) - set(filtered_weights.index):
        filtered_weights[m] = 1 / len(filtered_tickers)
    filtered_weights = filtered_weights / filtered_weights.sum()

    portfolio_returns = year_returns.mul(filtered_weights, axis=1).sum(axis=1)
    bench_year = benchmark['Daily Return'].loc[str(year)].dropna()

   
    aligned = pd.concat([portfolio_returns, bench_year], axis=1).dropna()
    portfolio_returns = aligned.iloc[:, 0]
    benchmark_returns = aligned.iloc[:, 1]

    annual_return = (1 + portfolio_returns).prod() - 1
    volatility = portfolio_returns.std() * np.sqrt(252)

  
    sharpe_ratio = (annual_return - risk_free_rates[year]) / volatility

    
    beta, alpha_daily = np.polyfit(benchmark_returns, portfolio_returns, 1)
    alpha_annual = alpha_daily * 252 * 100 

    active_return = portfolio_returns - benchmark_returns
    tracking_error = np.sqrt(252) * active_return.std()

    
    cumulative = (1 + portfolio_returns).cumprod()
    peak = cumulative.cummax()
    drawdown = (cumulative - peak) / peak
    max_dd = drawdown.min() * 100

    results.append({
        'Année': year,
        'Rendement (%)': annual_return * 100,
        'Volatilité (%)': volatility * 100,
        'Sharpe Ratio': sharpe_ratio,
        'Alpha (%)': alpha_annual,
        'Beta': beta,
        'Tracking Error (%)': tracking_error * 100,
        'Max Drawdown (%)': max_dd
    })
filtered_performance_df = pd.DataFrame(results).set_index('Année').round(2)


print(filtered_performance_df)


filtered_performance_df.to_csv('Analyse_LRGF_Filtré_Sharpe_Corrigé_2019_2024.csv')
