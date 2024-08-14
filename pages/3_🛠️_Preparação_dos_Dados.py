# notebook_page.py
import streamlit as st
import streamlit.components.v1 as components
import base64

st.set_page_config(
    page_title="Preparação dos Dados",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🛠️"
)
st.title("🛠️ Preparação dos Dados")
st.markdown("---")

st.write("""
Nesta página, apresentamos todo o processo de transformação do DataFrame, desde a sua versão inicial até a forma final 
que é utilizada nos relatórios exibidos nesta aplicação. Aqui, você poderá acompanhar cada etapa de manipulação, limpeza, 
e agregação de dados, detalhando como as informações foram refinadas para fornecer as análises mais precisas e relevantes 
possíveis.
""")

# Path to your HTML file
html_file_path = "dataset\DATAPREP.html"

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