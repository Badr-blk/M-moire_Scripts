
import pandas as pd
import yfinance as yf

lrgf_comp = pd.read_csv('LRGF_holdings.csv', skiprows=9)
lrgf_filtered = lrgf_comp[['Ticker', 'Name', 'Weight (%)', 'Quantity', 'Price']]
lrgf_filtered = lrgf_filtered.rename(columns={'Weight (%)': 'Weight'})

tickers = lrgf_filtered['Ticker'].tolist()

volume_moyen = {}

for ticker in tickers:
    try:
        data = yf.Ticker(ticker)
        hist = data.history(period="1mo")
        avg_volume = hist['Volume'].mean()
        volume_moyen[ticker] = avg_volume
    except Exception as e:
        print(f"Erreur pour {ticker}: {e}")
        volume_moyen[ticker] = None


lrgf_filtered['Avg Volume'] = lrgf_filtered['Ticker'].map(volume_moyen)
volume_seuil = 500000  
lrgf_liquid = lrgf_filtered[lrgf_filtered['Avg Volume'] > volume_seuil]
lrgf_liquid['New Weight'] = lrgf_liquid['Weight'] / lrgf_liquid['Weight'].sum() * 100
print(lrgf_liquid[['Ticker', 'Name', 'New Weight', 'Avg Volume']])
lrgf_liquid.to_csv('LRGF_liquid_filtered.csv', index=False)

