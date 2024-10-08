import pandas as pd
import streamlit as st
import PIL.Image as Image

from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_numeric_dtype,
    is_object_dtype,
)

st.set_page_config(
    page_title="Pesquisa Dados PEDE",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🔍"
)

with open("./css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

image = Image.open("./img/passos-magicos.png")
st.image(image)

logo = Image.open("./img/postech-logo-white.png")
logo2 = Image.open("./img/postech-logo-white2.png")
st.logo(logo2, link=None, icon_image=logo)

st.title("🔍 Pesquisa Dados da PEDE (2020, 2021 e 2022)")
st.markdown("---")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)

    # Convertendo a coluna ID do aluno para inteiro
    if 'ID_ALUNO' in df.columns:
        df['ID_ALUNO'] = df['ID_ALUNO'].astype(int)

    return df

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:

    modify = st.checkbox("Adicione os filtros desejados")

    if not modify:
        return df

    df = df.copy()

    # Tenta converter datetimes para um formato padrão (datetime, sem timezone)
    for col in df.columns:
        if is_object_dtype(df[col]):
            try:
                df[col] = pd.to_datetime(df[col])
            except Exception:
                pass

        if is_datetime64_any_dtype(df[col]):
            df[col] = df[col].dt.tz_localize(None)

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filtrar dataframe em", df.columns, placeholder="Selecione uma opção")
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            left.write("↳")
            # Tratando a coluna ID_ALUNO como inteiro
            if column == "ID_ALUNO":
                user_num_input = right.number_input(
                    f"Valor para {column}",
                    min_value=int(df[column].min()),
                    max_value=int(df[column].max()),
                    value=None,
                )
                if user_num_input is not None:
                    df = df[df[column] == user_num_input]
            elif isinstance(df[column].dtype, pd.api.types.CategoricalDtype) or df[column].nunique() < 10:
                user_cat_input = right.multiselect(
                    f"Valores para {column}",
                    df[column].unique(), placeholder="Selecione uma opção"
                )
                if user_cat_input:
                    df = df[df[column].isin(user_cat_input)]
            elif is_numeric_dtype(df[column]):
                user_num_input = right.number_input(
                    f"Valor para {column}",
                    min_value=float(df[column].min()),
                    max_value=float(df[column].max()),
                    value=None,
                )
                if user_num_input is not None:
                    df = df[df[column] == user_num_input]
            elif is_datetime64_any_dtype(df[column]):
                user_date_input = right.date_input(
                    f"Valor para {column}",
                    value=None,
                )
                if user_date_input:
                    start_date, end_date = user_date_input
                    df = df.loc[df[column].between(start_date, end_date)]
            else:
                user_text_input = right.text_input(
                    f"Substring ou regex em {column}",
                )
                if user_text_input:
                    df = df[df[column].str.contains(user_text_input)]

    return df


st.write(
    """Nessa página estamos inserindo uma cópia do nosso dataset para pesquisa e visualização simples em tabela
    """
)

df = load_data("dataset/dados_finais.csv")

st.dataframe(filter_dataframe(df))
