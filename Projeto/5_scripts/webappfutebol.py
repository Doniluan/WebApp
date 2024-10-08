import streamlit as st
import pandas as pd
from datetime import datetime

st.write(
    """
    **Futebol Web App**
    """
)

st.sidebar.header('Escolha os times')

# Função para carregar os dados
def get_data():
    path = '../2_bases_tratadas/futebol2.csv'
    return pd.read_csv(path, sep=';')

# Carregar os dados
df = get_data()

# Obter as datas únicas no formato datetime
df['datanova'] = pd.to_datetime(df['datanova'])
df_data = df['datanova'].dt.date.drop_duplicates()

# Definir as datas mínima e máxima
min_data = min(df_data)
max_data = max(df_data)

# Obter a lista de times
times = df['home_team_name'].drop_duplicates()

# Entradas do usuário para datas e time
start_date = st.sidebar.date_input("Digite uma data de início:", min_data)
end_date = st.sidebar.date_input("Digite uma data final:", max_data)

# Garantir que a data de início seja antes da data final
if start_date > end_date:
    st.sidebar.error('A data de início deve ser anterior à data final.')

# Escolher o time
time_escolhido = st.sidebar.selectbox("Escolha o time", times)

# Filtrar o DataFrame com base nas escolhas do usuário
df_filtered = df[(df['home_team_name'] == time_escolhido) 
                 & (df['datanova'].dt.date >= start_date) 
                 & (df['datanova'].dt.date <= end_date)]

# Exibir informações no app
st.header('Time: ' + time_escolhido.upper())
st.write('Gols em casa')

# Verificar se há dados filtrados antes de exibir o gráfico
if not df_filtered.empty:
    st.line_chart(data=df_filtered, x='datanova', y='home_team_goal_count')
else:
    st.write("Nenhum jogo encontrado no intervalo de datas selecionado.")
