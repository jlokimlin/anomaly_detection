#!/usr/bin/python

from pytrends.request import TrendReq

def get_proxie_google_connection(geo_region='en-US'):
    pytrends_proxie = TrendReq(
        hl=geo_region,
        tz=360,
        timeout=(10,25),
        proxies=['https://34.203.233.13.80',],
        retries=2,
        backoff_factor=0.1)
    return pytrends_proxie
    
def gtrends(keywords, geo_region='en-US', timeframe='today 5-y'):
    """
    Description:
    
    Get a pandas DataFrame with Google trends data as a
    two column data frame where the first column consists of the timestamps
    and the second column consists of the observation.

    timestamps: year-month-date

    observation: Numbers represent search interest relative to the highest point on the chart for the given region and time. A value of 100 is the peak popularity for the term. A value of 50 means that the term is half as popular. A score of 0 means there was not enough data for this term.

    Usage:

    get_google_trends_df(keywords=['World Cup', 'FIFA', 'Russia'])

    Arguments:

    keywords:  A list of strings. 

    geo

Value: 
    
    The returned value is a pandas DataFrame containing timestamps and observation values. 
"""
    
    
    # Login to Google
    pytrend = get_proxie_google_connection(geo_region)

    # Create payload and capture API tokens. Only required for interest_over_time(), interest_by_region(), and related_queries() methods.
    pytrend.build_payload(kw_list=keywords, timeframe=timeframe)

    # Get Google Trends of keywords  as a Pandas DataFrame
    google_trends_df = pytrend.interest_over_time()

    return google_trends_df
