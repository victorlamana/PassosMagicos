import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset\dados_finais.csv")

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

st.title('Previsão do INDE para Alunos')

# Solicita o ID do aluno ao usuário
id_aluno = st.text_input('Insira o ID do aluno:', '')

# Verifica se o usuário inseriu algum valor no campo de texto
if id_aluno:
    try:
        # Tenta converter o ID do aluno para inteiro
        id_aluno_int = int(id_aluno)

        # Obtém os dados do aluno
        serie_temporal, anos = obter_dados_e_previsao(df, id_aluno_int)

        # Se os dados foram encontrados, exibe o gráfico
        if serie_temporal is not None:
            st.subheader(f'Evolução do INDE para o aluno {id_aluno_int}:')
            plotar_grafico_inde(serie_temporal, anos)
        else:
            st.write('ID do aluno não encontrado.')
    except ValueError:
        st.write('Por favor, insira um ID válido.')