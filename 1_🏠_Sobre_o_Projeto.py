import streamlit as st
import PIL.Image as Image
st.set_page_config(
    page_title="Sobre o Projeto",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🏠"
)
with open("./css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

image =  Image.open("./img/passos-magicos.png")
st.image(image)

logo =  Image.open("./img/postech-logo-white.png")
logo2 =  Image.open("./img/postech-logo-white2.png")
st.logo(logo2, link=None, icon_image=logo )

st.title("🏠 Sobre o Projeto")
st.markdown("---")

st.subheader("Qual foi a idéia por trás do projeto?")

st.write("""
Nosso objetivo com este dashboard é criar uma visão abrangente e personalizada para cada aluno da Passos Mágicos. 
Com base nos conceitos de reconhecimento individual, valorização singular e análise exclusiva, buscamos contar a 
história única de cada aluno por meio de gráficos que destacam seus principais indicadores de desenvolvimento educacional.
""")
image =  Image.open("./img/indicadores.png")
st.image(image, caption="Indicadores que fazem parte do cálculo do INDE.", width=900)


st.subheader("Sobre os Dados")

st.write("""
Os dados utilizados abrangem os anos de 2020, 2021 e 2022, e foram fornecidos pela Passos Mágicos de forma anonimizada. 
Esses dados incluem informações como nome, turma, ano de pesquisa, fase, pedra e principais KPIs dos alunos.

Embora a base contenha uma gama mais ampla de informações, selecionamos apenas os dados essenciais para realizar uma análise 
individual detalhada, mantendo o foco na singularidade de cada aluno.
""")