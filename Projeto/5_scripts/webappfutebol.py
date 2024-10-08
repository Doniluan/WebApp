import streamlit as st
import pandas as pd
from datetime import date

st.write(
    """
    **Futebol Wep App**
    """
)

st.sidebar.header('Escolha os times')

def get_data():
    path = './Projeto/2_Bases_Tratadas/futebol2.csv'
    return pd.read_csv(path, sep=';')

df = get_data()
df_data = pd.to_datetime(
    df['datanova']).dt.date.drop_duplicates()

min_data = min(df_data)
max_data = max(df_data)
times = df['home_team_name'].drop_duplicates()

start_date = st.sidebar.text_input(
    "Digite uma data de inicio:", min_data) 
end_date = st.sidebar.text_input(
    "Digite uma data final:", max_data) 

time_escolhido = st.selectbox(
    "Escolha o time", times)

df = df[(df['home_team_name'] == time_escolhido) 
    & (pd.to_datetime(df['datanova']) >= start_date) 
    & (pd.to_datetime(df['datanova']) <= end_date)]

st.header('Time: ' + time_escolhido.upper())
st.write('Gols em casa')
st.line_chart(data=df, 
              x='datanova', 
              y='home_team_goal_count')