import streamlit as st

st.set_page_config(
    page_title="Sobre o Projeto",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🏠"
)

st.title("🏠 Sobre o Projeto")
st.markdown("---")

st.subheader("Qual foi a idéia por trás do projeto?")

st.write("""
Nosso objetivo com este dashboard é criar uma visão abrangente e personalizada para cada aluno da Passos Mágicos. 
Com base nos conceitos de reconhecimento individual, valorização singular e análise exclusiva, buscamos contar a 
história única de cada aluno por meio de gráficos que destacam seus principais indicadores de desempenho (KPIs).
""")

st.subheader("Sobre os Dados")

st.write("""
Os dados utilizados abrangem os anos de 2020, 2021 e 2022, e foram fornecidos pela Passos Mágicos de forma anonimizada. 
Esses dados incluem informações como nome, turma, ano de pesquisa, fase, pedra e principais KPIs dos alunos.

Embora a base contenha uma gama mais ampla de informações, selecionamos apenas os dados essenciais para realizar uma análise 
individual detalhada, mantendo o foco na singularidade de cada aluno.
""")