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

# Exercício 1 e 2: Ativo (1) ou Passivo (2)
if exercicio == "Exercício 1 e 2":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex1_valor")
    classificacao = st.radio("Classificação:", [1, 2], format_func=lambda x: "Ativo" if x == 1 else "Passivo", key="ex1_class")
    if st.button("Calcular", key="ex1_button"):
        if classificacao == 1:
            st.write("Cadastro de ativo realizado com sucesso.")
        else:
            st.write("Cadastro de passivo realizado com sucesso.")

# Exercício 3: Ativo ou Passivo (com else)
if exercicio == "Exercício 3":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex3_valor")
    classificacao = st.radio("Classificação:", [1, 2], format_func=lambda x: "Ativo" if x == 1 else "Passivo", key="ex3_class")
    if st.button("Calcular", key="ex3_button"):
        if classificacao == 1:
            st.write("Cadastro de ativo realizado com sucesso.")
        else:
            st.write("Cadastro de passivo realizado com sucesso.")

# Exercício 4: Ativo, Passivo ou Patrimônio Líquido
if exercicio == "Exercício 4":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex4_valor")
    classificacao = st.radio(
        "Classificação:",
        [1, 2, 3],
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

# Exercício 5: Apenas IF (descrições)
if exercicio == "Exercício 5 (apenas IF)":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex5_valor")
    descricao = st.radio(
        "Descrição:",
        [1, 2, 3, 4],
        format_func=lambda x: {1: "Bem", 2: "Direito", 3: "Obrigação com Terceiro", 4: "Obrigação com Sócio"}[x],
        key="ex5_desc"
    )
    if st.button("Calcular", key="ex5_button"):
        if descricao in [1, 2]:
            st.write("Cadastro de ativo realizado com sucesso.")
        if descricao == 3:
            st.write("Cadastro de passivo realizado com sucesso.")
        if descricao == 4:
            st.write("Cadastro de patrimônio líquido realizado com sucesso.")

# Exercício 6: IF-ELIF-ELSE (descrições)
if exercicio == "Exercício 6 (IF-ELIF-ELSE)":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex6_valor")
    descricao = st.radio(
        "Descrição:",
        [1, 2, 3, 4],
        format_func=lambda x: {1: "Bem", 2: "Direito", 3: "Obrigação com Terceiro", 4: "Obrigação com Sócio"}[x],
        key="ex6_desc"
    )
    if st.button("Calcular", key="ex6_button"):
        if descricao in [1, 2]:
            st.write("Cadastro de ativo realizado com sucesso.")
        elif descricao == 3:
            st.write("Cadastro de passivo realizado com sucesso.")
        else:
            st.write("Cadastro de patrimônio líquido realizado com sucesso.")

# Exercício 7: A diferença está na quantidade de verificações realizadas pelo programa. Menos verificações e melhor desempenho em casos com múltiplas condições mutuamente exclusivas. (IF-ELIF-ELSE é mais eficiente em condições mutuamente exclusivas.)

# Exercício 8: Formatação monetária e sinal
if exercicio == "Exercício 8":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex8_valor")
    classificacao = st.radio(
        "Classificação:",
        [1, 2],
        format_func=lambda x: "Ativo" if x == 1 else "Passivo",
        key="ex8_class"
    )
    if st.button("Calcular", key="ex8_button"):
        valor_abs = abs(valor)
        # Formatação em R$ (ex: R$ 1.000,00)
        valor_formatado = f"R$ {valor_abs:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        if classificacao == 1:
            operacao = "crédito" if valor < 0 else "débito"
            st.write(f"Cadastro de {operacao} no ativo - valor de {valor_formatado} realizado com sucesso.")
        else:
            operacao = "débito" if valor < 0 else "crédito"
            st.write(f"Cadastro de {operacao} no passivo - valor de {valor_formatado} realizado com sucesso.")

# Exercício 9: Sim, é possível, mas não é recomendado devido à perda de clareza. (É possível, mas a estrutura alinhada é preferível para clareza.)

# Exercício 10: Validação de entradas
if exercicio == "Exercício 10":
    valor = st.number_input("Digite o valor:", value=0.0, key="ex10_valor")
    descricao = st.radio(
        "Descrição:",
        [1, 2, 3, 4],
        format_func=lambda x: {1: "Bem", 2: "Direito", 3: "Obrigação com Terceiro", 4: "Obrigação com Sócio"}[x],
        key="ex10_desc"
    )
    classificacao = st.radio(
        "Classificação:",
        [1, 2, 3],
        format_func=lambda x: "Ativo" if x == 1 else ("Passivo" if x == 2 else "Patrimônio Líquido"),
        key="ex10_class"
    )
    if st.button("Calcular", key="ex10_button"):
        if classificacao == 1:
            if descricao in [1, 2]:
                tipo = "bem" if descricao == 1 else "direito"
                st.write(f"Cadastro de ativo do tipo '{tipo}' realizado com sucesso.")
            else:
                st.error("Erro: Ativo deve ser 'Bem' (1) ou 'Direito' (2).")
        elif classificacao == 2:
            if descricao in [3, 4]:
                tipo = "obrigações com terceiros" if descricao == 3 else "obrigações com sócios"
                st.write(f"Cadastro de passivo do tipo '{tipo}' realizado com sucesso.")
            else:
                st.error("Erro: Passivo deve ser 'Obrigação com Terceiro' (3) ou 'Obrigação com Sócio' (4).")
        elif classificacao == 3:
            if descricao == 4:
                st.write("Cadastro de patrimônio líquido do tipo 'obrigações com sócios' realizado com sucesso.")
            else:
                st.error("Erro: Patrimônio Líquido deve ser 'Obrigação com Sócio' (4).")
