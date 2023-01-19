# ====================
# IMPORTS
# ====================

import streamlit as st
import utils.cities_data as cdt

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
    st.set_page_config(page_title="Cities", page_icon="🏙️", layout="wide")
    
    df = cdt.read_processed_data()
    
    countries = create_sidebar(df)
    
    with st.container():
        fig = cdt.top_ten(countries)
        fig.update_layout(title_text='Top 10 cidades com mais restaurantes na base de dados', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True) 
        
    st.markdown('---')
        
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fig = cdt.top_seven_up(countries)
            fig.update_layout(title_text='Top 7 restaurantes com avaliações acima de 4.0', title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            fig = cdt.top_seven_down(countries)
            fig.update_layout(title_text='Top 7 restaurantes com avaliações abaixo de 2.5', title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)
        
    st.markdown('---')
            
    with st.container():
        fig = cdt.top_cuisines(countries)
        fig.update_layout(title_text='Top 10 cidades com mais restaurantes com tipos culinários distintos ', title_x=0.5)
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()