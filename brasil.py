import streamlit as st
import pandas as pd

# Lista de times
teams = ['Palmeiras', 'São Paulo', 'Santos', 'Corinthias']

# inicializa os dados dos times
if 'stats' not in st.session_state:
    st.session_state.stats = {
        team: {
            "Pontos": 0,
            "Partidas": 0,
            "Gols Marcados": 0,
            "Gols Sofridos": 0,
            "Saldo de Gols": 0
        } for team in teams
    }

st.title("Calculadora de Pontuação do Jogo")

# seção para seleção de times e registro do placar
time1 = st.selectbox("Selecione o Time 1", teams, index=0)
time2 = st.selectbox("Selecione o Time 2", teams, index=1)

if time1 == time2:
    st.error("Por favor, selecione times diferentes para a partida.")
else:
    placar_time1 = st.number_input(f"Placar do {time1}", min_value=0, value=0)
    placar_time2 = st.number_input(f"Placar do {time2}", min_value=0, value=0)
    
    if st.button("Registrar Jogo"):
        # Atualiza pontos conforme o resultado do jogo
        if placar_time1 > placar_time2:
            st.write(f"{time1} venceu e recebe +3 pontos; {time2} perdeu e recebe 0 pontos.")
            st.session_state.stats[time1]["Pontos"] += 3
        elif placar_time1 < placar_time2:
            st.write(f"{time2} venceu e recebe +3 pontos; {time1} perdeu e recebe 0 pontos.")
            st.session_state.stats[time2]["Pontos"] += 3
        else:
            st.write("Empate! Ambos os times recebem +1 ponto.")
            st.session_state.stats[time1]["Pontos"] += 1
            st.session_state.stats[time2]["Pontos"] += 1

        # atualiza infomações do time1
        st.session_state.stats[time1]["Partidas"] += 1
        st.session_state.stats[time1]["Gols Marcados"] += placar_time1
        st.session_state.stats[time1]["Gols Sofridos"] += placar_time2
        st.session_state.stats[time1]["Saldo de Gols"] = (
            st.session_state.stats[time1]["Gols Marcados"] - st.session_state.stats[time1]["Gols Sofridos"]
        )

        # atualiza informações dp time2
        st.session_state.stats[time2]["Partidas"] += 1
        st.session_state.stats[time2]["Gols Marcados"] += placar_time2
        st.session_state.stats[time2]["Gols Sofridos"] += placar_time1
        st.session_state.stats[time2]["Saldo de Gols"] = (
            st.session_state.stats[time2]["Gols Marcados"] - st.session_state.stats[time2]["Gols Sofridos"]
        )

# montagem da tabela de classificação
st.subheader("Tabela de Classificação")

df = pd.DataFrame(st.session_state.stats).T.reset_index()
df = df.rename(columns={"index": "Time"})

# reorganiza informações da tabela
df = df[["Time", "Pontos", "Partidas", "Gols Marcados", "Gols Sofridos", "Saldo de Gols"]]
df = df.sort_values(by=["Pontos", "Saldo de Gols", "Gols Marcados"], ascending=False).reset_index(drop=True)
df.index += 1  # primeira posição = 1

# exibição da tabela
st.dataframe(df)
