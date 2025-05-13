conda create -n py311-env python=3.11
conda activate py311-env
pip install pandas_datareader pandas

import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas_datareader as pdr
import numpy as np

start_date = '1996-01-01'
end_date = '2024-10-01'

bgdp = web.DataReader('NGDPRSAXDCBRQ','fred',start_date,end_date)
log_bgdp = np.log(bgdp)

cycle, trend = sm.tsa.filters.hpfilter(log_bgdp, lamb=1600)

plt.plot(log_gdp, label="Original GDP (in log)")

plt.plot(trend, label="Trend")

plt.legend()
plt.show()