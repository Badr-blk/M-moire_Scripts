import pandas as pd


vlue_comp = pd.read_csv('VLUE_holdings.csv')
mtum_comp = pd.read_csv('MTUM_holdings.csv')
usmv_comp = pd.read_csv('USMV_holdings.csv')
qual_comp = pd.read_csv('QUAL_holdings.csv')
lrgf_comp = pd.read_csv('LRGF_holdings.csv')

vlue_comp = pd.read_csv('VLUE_holdings.csv', skiprows=9, sep=',')
print(vlue_comp.head())
