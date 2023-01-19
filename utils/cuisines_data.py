import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def read_processed_data():
    return pd.read_csv('./dataset/processed_data/data.csv')

def restaurant_cuisine(countries):
    
    df = read_processed_data()
    
    filter_restaurants = (df['aggregate_rating'] == df['aggregate_rating'].max()) & (df['country_name'].isin(countries))
    cols = ['restaurant_name', 'cuisines', 'aggregate_rating']
    
    df_aux = (df.loc[filter_restaurants, cols].groupby(['cuisines'])
                                            .max()
                                            .sort_values(by='aggregate_rating', ascending=False)
                                            .reset_index()
                                           .head(5))
    
    col = st.columns(5)
    for index, coluna in df_aux.iterrows():
         with col[index]:
            cuisines_metric = col[index].metric(f'{coluna[1]}: {coluna[0]}', f'{coluna[2]}/5.0')
            
    return cuisines_metric

def top_ten_restaurants(countries):
    
    df = read_processed_data()
    
    filter_restaurant = (df['aggregate_rating'] == df['aggregate_rating'].max()) & (df['country_name'].isin(countries))
    cols = ['restaurant_id', 'restaurant_name', 'country_name', 'city', 'cuisines', 'price_in_dollar', 'aggregate_rating', 'votes']   
    
    df_aux = (df.loc[filter_restaurant, cols]
                    .sort_values(by='restaurant_id')
                    .head(10))
    return df_aux

def ten_top_cuisines(countries):
    
    df = read_processed_data()
    
    df_aux = (df.loc[df['country_name'].isin(countries), ['cuisines', 'aggregate_rating']].groupby('cuisines')
              .max()
              .sort_values(by='aggregate_rating', ascending=False)
              .reset_index()
              .head(10))

    fig = px.bar(df_aux,
                 x='cuisines',
                 y='aggregate_rating',
                 text='aggregate_rating',
                 title='Top 10 melhores culinárias',
                 labels={
                    'cuisines': 'Tipo de Culinária',
                     'aggregate_rating': 'Média de Avaliações'
                    },
                )
    
    return fig

def ten_worse_cuisines(countries):
    
    df = read_processed_data()
    
    df_aux = (df.loc[df['country_name'].isin(countries), ['cuisines', 'aggregate_rating']].groupby('cuisines')
              .max()
              .sort_values(by='aggregate_rating')
              .reset_index()
              .head(10))

    fig = px.bar(df_aux,
                 x='cuisines',
                 y='aggregate_rating',
                 text='aggregate_rating',
                 title='Top 10 piores culinárias',
                 labels={
                    'cuisines': 'Tipo de Culinária',
                     'aggregate_rating': 'Média de Avaliações'
                    },
                )
    
    return fig