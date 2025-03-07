import streamlit as st

st.title("Dados da Receita")

# Container para dados do leite condensado
with st.container():
    st.header("Leite Condensado")
    quantidade_leite = st.number_input(
        "Digite a quantidade de latas/caixas de leite condensado:", 
        min_value=0, step=1, format="%d"
    )
    gramas_leite = st.number_input(
        "Digite a quantidade de gramas por lata/caixa:", 
        min_value=0.0, step=1.0
    )

# Container para dados da farinha
with st.container():
    st.header("Farinha")
    quantidade_xicaras = st.number_input(
        "Digite a quantidade de xícaras de farinha:", 
        min_value=0, step=1, format="%d"
    )
    gramas_xicara = st.number_input(
        "Digite a quantidade de gramas por xícara:", 
        min_value=0.0, step=1.0
    )

# Container para dados dos ovos
with st.container():
    st.header("Ovos")
    quantidade_ovos = st.number_input(
        "Digite a quantidade de ovos:", 
        min_value=0, step=1, format="%d"
    )

# Container para exibir os valores recebidos
with st.container():
    st.header("Valores Recebidos")
    st.write("Latas/caixas de leite condensado:", quantidade_leite)
    st.write("Gramas por lata/caixa:", gramas_leite)
    st.write("Xícaras de farinha:", quantidade_xicaras)
    st.write("Gramas por xícara de farinha:", gramas_xicara)
    st.write("Quantidade de ovos:", quantidade_ovos)
