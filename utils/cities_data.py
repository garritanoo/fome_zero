import pandas as pd
import streamlit as st
import plotly.express as px

def read_processed_data():
    return pd.read_csv('./dataset/processed_data/data.csv')

def top_ten(countries):
    
    df = read_processed_data()
    
    df_aux = ( df.loc[df['country_name'].isin(countries), ['city', 'restaurant_id', 'country_name']]
                                      .groupby(['country_name', 'city'])
                                      .count()
                                      .sort_values(by=['restaurant_id', 'city'], ascending=False)
                                      .reset_index()
                                      .head(10) )
    
    fig = px.bar(df_aux,
                 x='city',
                 y='restaurant_id',
                 text='restaurant_id', 
                 color='country_name',
                 text_auto='.2f',
                 title='Top 10 cidades com mais restaurantes na base de dados',
                 labels={
                    'city': 'Cidades',
                    'restaurant_id': 'Quantidade de restaurantes',
                     'country_name': 'País',
                    },
                )
    
    return fig

def top_seven_up(countries):
    
    df = read_processed_data()
        
    df_aux = ( df.loc[(df['country_name'].isin(countries) & (df['aggregate_rating'] >= 4)), ['city', 'restaurant_id', 'country_name']]
                                                                              .groupby(['country_name', 'city'])
                                                                              .count()
                                                                              .sort_values(by=['restaurant_id', 'city'], ascending=False)
                                                                              .reset_index()
                                                                              .head(7))
    
    fig = px.bar(df_aux,
                 x='city',
                 y='restaurant_id',
                 text='restaurant_id', 
                 color='country_name',
                 text_auto='.2f',
                 labels={
                    'city': 'Cidades',
                    'restaurant_id': 'Quantidade de Restaurantes',
                     'country_name': 'País',
                    },
                )
    
    return fig

def top_seven_down(countries):
    
    df = read_processed_data()
        
    df_aux = ( df.loc[(df['country_name'].isin(countries) & (df['aggregate_rating'] <= 2.5)), ['city', 'restaurant_id', 'country_name']]
                                                                              .groupby(['country_name', 'city'])
                                                                              .count()
                                                                              .sort_values(by=['restaurant_id', 'city'])
                                                                              .reset_index()
                                                                              .head(7))
    
    fig = px.bar(df_aux,
                 x='city',
                 y='restaurant_id',
                 text='city', 
                 color='country_name',
                 text_auto='.2f',
                 labels={
                    'city': 'Cidades',
                    'restaurant_id': 'Quantidade de Restaurantes',
                     'country_name': 'País',
                    },
                )
    
    return fig

def top_cuisines(countries):
    
    df = read_processed_data()
    
    df_aux = ( df.loc[df['country_name'].isin(countries), ['country_name', 'city', 'cuisines']]
                                      .groupby(['country_name', 'city'])
                                      .nunique()
                                      .sort_values(by=['city', 'cuisines'], ascending=False)
                                      .reset_index()
                                      .head(10) )

    fig = px.bar(df_aux,
                 x='city',
                 y='cuisines',
                text='cuisines', 
                color='country_name',
                title='Top 10 Cidades com mais culinárias distintas',
                labels={
                    'city': 'Cidades',
                    'restaurant_id': 'Quantidade de alguma coisa',
                    'country_name': 'País',
                    },
                )
    
    return fig