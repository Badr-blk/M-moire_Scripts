import yfinance as yf
import pandas as pd

etfs = ['VLUE', 'MTUM', 'USMV', 'QUAL', 'LRGF']

start_date = "2019-01-01"
end_date = "2024-12-31"


price_data = {}
volume_data = {}

for etf in etfs:
    data = yf.download(etf, start=start_date, end=end_date, interval='1d')
    price_data[etf] = data['Close']   
    volume_data[etf] = data['Volume'] 


prices_df = pd.concat(price_data, axis=1)    
volumes_df = pd.concat(volume_data, axis=1)   


prices_df.to_csv('ETF_prices_2019_2024.csv')
volumes_df.to_csv('ETF_volumes_2019_2024.csv')


