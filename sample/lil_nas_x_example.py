#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt

from helpers import get_proxie_google_connection
from pyculiarity.detect_ts import detect_ts

END_OF_LAST_YEAR='2018-12-20'
ARTIST = 'Lil Nas X'
SONG = 'Old Town Road'
TOPICS=[ARTIST, SONG]
XLABEL='Time'
YLABEL='Relative Interest over Time'

# Login to Google
pytrend = get_proxie_google_connection()

# Create payload and capture API tokens. Only required for interest_over_time(), interest_by_region(), and related_queries() methods.
pytrend.build_payload(kw_list=TOPICS)

# Get Google Trend of Topics  as a Pandas DataFrame
google_trend_df = pytrend.interest_over_time()
# Get artist Google hits as a time series
s = google_trend_df[ARTIST]
# Truncate series at start of 2019. pytrends library defaults to 5 years.
s=s.truncate(before=pd.Timestamp(END_OF_LAST_YEAR))

# Plot data
# Visualize time series with matplotlib (optional but useful if we're choosing between keywords)
plt.title('Lil Nas X - Google Trends Data')
#plt.subtitle('United States search volume')
plt.xlabel(XLABEL)
plt.tick_params(axis='x', rotation=-45)
plt.ylabel(YLABEL)
plt.tight_layout()
plt.autoscale()
plt.plot(s.index, s.values)
plt.savefig('../figures/lil_nas_x_google_trends_plot.png', bbox_inches='tight')
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
my_df = pd.DataFrame({'timestamp':s.values, 'observation':s.index})

results = detect_ts(df=my_df,
                  max_anoms=0.2,
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

plt.title('Lil Nas X - Google Trends Data - Twitter + GES')
#plt.subtitle('United States search volume')
plt.xlabel(XLABEL)
plt.tick_params(axis='x', rotation=-45)
plt.ylabel(YLABEL)
plt.tight_layout()
plt.autoscale()
plt.plot(s.index, s.values)
plt.plot(results['anoms'].anoms, 'o')
plt.savefig('../figures/lil_nas_x_anomalize_plot.png', bbox_inches='tight')
plt.close()

