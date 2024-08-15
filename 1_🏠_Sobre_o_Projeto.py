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

st.subheader("Metodologia")

st.write("""
Para acompanhar e analisar a evolução da performance dos alunos da Passos Mágicos foi utilizado um indicador chamado **INDE - Índice de Desenvolvimento Educacional**.

Este indicador é composto pela combinação de uma série de outros indicadores que avaliam por si só alguns aspectos das dimensões acadêmica, psicossocial ou psicopedagógica.
Essas dimensões avaliadas correspondem às dimensões as quais são impactadas pelas ações da associação Passos Mágicos.

Como a coleta dos indicadores é feita a cada ano, eles assumem pesos diferentes no cálculo do INDE de acordo com a fase em que cada aluno se encontra. 

Abaixo temos uma descrição e divisão das fases consideradas:
         

| Fase  | Etapa Correspondente |
| :------------: | :--------------- |
| 0 | Alfabetização |
| 1 | 2° ano ao 4° ano do ensino fundamental |
| 2 | 5° ano ao 6° ano do ensino fundamental |
| 3 | 7° ano ao 8° ano do ensino fundamental |
| 4 | 9° ano do ensino fundamental |
| 5 | 1° ano do ensino médio |
| 6 | 2° ano do ensino médio |
| 7 | 3° ano do ensino médio |
| 8 | Bolsista universitário |
         
No quadro seguinte mostramos os pesos de cada indicador por fases e uma breve descrição do que cada indicador busca representar:
""")

image =  Image.open("./img/Pesos.jpg")
st.image(image, caption="Pesos e Descrição da representação de cada indicador", width=1200)

st.write("""
Umas vez que todos os indicadores foram alimentados pela coleta dos dados, estes serão utilizados para produzirem o indicador INDE. 
Abaixo segue a fórmula de calculo:
""")

image =  Image.open("./img/formula.jpg")
st.image(image, caption="Fórmula de cálculo do INDE.", width=900)


st.subheader("Sobre os Dados")

st.write("""
Os dados utilizados abrangem os anos de 2020, 2021 e 2022, e foram fornecidos pela Passos Mágicos de forma anonimizada. 
Esses dados incluem informações como nome, turma, ano de pesquisa, fase, pedra e principais KPIs dos alunos.

Embora a base contenha uma gama mais ampla de informações, selecionamos apenas os dados essenciais para realizar uma análise 
individual detalhada, mantendo o foco na singularidade de cada aluno.
""")

st.write("""
Abaixo temos um quadro mostrando os indicadores e a origem das informações para a formação de cada um deles.
""")

image =  Image.open("./img/indicadores.png")
st.image(image, caption="Indicadores que fazem parte do cálculo do INDE.", width=900)

st.subheader("Apresentação das informações")

st.write("""
Além da visão dos indicadores do aluno mostrados em um gráfico radar, exibimos também na sessão "Visão Aluno 360°" uma classificação de sua performance com base na média e desvio padrão geral dos alunos daquela fase, porém não de forma discreta e sim em forma de conceito como é feito na pesquisa PEDE.

A pesquisa PEDE quebra o range de notas de cada fase em 4 segmentos e cada um deles recebe um nome de uma pedra.
Dessa forma assim fica a classificação:
         
| Range de Pontuação  | Pedra |
| :------------: | :--------------- |
| Entre MVO e M - DP - 0,001  | Quartzo |
| Entre M - DP e M | Ágata |
| Entre M e M + DP | Ametista |
| Entre M + DP + 0,001 e VMO | Topázio |
         
Onde:

- MVO: Menor valor observado
- M: Média
- DP: Desvio padrão
- VMO: Valor máximo observado
""")