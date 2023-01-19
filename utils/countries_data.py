import pandas as pd
import streamlit as st
import plotly.express as px


def read_processed_data():
    return pd.read_csv('./dataset/processed_data/data.csv')

def order_country(countries):
    
    df = read_processed_data()
    
    df_aux = ( 
        df.loc[df['country_name'].isin(countries), ['country_name', 'restaurant_id']]
                                  .groupby('country_name')
                                  .count()
                                  .sort_values(by='restaurant_id', ascending=False)
                                  .reset_index() )
    
    fig = px.bar(df_aux,
                 x='country_name',
                 y='restaurant_id',
                 # text_auto=True,
                 title='Quantidade de restaurantes registrados por país',
                 text='restaurant_id',
                 labels={
                     'country_name': 'Países',
                     'restaurant_id':'Quantidade de Restaurantes',
                 },
                )
        
    return fig

def order_city(countries):
    
    df = read_processed_data()
    
    df_aux = (
        df.loc[df['country_name'].isin(countries), ['country_name', 'city']]
              .groupby('country_name')
              .nunique()
              .sort_values(by='city', ascending=False)
              .reset_index() )

    fig = px.bar(df_aux,
                 x='country_name',
                 y='city',
                 title='Quantiade de restaurantes registrados por cidade',
                 text='city',
                 labels={
                     'country_name': 'Países',
                     'city': 'Quantidade de Cidades',
                 },
                )
    
    return fig

def votes_mean(countries):
    
    df = read_processed_data()
    
    df_aux = (df.loc[df['country_name'].isin(countries), ['country_name', 'votes']]
                                      .groupby('country_name')
                                      .mean()
                                      .sort_values(by='votes', ascending=False)
                                      .reset_index())
    
    fig = px.bar(df_aux, 
                 x='country_name',
                 y='votes',
                 title='Média de avaliações feitas por país',
                 text='votes',
                 text_auto='.2f',
                 labels={
                     'country_name': 'Países',
                     'votes': 'Votos',
                    },
                )

    return fig

def mean_for_two(countries):
    
    df = read_processed_data()
    
    df_aux = ( df.loc[df['country_name'].isin(countries), ['country_name', 'price_in_dollar']]
                                        .groupby('country_name')
                                        .mean()
                                        .sort_values('price_in_dollar', ascending=False)
                                        .reset_index() )
    
    fig = px.bar(df_aux, 
                 x='country_name',
                 y='price_in_dollar',
                 title='Média de preço para duas pessoas',
                 text='price_in_dollar',
                 text_auto='.2f',
                 labels={
                     'country_name': 'Países',
                     'price_in_dollar': 'Preço em dólar',
                    },
                )
    
    return fig