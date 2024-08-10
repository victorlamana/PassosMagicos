import streamlit as st

st.set_page_config(
    page_title="Visao 360 Aluno",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.title("Visão 360 Aluno")
st.write(
    """
    Bem-vindo ao Visão 360 Aluno! Utilize o menu ao lado para navegar entre as páginas.
    """
)

st.markdown("### Páginas Disponíveis")
st.write("- **Sobre o modelo:** Informações detalhadas sobre o modelo de previsão do INDE.")
st.write("- **Previsão INDE:** Insira o ID do aluno para visualizar a previsão do INDE.")
st.write("- **Filtrar DataFrame:** Interaja com os dados utilizando filtros personalizados.")