import streamlit as st

times = ['Palmeiras', 'São Paulo', 'Santos', 'Corinthias']

st.title("Calculadora de Pontuação do Jogo")

time1 = st.selectbox("Selecione o Time 1", times, index=0)
time2 = st.selectbox("Selecione o Time 2", times, index=1)

if time1 == time2:
    st.error("Por favor, selecione times diferentes para a partida.")
else:
    placar_time1 = st.number_input(f"Placar do {time1}", min_value=0, value=0)
    placar_time2 = st.number_input(f"Placar do {time2}", min_value=0, value=0)

    if st.button("Calcular Pontuação"):
        if placar_time1 > placar_time2:
            resultado = f"{time1} venceu e recebe +3 pontos; {time2} perdeu e recebe 0 pontos."
        elif placar_time1 < placar_time2:
            resultado = f"{time2} venceu e recebe +3 pontos; {time1} perdeu e recebe 0 pontos."
        else:
            resultado = "Empate! Ambos os times recebem +1 ponto."
            
        st.write(resultado)
