# ====================
# IMPORTS
# ====================

import streamlit as st
import utils.countries_data as cdt

def create_sidebar(df):
        
    st.sidebar.markdown('## Fome Zero')

    st.sidebar.markdown('### Filtros')

    countries = st.sidebar.multiselect(
            'Selecione todos os países que deseja filtrar',
            df.loc[:, 'country_name'].unique().tolist(), 
            default = ['Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India'])

    st.sidebar.markdown('---')
    st.sidebar.markdown('##### Powered by Juarez Garritano')
    
    return list(countries)

            
def main():
    st.set_page_config(page_title="Countries", page_icon="🌐", layout="wide")
    
    df = cdt.read_processed_data()
    
    countries = create_sidebar(df)
    
    with st.container():
        fig = cdt.order_country(countries)
        fig.update_layout(title_text='Quantidade de restaurantes registrados por país', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True) 
    
    with st.container():
        fig = cdt.order_city(countries)
        fig.update_layout(title_text='Quantidade de cidades registradas por país', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)
        
    st.markdown('---')
    
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fig = cdt.votes_mean(countries)
            fig.update_layout(title_text='Média de avaliações feita por país', title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)
            
        with col2:
            fig = cdt.mean_for_two(countries)
            fig.update_layout(title_text='Média de preço de um prato para duas pessoas por país', title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()