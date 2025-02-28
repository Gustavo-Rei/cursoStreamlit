import pandas as pd
import streamlit as st

st.title("Formulário de Cadastro de Aluno")
    
with st.form("formulario_aluno"):
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
    st.write(f"**Telefone:** {telefone}")
    st.write(f"**E-mail:** {email}")
    st.write(f"**Data de Nascimento:** {data_nascimento}")

