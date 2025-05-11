import matplotlib.pyplot as plt


df_display = df.copy()
df_display["Rendement ETF"] = (df_display["Rendement ETF"] * 100).round(2)
df_display["Rendement Benchmark"] = (df_display["Rendement Benchmark"] * 100).round(2)
df_display["Volatilité ETF"] = (df_display["Volatilité ETF"] * 100).round(2)
df_display["Alpha"] = (df_display["Alpha"] * 100).round(2)
df_display["Tracking Error"] = (df_display["Tracking Error"] * 100).round(2)


df_display.columns = [
    "Rendement ETF (%)",
    "Rendement Benchmark (%)",
    "Volatilité ETF (%)",
    "Alpha (%)",
    "Bêta",
    "Ratio de Sharpe",
    "Tracking Error (%)"
]


fig, ax = plt.subplots(figsize=(14, 4))
ax.axis('off')
table = ax.table(cellText=df_display.values,
                 colLabels=df_display.columns,
                 rowLabels=df_display.index,
                 rowColours=["#f2f2f2"] * len(df_display),
                 colColours=["#d0d0d0"] * len(df_display.columns),
                 cellLoc='center',
                 loc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)
plt.title("Analyse de l'ETF LRGF (2019–2024)", fontsize=14, weight='bold', pad=20)
plt.tight_layout()
plt.show()
