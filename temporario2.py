import pandas as pd
import streamlit as st

st.title("Formulário de Cadastro de Aluno")

# Inicializa a lista de alunos na session_state, se ainda não existir
if "dados_alunos" not in st.session_state:
    st.session_state["dados_alunos"] = []

with st.form("formulario_aluno", clear_on_submit=True):
    nome = st.text_input("Nome Completo")
    cpf = st.number("CPF")
    rg = st.number("RG")
    ra = st.number("RA")
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
    
    # Adiciona os dados do aluno à lista de respostas na session_state
    st.session_state["dados_alunos"].append(dados_aluno)
    
    # Converte a lista de dicionários para um DataFrame do pandas
    df_alunos = pd.DataFrame(st.session_state["dados_alunos"])
    
    # Exibindo o DataFrame com todas as respostas armazenadas
    st.write("### Dados Armazenados")
    st.dataframe(df_alunos)
