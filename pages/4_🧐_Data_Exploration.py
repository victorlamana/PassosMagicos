import streamlit as st
import streamlit.components.v1 as components
import PIL.Image as Image

st.set_page_config(
    page_title="Data Exploration",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="👥"
)

# Importando estilos CSS
with open("./css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Exibindo imagem principal
image = Image.open("./img/passos-magicos.png")
st.image(image)

# Exibindo logos
logo = Image.open("./img/postech-logo-white.png")
logo2 = Image.open("./img/postech-logo-white2.png")
st.logo(logo2, link=None, icon_image=logo)

# Título da página
st.title("🧐 Data Exploration")
st.markdown("---")

# Instruções sobre o propósito da página
st.markdown("""
    **Bem-vindo à página de Exploração de Dados da Passos Mágicos!** 

    Aqui, você terá acesso a uma análise detalhada dos dados dos nossos alunos, utilizando visualizações interativas para facilitar a compreensão dos principais indicadores de desempenho (KPIs).

    O objetivo desta página é proporcionar uma visão abrangente e intuitiva do progresso dos alunos na Passos Mágicos, de forma global. Destacando tendências importantes e áreas de melhoria. Navegue pelos gráficos e relatórios interativos do Power BI abaixo e explore insights sobre o desenvolvimento dos alunos.

    Esperamos que esta plataforma ajude a acompanhar o impacto do nosso trabalho e a tomar decisões baseadas em dados para promover o sucesso contínuo da Passos Mágicos.
""")

# Incorporar o Dashboard do Power BI
# Substitua 'your_power_bi_report_url' pela URL do seu relatório do Power BI
power_bi_report_url = "https://app.powerbi.com/view?r=eyJrIjoiNDA4NWQ1ODUtMzY0MC00YTBjLWFiZDAtYWM2ODkwMGJlYzRjIiwidCI6IjExZGJiZmUyLTg5YjgtNDU0OS1iZTEwLWNlYzM2NGU1OTU1MSIsImMiOjR9"
components.iframe(power_bi_report_url, height=640, scrolling=True)