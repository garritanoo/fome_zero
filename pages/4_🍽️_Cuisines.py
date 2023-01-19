# ====================
# IMPORTS
# ====================

import streamlit as st
import utils.cuisines_data as cdt

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
    st.set_page_config(page_title="Cuisines", page_icon="🍽️", layout="wide")
    
    df = cdt.read_processed_data()
    
    countries = create_sidebar(df)
    
    st.markdown('### Melhores Restaurantes dos Principais Tipos Culinários')
    
    with st.container():
        cdt.restaurant_cuisine(countries)
        
    st.markdown('---')
    
    st.markdown('### Top 10 Restaurantes')
    
    with st.container():
        df_restaurants = cdt.top_ten_restaurants(countries)
        st.dataframe(df_restaurants)
        
    st.markdown('---')
        
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            fig = cdt.ten_top_cuisines(countries)
            fig.update_layout(title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)

        with col2:
            fig = cdt.ten_worse_cuisines(countries)
            fig.update_layout(title_x=0.5)
            st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()