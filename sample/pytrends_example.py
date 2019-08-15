#!/usr/bin/python

from helpers import gtrends
import matplotlib.pyplot as plt

US_SPELLING = 'Donut'
BRITISH_SPELLING = 'Doughnut'

# Get Google trends as a pandas DataFrame
google_trends_df = gtrends(
    keywords=[US_SPELLING, BRITISH_SPELLING],
    geo_region='GLOBAL',
    timeframe='today 5-y')

# Visualize Google data
google_trends_df.plot(title='How do you spell it?')
plt.legend()
plt.savefig('../figures/google_trends_plot.png', bbox_inches='tight')
plt.close()
