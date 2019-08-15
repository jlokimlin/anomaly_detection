#!/usr/bin/python

from helpers import gtrends
import matplotlib.pyplot as plt

# Get Google trends as a pandas DataFrame
google_trends_df = gtrends(
    keywords=['Moving Delivery Services'],
    geo_region='en-US',
    timeframe='today 5-y')

# Visualize Google data
google_trends_df.plot()
plt.legend()
plt.savefig('../figures/moving_delivery_services_google_trends_plot.png', bbox_inches='tight')
plt.close()
