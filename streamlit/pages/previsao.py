import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dados_finais.csv')

def obter_dados_e_previsao(id_aluno):
    df_aluno = df[df['ID_ALUNO'] == id_aluno].sort_values(by='ANO_PESQUISA')
    if df_aluno.empty:
        return None, None, None

    serie_temporal = df_aluno['INDE'].values
    anos = df_aluno['ANO_PESQUISA'].values
    return serie_temporal, anos

def plotar_grafico_inde(serie_temporal, anos, id_aluno):
    plt.figure(figsize=(10, 5))

    plt.plot(anos, serie_temporal, marker='o', linestyle='-', label='INDE Real', color='b')

    plt.legend()
    st.pyplot(plt)


st.title('Previsão do INDE para Alunos')

id_aluno = st.text_input('Insira o ID do aluno:', '')

if id_aluno:
    try:
        id_aluno_int = int(id_aluno)
        serie_temporal, anos = obter_dados_e_previsao(id_aluno_int)
        if serie_temporal is not None:
            st.subheader(f'O INDE previsto para o aluno {id_aluno_int} é:')
            st.markdown("##")
            plotar_grafico_inde(serie_temporal, anos, id_aluno_int)
        else:
            st.write('ID do aluno não encontrado.')
    except ValueError:
        st.write('Por favor, insira um ID válido.')