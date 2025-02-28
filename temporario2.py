import pandas as pd
import streamlit as st

st.title("Formulário de Cadastro de Aluno")

with st.form("formulario_aluno", clear_on_submit=True):
    nome = st.text_input("Nome Completo")
    cpf = st.text_input("CPF")
    rg = st.text_input("RG")
    ra = st.text_input("RA")
    email = st.text_input("E-mail")
    data_nascimento = st.date_input("Data de Nascimento")
    
    enviado = st.form_submit_button("Enviar")

if enviado:
    st.success("Dados enviados com sucesso!")
    st.write("### Dados do Aluno")
    st.write(f"**Nome:** {nome}")
    st.write(f"**CPF:** {cpf}")
    st.write(f"**RG:** {rg}")
    st.write(f"**RA:** {ra}")
    st.write(f"**E-mail:** {email}")
    st.write(f"**Data de Nascimento:** {data_nascimento}")

    # Armazenando os dados do usuário em um dicionário
    dados_aluno = {
        "Nome": nome,
        "CPF": cpf,
        "RG": rg,
        "RA": ra,
        "E-mail": email,
        "Data de Nascimento": data_nascimento,
    }
    
    # Convertendo o dicionário para um DataFrame do pandas
    df_aluno = pd.DataFrame([dados_aluno])
    
    # Exibindo o DataFrame
    st.write("### Dados Armazenados")
    st.dataframe(df_aluno)
