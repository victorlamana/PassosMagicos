import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import PIL.Image as Image

st.set_page_config(
    page_title="Visão Aluno 360°",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊"
)
with open("./css/style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

image =  Image.open("./img/passos-magicos.png")
st.image(image)

st.title('📊 Visão Aluno 360°')
st.markdown("---")

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

@st.cache_data
def filtra_aluno(id_aluno):
    df = load_data("dataset/dados_finais.csv")
    df_aluno = df[df['ID_ALUNO'] == id_aluno].sort_values(by='ANO_PESQUISA')
    return df_aluno
# Função para dividir o DataFrame por ano de pesquisa
@st.cache_data
def gera_df_comparativo_aluno_medias(df):
    dataframes = {}
    for index, row in df.iterrows():
        ano_pesquisa = row['ANO_PESQUISA']
        data = {
            'Indice': ['IAN', 'IDA', 'IEG', 'IAA', 'IPS', 'IPP','IPV']*3,
            'Legenda': [f'Notas do Aluno ({ano_pesquisa})']*7 + [f'Médias da Fase ({ano_pesquisa})']*7 +[f'Médias da Turma ({ano_pesquisa})']*7,
            'Nota': [df['IAN'][index], df['IDA'][index], df['IEG'][index], df['IAA'][index], df['IPS'][index], df['IPP'][index], df['IPV'][index], df['IAN_MEDIO_ANO_FASE'][index], df['IDA_MEDIO_ANO_FASE'][index], df['IEG_MEDIO_ANO_FASE'][index], df['IAA_MEDIO_ANO_FASE'][index], df['IPS_MEDIO_ANO_FASE'][index], df['IPP_MEDIO_ANO_FASE'][index], df['IPV_MEDIO_ANO_FASE'][index], df['IAN_MEDIO_ANO_FASE_TURMA'][index], df['IDA_MEDIO_ANO_FASE_TURMA'][index], df['IEG_MEDIO_ANO_FASE_TURMA'][index], df['IAA_MEDIO_ANO_FASE_TURMA'][index], df['IPS_MEDIO_ANO_FASE_TURMA'][index], df['IPP_MEDIO_ANO_FASE_TURMA'][index], df['IPV_MEDIO_ANO_FASE_TURMA'][index]]
        }
        novo_df = pd.DataFrame(data)
        dataframes[ano_pesquisa] = novo_df
    return dataframes

# Função para gerar um DataFrame Comparativo Ano a Ano
@st.cache_data
def gera_df_comparativo_anos(df):
    data = {
        'Indice': [],
        'Legenda': [],
        'Nota': []
    }
    for index, row in df.iterrows():
        data['Indice'] += ['IAN', 'IDA', 'IEG', 'IAA', 'IPS', 'IPP','IPV']
        data['Legenda'] += [f"Notas do Aluno ({df['ANO_PESQUISA'][index]})"]*7
        data['Nota'] += [df['IAN'][index],df['IDA'][index],df['IEG'][index],df['IAA'][index],df['IPS'][index],df['IPP'][index],df['IPV'][index]]
    novo_df = pd.DataFrame(data)
    return novo_df

# Função para carregar as imagens das pedras
@st.cache_data
def carrega_imagem_pedra(nome_pedra):
    try:
        imagem = Image.open(f'img/{nome_pedra}.png')
        return imagem
    except FileNotFoundError:
        st.write(f"Imagem para a pedra {nome_pedra} não encontrada.")
        return None

# Função para exibir as pedras em linha
def exibe_pedras_por_ano(df):
    pedras_por_ano = df[['ANO_PESQUISA', 'PEDRA']].drop_duplicates()
    pedras_por_ano = pedras_por_ano.sort_values(by='ANO_PESQUISA', ascending=True)

    pedra2020 = pedras_por_ano[pedras_por_ano['ANO_PESQUISA'] == 2020].PEDRA
    pedra2021 = pedras_por_ano[pedras_por_ano['ANO_PESQUISA'] == 2021].PEDRA
    pedra2022 = pedras_por_ano[pedras_por_ano['ANO_PESQUISA'] == 2022].PEDRA

    col2020, col2021, col2022 = st.columns(3)

    with col2020:
        st.header("2020")
        if not pedra2020.empty:
            imagem_pedra2020 = carrega_imagem_pedra(pedra2020.iloc[0])
            st.image(imagem_pedra2020, caption=f"Pedra: {pedra2020.iloc[0]} (2020)")
    with col2021:
        st.header("2021")
        if not pedra2021.empty:
            imagem_pedra2021 = carrega_imagem_pedra(pedra2021.iloc[0])
            st.image(imagem_pedra2021, caption=f"Pedra: {pedra2021.iloc[0]} (2021)")
    with col2022:
        st.header("2022")
        if not pedra2022.empty:
            imagem_pedra2022 = carrega_imagem_pedra(pedra2022.iloc[0])
            st.image(imagem_pedra2022, caption=f"Pedra: {pedra2022.iloc[0]} (2022)")

    # if not pedras_por_ano.empty:
    #     max_size = 200
    #     colunas = st.columns(len(pedras_por_ano))
    #     for idx, row in enumerate(pedras_por_ano.itertuples()):
    #
    #         imagem_pedra = carrega_imagem_pedra(row.PEDRA)
    #         if imagem_pedra:
    #             with colunas[idx]:
    #                 st.image(imagem_pedra, caption=f"Pedra: {row.PEDRA} ({row.ANO_PESQUISA})")


def exibir_grafico_inde(df):
    if not df.empty:
        anos = df['ANO_PESQUISA'].values
        inde = df['INDE'].values

        plt.figure(figsize=(10, 5))
        plt.plot(anos, inde, marker='o', linestyle='-', color='b', label='INDE')
        plt.xticks(anos)
        plt.xlabel('Ano')
        plt.ylabel('INDE')
        plt.title(f'Evolução do INDE para o aluno {id_aluno}')
        plt.legend()

        # Cálculo da diferença percentual e anotação no gráfico
        for i in range(1, len(anos)):
            diff_percent = ((inde[i] - inde[i-1]) / inde[i-1]) * 100
            diff_text = f"Aumentou {diff_percent:.2f}%" if diff_percent > 0 else f"Diminuiu {diff_percent:.2f}%"
            plt.text(anos[i], inde[i], diff_text, fontsize=9, verticalalignment='bottom', horizontalalignment='right')

        st.pyplot(plt)
    else:
        st.write('ID do aluno não encontrado.')

def gera_grafico_medias(df):
    df_medias = gera_df_comparativo_aluno_medias(df)
    fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'polar'}]*3],x_title="Evolução do Aluno por Ano", subplot_titles=[2020, 2021, 2022])
    for index, key in enumerate(df_medias):
        fig1 = px.line_polar(df_medias[key], r="Nota", theta="Indice", color="Legenda", title=key, line_close=True, markers=True, range_r=[0,10], start_angle=0, direction='counterclockwise')
        fig.add_traces(list(fig1.select_traces()),1,key-2019)

        labels_to_show_in_legend = ["Notas do Aluno", "Médias da Fase", "Médias da Turma"]
        for trace in fig.data[3:]:
            if (trace['name'] in labels_to_show_in_legend):
                trace['showlegend'] = False
                # print(trace)
    # fig.update_layout(
    #     showlegend=False
    # )
    # Plot!
    st.plotly_chart(fig, use_container_width=True)

