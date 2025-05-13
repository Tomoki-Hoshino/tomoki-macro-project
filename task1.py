import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas_datareader.data import DataReader

start_date = '1996-01-01'
end_date = '2024-10-01'

bgdp = DataReader('NGDPRSAXDCBRQ','fred',start_date,end_date)
log_gdp = np.log(bgdp)

lambdas = [10,100,1600]
trends = {}

for lam in lambdas:
    _,trend = sm.tsa.filters.hpfilter(log_gdp, lamb=lam)
    trends[lam] = trend

plt.figure(figsize=(12, 6))
plt.plot(log_gdp, label="Log of Real GDP", color='black')

colors = ['red','green','blue']
for lam, color in zip(lambdas,  colors):
    plt.plot(trends[lam], label=f"HP Trend (λ={lam})", linestyle='--', color=color)

plt.title("Log of Brazil Real GDP and HP Trend (1996–2024)")
plt.xlabel("Date")
plt.ylabel("Log GDP")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()