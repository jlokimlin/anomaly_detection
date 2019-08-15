#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt

from helpers import gtrends
from pyculiarity.detect_ts import detect_ts


KEYWORD='Flu Vaccine'
XLABEL='Time'
YLABEL='Relative Interest over Time'

# Get Google trend as a pandas DataFrame
google_trend_df = gtrends([KEYWORD])

# Set Google hits as a time series
ts = google_trend_df[KEYWORD]

# Plot data
# Visualize time series with matplotlib (optional but useful if we're choosing between keywords)
plt.title(KEYWORD + ' - Google Trends Data')
#plt.subtitle('United States search volume')
plt.xlabel(XLABEL)
plt.tick_params(axis='x', rotation=-45)
plt.ylabel(YLABEL)
plt.tight_layout()
plt.autoscale()
plt.plot(ts.index, ts.values)
plt.savefig('../figures/flu_vaccine_google_trends_plot.png', bbox_inches='tight')
plt.close()

'''Anomalize

References:
     Vallis, O., Hochenbaum, J. and Kejariwal, A., (2014) "A Novel
     Technique for Long-Term Anomaly Detection in the Cloud", 6th
     USENIX, Philadelphia, PA.

     Rosner, B., (May 1983), "Percentage Points for a Generalized ESD
     Many-Outlier Procedure" , Technometrics, 25(2), pp. 165-172.

'''

# First prepare data from truncated series
my_df = pd.DataFrame({'timestamp':ts.values, 'observation':ts.index})

results = detect_ts(df=my_df,
                  max_anoms=0.1,
                  direction="pos",
                  alpha=0.05,
                  only_last=None,
                  threshold=None,
                  e_value=False,
                  longterm=False,
                  piecewise_median_period_weeks=2,
                  plot=False,
                  y_log=False,
                  xlabel=XLABEL,
                  ylabel=YLABEL,
                  title='Google Trends Data - Twitter + IQR Method',
                  verbose=False)

plt.title(KEYWORD + ' - Google Trends Data - Twitter + GES')
#plt.subtitle('United States search volume')
plt.xlabel(XLABEL)
plt.tick_params(axis='x', rotation=-45)
plt.ylabel(YLABEL)
plt.tight_layout()
plt.autoscale()
plt.plot(ts.index, ts.values)
plt.plot(results['anoms'].anoms, 'o')
plt.savefig('../figures/flu_vaccine_anomalize_plot.png', bbox_inches='tight')
plt.close()
