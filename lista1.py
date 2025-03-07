import streamlit as st

# Container para os inputs da receita
with st.container():
    st.header("Dados de Entrada da Receita")
    
    # Dados do leite condensado
    qtd_leite = st.number_input(
        "Digite a quantidade de latas/caixas de leite condensado:",
        min_value=0, step=1, format="%d"
    )
    g_leite = st.number_input(
        "Digite a quantidade de gramas de cada lata/caixa de leite condensado:",
        min_value=0.0, step=0.1, format="%.1f"
    )
    
    # Dados da farinha
    qtd_xicaras = st.number_input(
        "Digite a quantidade de xícaras de farinha:",
        min_value=0, step=1, format="%d"
    )
    g_xicara = st.number_input(
        "Digite a quantidade de gramas de cada xícara de farinha:",
        min_value=0.0, step=0.1, format="%.1f"
    )
    
    # Dados dos ovos
    qtd_ovos = st.number_input(
        "Digite a quantidade de ovos da receita:",
        min_value=0, step=1, format="%d"
    )

# Cálculo dos totais
total_gl = qtd_leite * g_leite
total_gx = qtd_xicaras * g_xicara

# Container para exibir os resultados
with st.container():
    st.subheader("Resumo da Receita")
    st.write(f"**Leite condensado:** {qtd_leite} lata(s)/caixa(s) com {g_leite} gramas cada. Total: {total_gl} g.")
    st.write(f"**Farinha:** {qtd_xicaras} xícara(s) com {g_xicara} gramas cada. Total: {total_gx} g.")
    st.write(f"**Ovos:** {qtd_ovos} unidade(s)")
