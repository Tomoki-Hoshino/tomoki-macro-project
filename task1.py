import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pandas_datareader.data import DataReader

start_date = '1996-01-01'
end_date = '2024-10-01'

Brazilgdp = DataReader('NGDPRSAXDCBRQ','fred',start_date,end_date)
log_bgdp = np.log(Brazilgdp)

Japangdp = DataReader('NGDPRSAXDCJPQ','fred',start_date,end_date)
log_jgdp = np.log(Japangdp)

lambdas = [10,100,1600]
Brazil_trends = {}
Japan_trends = {}

for lam in lambdas:
    _, b_trend = sm.tsa.filters.hpfilter(log_bgdp, lamb=lam)
    _, j_trend = sm.tsa.filters.hpfilter(log_jgdp, lamb=lam)
    Brazil_trends[lam] = b_trend
    Japan_trends[lam] = j_trend

plt.figure(figsize=(12, 6))
plt.plot(log_jgdp, label="Japan Log GDP", color="gray", linewidth=1.5)
plt.plot(log_bgdp, label="Brazil Log GDP", color="black", linewidth=1.5)

colors = ['red','green','blue']
for lam, color in zip(lambdas,  colors):
    plt.plot(Brazil_trends[lam], label=f"Brazil Trend (λ={lam})", linestyle='--', color=color)
    plt.plot(Japan_trends[lam], label=f"Japan Trend λ={lam}", linestyle=':', color=color)


plt.title("Log of Brazil and Japan Real GDP and HP Trend (1996–2024)")
plt.xlabel("Date")
plt.ylabel("Log GDP")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()