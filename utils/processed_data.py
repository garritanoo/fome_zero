import pandas as pd
import inflection

def country_name(name):
    """Está função tem a responsabilidade de converter o número inteiro, correspondente a um país em uma string com o nome do país
        
        Tipo de conversão
        1. Número inteiro -> String com nome do país
        
        return: nome do país
    """
    
    country_name = {
        1: "India",
        14: "Australia",
        30: "Brazil",
        37: "Canada",
        94: "Indonesia",
        148: "New Zeland",
        162: "Philippines",
        166: "Qatar",
        184: "Singapure",
        189: "South Africa",
        191: "Sri Lanka",
        208: "Turkey",
        214: "United Arab Emirates",
        215: "England",
        216: "United States of America",
    }
    
    return country_name[name]

def price_type(price_range):
    """Está função tem a responsabilidade de converter um número inteiro a um correspondente nível de precificação
        
        Tipo de conversão
        1. Número inteiro: 1, 2, 3 e 4
        2. String derivada dos números: 
            1 = cheap
            2 = normal
            3 = expensive
            4 = gourmet
        
        return: string com o nível de precificação
    """
    
    if price_range == 1:
        return "cheap"
    elif price_range == 2:
        return "normal"
    elif price_range == 3:
        return "expensive"
    else:
        return "gourmet"

def color_name(color_code):
    '''Função que cria cores baseada em códigos hexadecimais
    
    return: cor referente a um código hexadecimal
    '''   
    
    COLORS = {
        "3F7E00": "darkgreen",
        "5BA829": "green",
        "9ACD32": "lightgreen",
        "CDD614": "orange",
        "FFBA00": "red",
        "CBCBC8": "darkred",
        "FF7800": "darkred",
    }
    
    return COLORS[color_code]

def clean_dataframe(df):
    ''' Função que tem a responsabilidade de limpar o dataframe
    
        Tipos de limpeza:
        1. Remoação de valores outliers
        2. Remoção de valores nulos
        3. Remocação de valores duplicados
        4. Categorizar os valores da coluna cuisines com apenas um tipo de culinária
        
        return: um dataframe limpo baseado nos tipos descritos acima    
    
    '''
    
    
    return df
    

def rename_columns(df):
    '''Função que formata o nome das colunas    
    
        1. Recebe um dataframe
        2. Localiza os títulos
        3. Coloca os títulos em letras minúsculas
        4. Remove os espaços
        5. Insere um _ no lugar dos espaços
        6 Transforma os títulos em uma lista
        
        return: um dataframe com o cabeçalho formatado "texto_texto"
    '''
    
    df = df.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    
    return df

def processed_data(file_path):
    df_raw = pd.read_csv(file_path)

    # Renomeia as colunas > limpa o dataframe
    df = rename_columns(df_raw)
    
    # Excluindo outlier do dataset
    df = df.loc[df['restaurant_id'] != 16608070, :]
    
    df = df.loc[df['average_cost_for_two'] != 0, :]
    
    # Removendo valores nulos do dataset
    df = df.loc[df['cuisines'].notnull(), :]

    # Excluindo dados duplicados do datatset
    df = df.loc[:, :].drop_duplicates().reset_index(drop=True)

    # Categorizando os restaurantes por um tipo de culinária
    df['cuisines'] = df.loc[:, 'cuisines'].apply(lambda x: x.split(",")[0])
    
    # Criando a coluna price_type de acordo com a coluna price_range
    df['price_type'] = df['price_range'].apply(lambda x: price_type(x))

    # Criando a coluna color name de acordo com a coluna rating_color
    df['color_name'] = df['rating_color'].apply(lambda x: color_name(x))

    # Criando a coluna country_name baseada na coluna country_code
    df['country_name'] = df['country_code'].apply(lambda x: country_name(x))
    
    # Criando a coluna price_in_dollar baseada nas colunas currency e average_cost_for_two
    df['price_in_dollar'] = ( df[['currency', 'average_cost_for_two']]
                 .apply( lambda x: ( x['average_cost_for_two'] / 12.85 )
                if x['currency'] == 'Botswana Pula(P)' else ( x['average_cost_for_two'] / 5.31 )
                if x['currency'] == 'Brazilian Real(R$)' else ( x['average_cost_for_two'] / 1 )
                if x['currency'] == 'Dollar($)' else ( x['average_cost_for_two'] / 3.67 )
                if x['currency'] == 'Emirati Diram(AED)' else ( x['average_cost_for_two'] / 82.68 )
                if x['currency'] == 'Indian Rupees(Rs.)' else ( x['average_cost_for_two'] / 15608.45 )
                if x['currency'] == 'Indonesian Rupiah(IDR)' else ( x['average_cost_for_two'] / 1.57 )
                if x['currency'] == 'NewZealand($)' else ( x['average_cost_for_two'] / 0.819257 )
                if x['currency'] == 'Pounds(£)' else ( x['average_cost_for_two'] / 3.64 )
                if x['currency'] == 'Qatari Rial(QR)' else ( x['average_cost_for_two'] / 17.59 )
                if x['currency'] == 'Rand(R)' else ( x['average_cost_for_two'] / 366.86 )
                if x['currency'] == 'Sri Lankan Rupee(LKR)' else ( x['average_cost_for_two'] / 18.65 )
                if x['currency'] == 'Turkish Lira(TL)' else 0, axis=1 ) )
    
    df.to_csv('./dataset/processed_data/data.csv', index=False)
    
    return df