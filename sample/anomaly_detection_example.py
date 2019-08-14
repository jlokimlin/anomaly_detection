#!/usr/bin/python

import pandas as pd
import matplotlib.pyplot as plt

from helpers import get_proxie_google_connection

END_OF_LAST_YEAR='2018-12-20'
ARTIST = 'Lil Nas X'
SONG = 'Old Town Road'
TOPICS=[ARTIST, SONG]

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

# Visualize time series with matplotlib (optional but useful if we're choosing between keywords)
plt.title('Google Trends Data')
#plt.subtitle('United States search volume')
plt.xlabel('Time')
plt.tick_params(axis='x', rotation=-45)
plt.ylabel('Relative interest over time')
plt.tight_layout()
plt.autoscale()
plt.plot(s.index, s.values)
plt.savefig('../figures/google_trends_plot.png', bbox_inches='tight')
