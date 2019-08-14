#!/usr/bin/python

from helpers import get_proxie_google_connection

# Login to Google
pytrend = get_proxie_google_connection()

# Create payload and capture API tokens. Only required for interest_over_time(), interest_by_region(), and related_queries() methods.
pytrend.build_payload(kw_list=['Lil Nas X', 'Old Town Road'])

# Interest over time.
interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df.tail())

# Interest by Region
interest_by_region_df = pytrend.interest_by_region()
print(interest_by_region_df.tail())

# Related Queries, returns a dictionary of dataframes
related_queries_dict = pytrend.related_queries()
print(related_queries_dict)

# Get Google Hot Trends data
trending_searches_df = pytrend.trending_searches()
print(trending_searches_df.tail())

# Get Google Hot Trends data
today_searches_df = pytrend.today_searches()
print(today_searches_df.tail())

# Get Google Top Charts
top_charts_df = pytrend.top_charts(2018, hl='en-US', tz=300, geo='GLOBAL')
print(top_charts_df.tail())

# Get Google Keyword Suggestions
suggestions_dict = pytrend.suggestions(keyword='Lil Nas X')
print(suggestions_dict)
