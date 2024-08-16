import streamlit as st
import PIL.Image as Image

st.set_page_config(
    page_title="Data Exploration",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="👥"
)
with open("./css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
image =  Image.open("./img/passos-magicos.png")
st.image(image)

logo =  Image.open("./img/postech-logo-white.png")
logo2 =  Image.open("./img/postech-logo-white2.png")
st.logo(logo2, link=None, icon_image=logo )

st.title("🧐 Data Exploration")
st.markdown("---")


power_bi_url = "https://app.powerbi.com/reportEmbed?reportId=9543c85b-5bd3-4a10-b0ac-ad2a6950e2cc&autoAuth=true&ctid=40a64d0b-f2f9-4a34-b1b3-0992ac0e5e4e"


# Instruções sobre o propósito da página
st.markdown("""
    **Bem-vindo à página de Exploração de Dados da Passos Mágicos!** 

    Aqui, você terá acesso a uma análise detalhada dos dados dos nossos alunos, utilizando visualizações interativas para facilitar a compreensão dos principais indicadores de desempenho (KPIs).

    O objetivo desta página é proporcionar uma visão abrangente e intuitiva do progresso dos alunos na Passos Mágicos, de forma global. Destacando tendências importantes e áreas de melhoria. Navegue pelos gráficos e relatórios interativos do Power BI abaixo e explore insights sobre o desenvolvimento dos alunos.

    Esperamos que esta plataforma ajude a acompanhar o impacto do nosso trabalho e a tomar decisões baseadas em dados para promover o sucesso contínuo da Passos Mágicos.
""")


st.markdown(
    f'<iframe width="100%" height="500" src="{power_bi_url}" frameborder="0" allowFullScreen="true"></iframe>',
    unsafe_allow_html=True
)