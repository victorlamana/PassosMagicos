import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# Função para dividir o DataFrame por ano de pesquisa
def split_df_por_ano(df):
    dataframes = {}
    for _, row in df.iterrows():
        ano_pesquisa = row['ANO_PESQUISA']
        data = {
            'INDICE': ['IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN'] * 3,
            'TIPO': ['ALUNO'] * 7 + ['MEDIA_FASE'] * 7 + ['MEDIA_TURMA'] * 7,
            'NOTA': [
                row['IAA'], row['IEG'], row['IPS'], row['IDA'], row['IPP'], row['IPV'], row['IAN'],
                row['IAA_MEDIO_ANO_FASE'], row['IEG_MEDIO_ANO_FASE'], row['IPS_MEDIO_ANO_FASE'], 
                row['IDA_MEDIO_ANO_FASE'], row['IPP_MEDIO_ANO_FASE'], row['IPV_MEDIO_ANO_FASE'], 
                row['IAN_MEDIO_ANO_FASE'],
                row['IAA_MEDIO_ANO_FASE_TURMA'], row['IEG_MEDIO_ANO_FASE_TURMA'], row['IPS_MEDIO_ANO_FASE_TURMA'], 
                row['IDA_MEDIO_ANO_FASE_TURMA'], row['IPP_MEDIO_ANO_FASE_TURMA'], row['IPV_MEDIO_ANO_FASE_TURMA'], 
                row['IAN_MEDIO_ANO_FASE_TURMA']
            ]
        }
        dataframes[ano_pesquisa] = pd.DataFrame(data)
    return dataframes

# Função para gerar um DataFrame year-over-year (YoY)
def gera_yoy_df(df):
    data = {
        'INDICE': [],
        'ANO_PESQUISA': [],
        'NOTA': []
    }
    for _, row in df.iterrows():
        indices = ['IAA', 'IEG', 'IPS', 'IDA', 'IPP', 'IPV', 'IAN']
        data['INDICE'].extend(indices)
        data['ANO_PESQUISA'].extend([row['ANO_PESQUISA']] * len(indices))
        data['NOTA'].extend([row[indice] for indice in indices])

    return pd.DataFrame(data)

# Função para carregar as imagens das pedras
def carrega_imagem_pedra(nome_pedra, tamanho):
    try:
        imagem = Image.open(f'dataset\images\{nome_pedra}.png')
        imagem = imagem.resize((tamanho, tamanho))
        return imagem
    except FileNotFoundError:
        st.write(f"Imagem para a pedra {nome_pedra} não encontrada.")
        return None

# Função para exibir as pedras em linha
def exibe_pedras_por_ano(dfaluno):
    pedras_por_ano = dfaluno[['ANO_PESQUISA', 'PEDRA']].drop_duplicates()
    pedras_por_ano = pedras_por_ano.sort_values(by='ANO_PESQUISA', ascending=False)

    if not pedras_por_ano.empty:
        # Configura o tamanho máximo da imagem
        max_size = 200
        # Lista para armazenar as colunas para cada pedra
        colunas = st.columns(len(pedras_por_ano))
        for idx, row in enumerate(pedras_por_ano.itertuples()):
            tamanho = max_size // (2 ** idx)  # Reduz o tamanho da imagem para cada ano anterior
            imagem_pedra = carrega_imagem_pedra(row.PEDRA, tamanho)
            if imagem_pedra:
                with colunas[idx]:
                    st.image(imagem_pedra, caption=f"Pedra: {row.PEDRA} ({row.ANO_PESQUISA})")

# Carrega os dados do CSV
df = pd.read_csv("dataset/dados_finais.csv")

# Configuração da página no Streamlit
st.title('Visão 360 do Aluno')

# Solicitação do ID do aluno
id_aluno = st.text_input('Insira o ID do aluno:', '')

if id_aluno:
    try:
        # Converte o ID do aluno para inteiro
        id_aluno_int = int(id_aluno)
        
        # Filtra os dados do aluno
        dfaluno = df[df['ID_ALUNO'] == id_aluno_int]

        if dfaluno.empty:
            st.write("ID do aluno não encontrado.")
        else:
            # Exibe as pedras que o aluno já teve
            st.subheader("Pedras por Ano")
            exibe_pedras_por_ano(dfaluno)

            # Gera os DataFrames para os gráficos
            dfs_por_ano = split_df_por_ano(dfaluno)
            df_yoy = gera_yoy_df(dfaluno)

            # Gera e exibe o primeiro gráfico
            for ano, df_ano in dfs_por_ano.items():
                st.subheader(f'Gráfico Polar para o Ano {ano}')
                fig = px.line_polar(df_ano, r="NOTA", theta="INDICE", color="TIPO",
                                    line_close=True, color_discrete_sequence=px.colors.sequential.Plasma_r,
                                    template="plotly_dark")
                st.plotly_chart(fig)

            # Gera e exibe o segundo gráfico
            st.subheader('Gráfico Polar Year-over-Year (YoY)')
            fig = px.line_polar(df_yoy, r="NOTA", theta="INDICE", color="ANO_PESQUISA",
                                line_close=True, color_discrete_sequence=px.colors.sequential.Plasma_r,
                                template="plotly_dark")
            st.plotly_chart(fig)

    except ValueError:
        st.write("Por favor, insira um ID válido.")
