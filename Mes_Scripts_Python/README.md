#  Scripts du Mémoire

Ce dépôt contient les scripts Python développés dans le cadre du mémoire :  
**"Titre de ton mémoire"**  
Auteur : BOULEKHLEF BADR – Année : *2025*

---

## Contenu des Applications

###  **Application 1 – Analyse de la Performance des ETF (2019-2024)**  
- Calcul du **ratio de Sharpe** pour évaluer la rentabilité ajustée au risque.  
- Élaboration d’un **tableau de performance** des ETF sur la période 2019-2024, comprenant :  
  - Ratio de Sharpe  
  - Bêta  
  - Tracking Error  
  - Volatilité des ETF  
  - Volatilité des benchmarks  

###  **Application 2 – Analyse des Titres Sous-Jacents des ETF**  
- Filtrage d’un document (holdings) issu du site de l’émetteur des ETF (iShares), illustrant le poids des titres sous-jacents.  
- Sélection des colonnes utiles à l’analyse.  
- Application de **deux filtres de liquidité** pour restreindre l’univers des titres analysés.  
- Réalisation de la même analyse de performance que pour l’Application 1, adaptée aux titres filtrés.

---

##  Prérequis

- Python 3.11 ou plus récent.
- Librairies Python nécessaires :
  - pandas  
  - numpy  
  - matplotlib  

Installation des librairies :

```bash
pip install pandas numpy matplotlib
