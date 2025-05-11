# --- Partie 1 : Nettoyage (déjà fait) ---
import pandas as pd
import yfinance as yf

vlue_comp = pd.read_csv('USMV_holdings.csv', skiprows=9)
vlue_filtered = vlue_comp[['Ticker', 'Name', 'Weight (%)', 'Quantity', 'Price']]
vlue_filtered = vlue_filtered.rename(columns={'Weight (%)': 'Weight'})

# --- Partie 2 : Volume moyen et filtrage (nouveau à ajouter) ---
tickers = vlue_filtered['Ticker'].tolist()

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

vlue_filtered['Avg Volume'] = vlue_filtered['Ticker'].map(volume_moyen)

# Filtrer
volume_seuil = 500000
vlue_liquid = vlue_filtered[vlue_filtered['Avg Volume'] > volume_seuil]

# Repondérer
vlue_liquid['New Weight'] = vlue_liquid['Weight'] / vlue_liquid['Weight'].sum() * 100

# Afficher résultat
print(vlue_liquid[['Ticker', 'Name', 'New Weight', 'Avg Volume']])

# Sauvegarder
vlue_liquid.to_csv('USMV_liquid_filtered.csv', index=False)
print("\n✅ Fichier USMV_liquid_filtered.csv créé avec succès !")

