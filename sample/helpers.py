#!/usr/bin/python

from pytrends.request import TrendReq

def get_proxie_google_connection():
    pytrends_proxie = TrendReq(
        hl='en-US',
        tz=360,
        timeout=(10,25),
        proxies=['https://34.203.233.13.80',],
        retries=2,
        backoff_factor=0.1)
    return pytrends_proxie
    
def get_google_trends_df(keywords='Lil Nas X'):
    # Create DataFrame with Google trends data.
    return None
