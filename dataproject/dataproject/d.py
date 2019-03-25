#%%
a = 'dear'
print('dear')
#%%

b = 5*9
print(b)

#%%
import pandas as pd

#%%
import os
#%%
import csv
#%%
df=pd.read_csv('C:/Users/aegea/.jupyter/data/food_supply_kilocalories_per_person_and_day.csv')
df.head(10)
df.info()
df.loc[:, ['2002']]
df['growth']=df['2009']/df['2010']
mydict={}
for i in range(1961, 2013):
    mydict[str(i)] = f'e{i}'
mydict
df.describe()
import numpy as np
import matplotlib.pyplot as plt
df1=pd.read_csv('E:/Block 8 IPNA/Data/total_health_spending_percent_of_gdp.csv')
new=pd.merge(df, df1, on=['country'], how='inner')
new


#%%

## maybe we can work with the codes from "Fun application" lecture note: CO2 emmisions and GDP part
## I will write sth down on the jubyternote file(ipynb) in dataproject folder, right below the dataproject.ipynb file: this is the folder where we should write down the final code as a result. I will name my practice ipynb file as pr:dataprojet.ipynb. Plz add up or change stuffs freely there

