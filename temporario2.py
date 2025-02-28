import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados\import streamlit as st  # Importa o Streamlit para criar a interface web

# Define o título da aplicação
st.title("Formulário de Cadastro de Aluno")

# Inicializa a lista de alunos na session_state, se ainda não existir
if "dados_alunos" not in st.session_state:
    st.session_state["dados_alunos"] = []  # Cria uma lista vazia para armazenar os alunos

# Criação do formulário dentro de um bloco 'with'
with st.form("formulario_aluno", clear_on_submit=True):
    nome = st.text_input("Nome Completo")  # Campo de entrada para o nome do aluno
    cpf = st.text_input("CPF")  # Campo de entrada para o CPF
    rg = st.text_input("RG")  # Campo de entrada para o RG
    ra = st.text_input("RA")  # Campo de entrada para o RA
    email = st.text_input("E-mail")  # Campo de entrada para o e-mail
    data_nascimento = st.date_input("Data de Nascimento")  # Campo de entrada para a data de nascimento
    
    enviado = st.form_submit_button("Enviar")  # Botão para enviar o formulário

# Quando o botão "Enviar" for pressionado
if enviado:
    st.success("Dados enviados com sucesso!")  # Exibe uma mensagem de sucesso
    
    # Exibe os dados enviados
    st.write("### Dados do Aluno")
    st.write(f"**Nome:** {nome}")
    st.write(f"**CPF:** {cpf}")
    st.write(f"**RG:** {rg}")
    st.write(f"**RA:** {ra}")
    st.write(f"**E-mail:** {email}")
    st.write(f"**Data de Nascimento:** {data_nascimento}")

    # Armazena os dados do aluno em um dicionário
    dados_aluno = {
        "Nome": nome,
        "CPF": cpf,
        "RG": rg,
        "RA": ra,
        "E-mail": email,
        "Data de Nascimento": data_nascimento,
    }
    
    # Adiciona os dados do aluno à lista armazenada no session_state
    st.session_state["dados_alunos"].append(dados_aluno)
    
    # Converte a lista de dicionários para um DataFrame do pandas
    df_alunos = pd.DataFrame(st.session_state["dados_alunos"])
    
    # Exibe os dados armazenados em formato de tabela
    st.write("### Dados Armazenados")
    st.dataframe(df_alunos)
