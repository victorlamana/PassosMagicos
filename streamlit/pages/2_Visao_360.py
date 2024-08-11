import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
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
        imagem = Image.open(f'dataset/images/{nome_pedra}.png')
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
        max_size = 200
        colunas = st.columns(len(pedras_por_ano))
        for idx, row in enumerate(pedras_por_ano.itertuples()):
            tamanho = max_size // (2 ** idx)
            imagem_pedra = carrega_imagem_pedra(row.PEDRA, tamanho)
            if imagem_pedra:
                with colunas[idx]:
                    st.image(imagem_pedra, caption=f"Pedra: {row.PEDRA} ({row.ANO_PESQUISA})")


def obter_dados_e_previsao(df, id_aluno):
    df_aluno = df[df['ID_ALUNO'] == id_aluno].sort_values(by='ANO_PESQUISA')
    if df_aluno.empty:
        return None, None

    serie_temporal = df_aluno['INDE'].values
    anos = df_aluno['ANO_PESQUISA'].values
    return serie_temporal, anos

def plotar_grafico_inde(serie_temporal, anos):
    plt.figure(figsize=(10, 5))
    plt.plot(anos, serie_temporal, marker='o', linestyle='-', label='INDE Real', color='b')
    plt.xlabel('Ano')
    plt.ylabel('INDE')
    plt.title('Evolução do INDE ao longo dos anos')
    plt.legend()
    st.pyplot(plt)

###################################################################################################################

# Carrega os dados do CSV
df = pd.read_csv("dataset/dados_finais.csv")

# Configuração da página no Streamlit
st.set_page_config(page_title="Visão 360 Aluno", layout="wide", initial_sidebar_state="expanded")

st.title('Visão 360 do Aluno')
st.markdown("---")

# Solicitação do ID do aluno
id_aluno = st.text_input('Insira o ID do aluno:', '')

if id_aluno:
    try:
        id_aluno_int = int(id_aluno)
        dfaluno = df[df['ID_ALUNO'] == id_aluno_int]

        if dfaluno.empty:
            st.warning("ID do aluno não encontrado.")
        else:
            st.subheader("Pedras por Ano")
            exibe_pedras_por_ano(dfaluno)

            dfs_por_ano = split_df_por_ano(dfaluno)
            df_yoy = gera_yoy_df(dfaluno)

            for ano, df_ano in dfs_por_ano.items():
                st.subheader(f'Análise de KPIs para o ano {ano}')
                fig = px.line_polar(
                    df_ano, 
                    r="NOTA", 
                    theta="INDICE", 
                    color="TIPO",
                    line_close=True, 
                    color_discrete_sequence=px.colors.qualitative.Plotly,
                    template="plotly_dark"
                )
                st.plotly_chart(fig)

            st.subheader('Overview anual')
            fig = px.line_polar(
                df_yoy, 
                r="NOTA", 
                theta="INDICE", 
                color="ANO_PESQUISA",
                line_close=True, 
                color_discrete_sequence=px.colors.qualitative.Plotly,
                template="plotly_dark"
            )
            st.plotly_chart(fig)

    except ValueError:
        st.error("Por favor, insira um ID válido.")