def gera_grafico_comparativo_anos(df):
    df_yoy = gera_df_comparativo_anos(df)

    fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scatter'}, {'type': 'polar'}]],
                        subplot_titles=('INDE', 'Índices'), x_title="Evolução do Aluno por Ano")
    fig1 = px.line(df, x="ANO_PESQUISA", y="INDE", markers=True, template="plotly_white")
    fig2 = px.line_polar(df_yoy, r="Nota", theta="Indice", color="Legenda",
                         line_close=True, markers=True, range_r=[0,10], start_angle=0, direction='counterclockwise')

    fig.add_traces(list(fig1.select_traces()),1,1)
    fig.add_traces(list(fig2.select_traces()),1,2)
    # Plot!
    st.plotly_chart(fig, use_container_width=True)

###################################################################################################################


# Solicitação do ID do aluno
id_aluno = st.text_input('Insira o ID do aluno:', '')

if id_aluno:
    try:
        id_aluno_int = int(id_aluno)
        df_aluno = filtra_aluno(id_aluno_int)

        if df_aluno.empty:
            st.warning("ID do aluno não encontrado.")
        else:
            st.subheader("Pedras por Ano")
            exibe_pedras_por_ano(df_aluno)
            gera_grafico_medias(df_aluno)
            gera_grafico_comparativo_anos(df_aluno)
    except ValueError:
        st.error("Por favor, insira um ID válido.")
