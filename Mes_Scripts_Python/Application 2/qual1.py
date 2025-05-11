# --- Partie 1 : Nettoyage (déjà fait) ---
import pandas as pd
import yfinance as yf

# Charger les holdings de QUAL
qual_comp = pd.read_csv('QUAL_holdings.csv', skiprows=9)
qual_filtered = qual_comp[['Ticker', 'Name', 'Weight (%)', 'Quantity', 'Price']]
qual_filtered = qual_filtered.rename(columns={'Weight (%)': 'Weight'})

# --- Partie 2 : Volume moyen et filtrage (nouveau à ajouter) ---
tickers = qual_filtered['Ticker'].tolist()

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

qual_filtered['Avg Volume'] = qual_filtered['Ticker'].map(volume_moyen)

# Filtrer selon un seuil de volume
volume_seuil = 500000
qual_liquid = qual_filtered[qual_filtered['Avg Volume'] > volume_seuil]

# Repondérer les poids
qual_liquid['New Weight'] = qual_liquid['Weight'] / qual_liquid['Weight'].sum() * 100

# Afficher le résultat
print(qual_liquid[['Ticker', 'Name', 'New Weight', 'Avg Volume']])

# Sauvegarder
qual_liquid.to_csv('QUAL_liquid_filtered.csv', index=False)
print("\n✅ Fichier QUAL_liquid_filtered.csv créé avec succès !")
