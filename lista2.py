import streamlit as st

st.title("Lista de Estruturas Condicionais - SweetTech")
st.markdown("Prof. MSc. Denise do Rocio Maciel")

# Seleção do exercício via sidebar
exercicio = st.sidebar.selectbox(
    "Escolha o exercício",
    [
        "Exercício 1 e 2",
        "Exercício 3",
        "Exercício 4",
        "Exercício 5 (apenas IF)",
        "Exercício 6 (IF-ELIF-ELSE)",
        "Exercício 8",
        "Exercício 10"
    ]
)

st.header(exercicio)

# Exercício 1 e 2: Recebe valor e classificação (ativo – 1 ou passivo – 2)
if exercicio == "Exercício 1 e 2":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex1_valor")
    classificacao = st.radio("Digite a classificação:", options=[1, 2], format_func=lambda x: "Ativo" if x == 1 else "Passivo", key="ex1_class")
    if st.button("Calcular", key="ex1_button"):
        if classificacao == 1:
            st.write("Cadastro de ativo realizado com sucesso.")
        elif classificacao == 2:
            st.write("Cadastro de passivo realizado com sucesso.")

# Exercício 3: Se ativo imprime cadastro de ativo; caso contrário, passivo.
if exercicio == "Exercício 3":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex3_valor")
    classificacao = st.radio("Digite a classificação:", options=[1, 2], format_func=lambda x: "Ativo" if x == 1 else "Passivo", key="ex3_class")
    if st.button("Calcular", key="ex3_button"):
        if classificacao == 1:
            st.write("Cadastro de ativo realizado com sucesso.")
        else:
            st.write("Cadastro de passivo realizado com sucesso.")

# Exercício 4: Classificação (ativo - 1, passivo - 2, patrimônio líquido - 3)
if exercicio == "Exercício 4":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex4_valor")
    classificacao = st.radio(
        "Digite a classificação:",
        options=[1, 2, 3],
        format_func=lambda x: "Ativo" if x == 1 else ("Passivo" if x == 2 else "Patrimônio Líquido"),
        key="ex4_class"
    )
    if st.button("Calcular", key="ex4_button"):
        if classificacao == 1:
            st.write("Cadastro de ativo realizado com sucesso.")
        elif classificacao == 2:
            st.write("Cadastro de passivo realizado com sucesso.")
        else:
            st.write("Cadastro de patrimônio líquido realizado com sucesso.")

# Exercício 5: Usando apenas IF (bem – 1, direito – 2, obrigação com terceiro – 3, obrigação com sócio – 4)
if exercicio == "Exercício 5 (apenas IF)":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex5_valor")
    descricao = st.radio(
        "Digite a descrição:",
        options=[1, 2, 3, 4],
        format_func=lambda x: {1: "Bem", 2: "Direito", 3: "Obrigação com Terceiro", 4: "Obrigação com Sócio"}[x],
        key="ex5_desc"
    )
    if st.button("Calcular", key="ex5_button"):
        # Utilizando apenas IF para cada condição (não mutuamente exclusivos)
        if descricao == 1 or descricao == 2:
            st.write("Cadastro de ativo realizado com sucesso.")
        if descricao == 3:
            st.write("Cadastro de passivo realizado com sucesso.")
        if descricao == 4:
            st.write("Cadastro de patrimônio líquido realizado com sucesso.")

# Exercício 6: Usando IF-ELIF-ELSE (mesma lógica do exercício 5)
if exercicio == "Exercício 6 (IF-ELIF-ELSE)":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex6_valor")
    descricao = st.radio(
        "Digite a descrição:",
        options=[1, 2, 3, 4],
        format_func=lambda x: {1: "Bem", 2: "Direito", 3: "Obrigação com Terceiro", 4: "Obrigação com Sócio"}[x],
        key="ex6_desc"
    )
    if st.button("Calcular", key="ex6_button"):
        if descricao == 1 or descricao == 2:
            st.write("Cadastro de ativo realizado com sucesso.")
        elif descricao == 3:
            st.write("Cadastro de passivo realizado com sucesso.")
        else:
            st.write("Cadastro de patrimônio líquido realizado com sucesso.")

# Exercício 8: Verifica valor e sua classificação com base no sinal (ativo - 1, passivo - 2)
if exercicio == "Exercício 8":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex8_valor")
    classificacao = st.radio(
        "Digite a classificação:",
        options=[1, 2],
        format_func=lambda x: "Ativo" if x == 1 else "Passivo",
        key="ex8_class"
    )
    if st.button("Calcular", key="ex8_button"):
        if classificacao == 1:
            if valor < 0:
                st.write(f"Cadastro de crédito no ativo - valor de {abs(valor)} realizado com sucesso.")
            else:
                st.write(f"Cadastro de débito no ativo - valor de {valor} realizado com sucesso.")
        elif classificacao == 2:
            if valor < 0:
                st.write(f"Cadastro de débito no passivo - valor de {abs(valor)} realizado com sucesso.")
            else:
                st.write(f"Cadastro de crédito no passivo - valor de {valor} realizado com sucesso.")

# Exercício 10: Recebe valor, descrição e classificação
if exercicio == "Exercício 10":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex10_valor")
    descricao = st.radio(
        "Digite a descrição:",
        options=[1, 2, 3, 4],
        format_func=lambda x: {1: "Bem", 2: "Direito", 3: "Obrigação com Terceiro", 4: "Obrigação com Sócio"}[x],
        key="ex10_desc"
    )
    classificacao = st.radio(
        "Digite a classificação:",
        options=[1, 2, 3],
        format_func=lambda x: "Ativo" if x == 1 else ("Passivo" if x == 2 else "Patrimônio Líquido"),
        key="ex10_class"
    )
    if st.button("Calcular", key="ex10_button"):
        if classificacao == 1:
            if descricao == 1:
                st.write("Cadastro de ativo do tipo 'bem' realizado com sucesso.")
            else:
                st.write("Cadastro de ativo do tipo 'direito' realizado com sucesso.")
        elif classificacao == 2:
            if descricao == 3:
                st.write("Cadastro de passivo do tipo 'obrigações com terceiros' realizado com sucesso.")
            else:
                st.write("Cadastro de passivo do tipo 'obrigações com sócios' realizado com sucesso.")
        else:
            st.write("Cadastro para patrimônio líquido realizado com sucesso.")
