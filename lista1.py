import streamlit as st

st.title("Calculadora de Receita")

with st.container(border=True):
    st.header("Leite Condensado")
    col1, col2 = st.columns(2)
    with col1:
        qtdLeite = st.number_input(
            "Quantidade de latas/caixas",
            min_value=0,
            step=1,
            format='%d',
            key="leite_qtd"
        )
    with col2:
        gLeite = st.number_input(
            "Gramas por unidade",
            min_value=0.0,
            format='%f',
            key="leite_grams"
        )
    totalGL = qtdLeite * gLeite

with st.container(border=True):
    st.header("Farinha")
    col3, col4 = st.columns(2)
    with col3:
        qtdXicaras = st.number_input(
            "Quantidade de xícaras",
            min_value=0,
            step=1,
            format='%d',
            key="farinha_qtd"
        )
    with col4:
        gXicara = st.number_input(
            "Gramas por xícara",
            min_value=0.0,
            format='%f',
            key="farinha_grams"
        )
    totalGX = qtdXicaras * gXicara

with st.container(border=True):
    st.header("Ovos")
    qtdOvos = st.number_input(
        "Quantidade de ovos",
        min_value=0,
        step=1,
        format='%d',
        key="ovos"
    )

with st.container(border=True):
    st.header("Dados da Receita")
    st.success(f"""
    **Leite condensado:** {qtdLeite} lata(s)/caixa(s) com {gLeite}g cada
    - Total: {totalGL}g
                
    **Farinha:** {qtdXicaras} xícara(s) com {gXicara}g cada
    - Total: {totalGX}g
                
    **Ovos:** {qtdOvos} unidade(s)
    """)
