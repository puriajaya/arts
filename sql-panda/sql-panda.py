import numpy as np
import pandas as pd

path='/media/rijan/disk2/kaggle/kcode/'
dataset =pd.read_csv(path+'prices.csv')

# Assume table name pricescsv

# select count(*) from pricescsv
print(len(dataset))
#851264

#select * from pricescsv limit 4
print(dataset.head(4))
#                  date  symbol        open       close         low        high     volume
# 0  2016-01-05 00:00:00   WLTW  123.430000  125.839996  122.309998  126.250000  2163600.0
# 1  2016-01-06 00:00:00   WLTW  125.239998  119.980003  119.940002  125.540001  2386400.0
# 2  2016-01-07 00:00:00   WLTW  116.379997  114.949997  114.930000  119.739998  2489500.0
# 3  2016-01-08 00:00:00   WLTW  115.480003  116.620003  113.500000  117.440002  2006300.0


#select symbol, volumn from pricescsv limit 10
print(dataset[['symbol','volume']].head(10))


#select count(*) from pricescsv where symbol='WLTW'
print(len(dataset[dataset['symbol'] == 'WLTW']))    #251


# select distinct(symbol) from pricescsv
print(dataset['symbol'].unique()[:20])
# ['WLTW' 'A' 'AAL' 'AAP' 'AAPL' 'ABC' 'ABT' 'ACN' 'ADBE' 'ADI' 'ADM' 'ADP'
#  'ADS' 'ADSK' 'AEE' 'AEP' 'AES' 'AET' 'AFL' 'AGN']


#select count(*) from pricescsv groupby symbol
print(dataset.groupby('symbol').size())
# XYL     1008
# YHOO    1762
# YUM     1762
# ZBH     1762
# ZION    1762
# ZTS      987
# Length: 501, dtype: int64

# select sum(volume) from pricescsv where symbol='XYL'
print(dataset[dataset['symbol']=='XYL'][['volume']].sum())


#select count(*) from pricescsv groupby symbol orderby symbol
print(dataset[['symbol','volume']].sort_values('symbol',ascending=False).head(10))

