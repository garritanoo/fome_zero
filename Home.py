# ====================
# IMPORTS
# ====================

import pandas as pd
import streamlit as st
import folium
from PIL import Image
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

from utils import general_data as gd
from utils.processed_data import processed_data

RAW_DATA_PATH = f'./dataset/raw/zomato.csv'

def create_sidebar(df):
    
    image = Image.open('images/restaurant.png')
    st.sidebar.image(image, width=50)

    st.sidebar.markdown('## Fome Zero')

    st.sidebar.markdown('### Filtros')

    countries = st.sidebar.multiselect(
            'Selecione todos os países que deseja filtrar',
            df.loc[:, 'country_name'].unique().tolist(), 
            default = ['Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India'])

    st.sidebar.markdown('### Dados Tratados')

    df_complete = pd.read_csv('./dataset/processed_data/data.csv')

    st.sidebar.download_button(
        label='Download',
        data=df_complete.to_csv(index=False, sep=';'),
        file_name='data.csv',
        mime='text/csv',
    )

    st.sidebar.markdown('---')
    st.sidebar.markdown('##### Powered by Juarez Garritano')
    
    return list(countries)

def create_map(df):
    m = folium.Map(zoom_start=10)
    
    marker_cluster = MarkerCluster().add_to(m)
    
    for _, location_info in df.iterrows():
        name = location_info['restaurant_name']
        price_dollar = location_info['price_in_dollar']
        cuisines = location_info['cuisines']
        aggregate_rating = location_info['aggregate_rating']
        color = f"{location_info['color_name']}"
        
        html = "<p><strong>{}</strong></p>"
        html += "<p>Price: {},00 para dois</p>"
        html += "<br />Type: {}"
        html += "<br />Aggregate Rating: {}/5.0"
        html += html.format(name, price_dollar, cuisines, aggregate_rating)
        
        popup = folium.Popup(
            folium.Html(html, script=True),
            max_width=500,
        )
        
        folium.Marker( [ location_info['latitude'], location_info['longitude'] ],
                        popup=popup,
                        icon=folium.Icon(color=color, icon='home', prefix='fa'),
                     ).add_to(marker_cluster)

    folium_static(m, width=960, height=600)
    

    return None    


# ------------------------- INICIO DA ESTRUTURA LÓGICA -------------------------


def main():
    
    df = processed_data(RAW_DATA_PATH)

    st.set_page_config(page_title='Home', page_icon=':house:', layout='wide')
    
    st.header('Fome Zero')
    st.subheader('O melhor lugar para encontrar seu restaurante favorito!')

    st.markdown('#### Confira as principais métricas da nossa plataforma')
    
    countries = create_sidebar(df)

    with st.container():
        col1, col2, col3, col4, col5  = st.columns(5)
        
        col1.metric('Restaurantes Cadastrados', gd.restaurant_metric(df))
        
        col2.metric('Países Cadastrados', gd.country_metric(df))
        
        col3.metric('Cidades Cadastradas', gd.city_metric(df))
        
        col4.metric('Total de Avaliações', f'{gd.votes_metric(df):,}'.replace(',', '.'))
        
        col5.metric('Tipos de Culinárias', gd.cuisines_metric(df))
            
    st.markdown('---')
        
    with st.container():
        df_map = df.loc[df['country_name'].isin(countries),  :]
        
        create_map(df_map)
        
        return None
        
if __name__ == '__main__':
    main()
