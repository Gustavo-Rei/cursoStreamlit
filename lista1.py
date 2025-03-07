import streamlit as st

st.title("Dados da Receita")

with st.container():
    st.header("Leite Condensado")
    qtdLeite = st.number_input(
        "Digite a quantidade de latas/caixas de leite condensado:",
        min_value=0, step=1, format="%d"
    )
    gLeite = st.number_input(
        "Digite a quantidade de gramas de cada lata/caixa de leite condensado:",
        min_value=0.0, step=1.0
    )
    totalGL = qtdLeite * gLeite
    st.write("Total de gramas de leite condensado:", totalGL, "g")

with st.container():
    st.header("Farinha")
    qtdXicaras = st.number_input(
        "Digite a quantidade de xícaras de farinha:",
        min_value=0, step=1, format="%d"
    )
    gXicara = st.number_input(
        "Digite a quantidade de gramas de cada xícara de farinha:",
        min_value=0.0, step=1.0
    )
    totalGX = qtdXicaras * gXicara
    st.write("Total de gramas de farinha:", totalGX, "g")

with st.container():
    st.header("Ovos")
    qtdOvos = st.number_input(
        "Digite a quantidade de ovos da receita:",
        min_value=0, step=1, format="%d"
    )

with st.container():
    st.header("Resumo da Receita")
    st.write(f"Leite condensado: {qtdLeite} lata(s)/caixa(s) com {gLeite} gramas cada. Total: {totalGL} g.")
    st.write(f"Farinha: {qtdXicaras} xícara(s) com {gXicara} gramas cada. Total: {totalGX} g.")
    st.write(f"Ovos: {qtdOvos} unidade(s)")
