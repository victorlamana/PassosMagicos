import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carrega os dados do CSV
df = pd.read_csv("dataset/dados_finais.csv")

# Função para obter e plotar dados do aluno com diferença percentual
def exibir_grafico_inde(df, id_aluno):
    df_aluno = df[df['ID_ALUNO'] == id_aluno].sort_values(by='ANO_PESQUISA')
    
    if not df_aluno.empty:
        anos = df_aluno['ANO_PESQUISA'].values
        inde = df_aluno['INDE'].values
        
        plt.figure(figsize=(10, 5))
        plt.plot(anos, inde, marker='o', linestyle='-', color='b', label='INDE Real')
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

# Configuração da página no Streamlit
st.title('Previsão do INDE para Alunos')

# Solicita o ID do aluno ao usuário
id_aluno = st.text_input('Insira o ID do aluno:', '')

# Verifica se o usuário inseriu algum valor no campo de texto e tenta exibir o gráfico
if id_aluno:
    try:
        exibir_grafico_inde(df, int(id_aluno))
    except ValueError:
        st.write('Por favor, insira um ID válido.')
