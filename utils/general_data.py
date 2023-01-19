import pandas as pd
from .processed_data import processed_data

def restaurant_metric(df):
    return df.loc[:, 'restaurant_id'].count()
    
def country_metric(df):    
    return df.loc[:, 'country_code'].nunique()
    
def city_metric(df):
    return df.loc[:, 'city'].nunique()
    
def votes_metric(df):
    return df.loc[:, 'votes'].sum()
    
def cuisines_metric(df):
    return df.loc[:, 'cuisines'].nunique()