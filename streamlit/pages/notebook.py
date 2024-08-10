# notebook_page.py
import streamlit as st
import streamlit.components.v1 as components
import base64


st.title("Embedded Notebook")

# Path to your HTML file
html_file_path = 'E:\git\PERSONAL\POSTECH\OTHER\streamlit\pages\datathon_prep.html'

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