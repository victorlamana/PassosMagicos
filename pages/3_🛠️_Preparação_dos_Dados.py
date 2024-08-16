# notebook_page.py
import streamlit as st
import streamlit.components.v1 as components
import base64
import PIL.Image as Image

st.set_page_config(
    page_title="Preparação dos Dados",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🛠️"
)
with open("./css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
image =  Image.open("./img/passos-magicos.png")
st.image(image)

logo =  Image.open("./img/postech-logo-white.png")
logo2 =  Image.open("./img/postech-logo-white2.png")
st.logo(logo2, link=None, icon_image=logo )

st.title("🛠️ Preparação dos Dados")
st.markdown("---")

st.write("""
Nesta página, apresentamos todo o processo de transformação do DataFrame, desde a sua versão inicial até a forma final 
que é utilizada nos relatórios exibidos nesta aplicação. Aqui, você poderá acompanhar cada etapa de manipulação, limpeza, 
e agregação de dados, detalhando como as informações foram refinadas para fornecer as análises mais precisas e relevantes 
possíveis.
""")

# Path to your HTML file
html_file_path = "dataset/DATAPREP.html"
sql_file_path = "dataset/script.sql"

# Read the HTML file with a specified encoding
try:
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
except UnicodeDecodeError:
    st.error("Error reading the HTML file. Please check the file encoding.")

# Convert HTML content to Data URI
encoded_html = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
data_uri = f"data:text/html;base64,{encoded_html}"

# Display the HTML content in Streamlit using an iframe
st.markdown(f"""
    <iframe src="{data_uri}" style="width:100%; height:1200px; border:none;"></iframe>
""", unsafe_allow_html=True)





try:
    with open(sql_file_path, 'r', encoding='utf-8') as sql_file:
        sql_query = sql_file.read()
except FileNotFoundError:
    st.error(f"O arquivo {sql_file_path} não foi encontrado.")
except Exception as e:
    st.error(f"Ocorreu um erro ao ler o arquivo: {e}")
else:
    # Exibir o conteúdo do arquivo .sql em uma seção de código formatada
    st.subheader("Script de transformação aplicado no PBI:")
    st.code(sql_query, language='sql')