import streamlit as st

st.set_page_config(
    page_title="Sobre o Grupo",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="👥"
)

st.title("👤 Sobre o Grupo")
st.markdown("---")

st.subheader("Gustavo França Severino - Data Engineer")
st.write("""
Gustavo é responsável pela engenharia de dados no projeto, utilizando seu conhecimento para garantir a integridade e a 
eficiência dos processos de ETL. Seu foco é otimizar o pipeline de dados, garantindo que as informações sejam processadas 
de maneira rápida e precisa.
""")

st.subheader("Frederico Garcia Costa - Data Engineer")
st.write("""
Frederico, atuando como Data Engineer, colabora na arquitetura e na implementação das soluções de dados. 
Ele é fundamental para assegurar que os dados sejam transformados e disponibilizados de forma a atender 
às necessidades do dashboard, sempre buscando inovações no processamento de dados.
""")

st.subheader("Carolina Pasianot Casetta - BI Specialist")
st.write("""
Carolina é especialista em Business Intelligence e é a responsável por transformar dados brutos em insights acionáveis. 
Ela trabalha na criação dos dashboards e relatórios, focando na visualização de dados que melhor representem os KPIs 
principais de cada aluno.
""")

st.subheader("Jeferson Vieira - Product Owner")
st.write("""
Jeferson é o Product Owner do projeto, sendo o elo entre a equipe técnica e as necessidades do cliente. 
Ele coordena o desenvolvimento do dashboard, garantindo que o produto final esteja alinhado com as expectativas 
e os objetivos estabelecidos pela Passos Mágicos.
""")

st.subheader("Victor Wilson Costa Lamana - Data Engineer")
st.write("""
Victor, como Data Engineer, colabora no desenvolvimento e manutenção das pipelines de dados. 
Seu papel é crucial para garantir que os dados fluam de forma contínua e que o dashboard receba as informações 
corretas em tempo hábil.
""")
