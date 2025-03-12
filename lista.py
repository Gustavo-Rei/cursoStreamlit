import streamlit as st
import math

def exercicio_1():
    st.header("Exercício 1")
    st.write("Minha vida vai melhorar agora que estou aprendendo a programar… pelo menos o computador vai entender meus problemas!")

def exercicio_2():
    st.header("Exercício 2")
    frase = st.text_input("Digite a frase abaixo:", "Programar um sistema de confeitaria é igual fazer um bolo: se errar a sintaxe, o código embatuma!")
    if st.button("Imprimir frase (Ex. 2)"):
        st.write(frase)

def exercicio_3():
    st.header("Exercício 3: Bolo de Leite Condensado com 3 Ingredientes")
    st.write("Parabéns, “Doce programador”, agora você está pronto para começar a receita!")
    
    with st.container():
        st.subheader("3.a – Quantidade de xícaras de farinha")
        xicaras = st.number_input("Digite a quantidade de xícaras de farinha necessárias:", min_value=0.0, value=0.0, step=0.1)
        if st.button("Exibir quantidade (3.a)"):
            st.write(f"Você informou {xicaras} xícaras de farinha.")
    
    with st.container():
        st.subheader("3.b – Quantidade total de farinha (em gramas)")
        xicaras_b = st.number_input("Digite a quantidade de xícaras de farinha:", min_value=0.0, value=0.0, step=0.1, key="xicaras_b")
        gramas_por_xicara = st.number_input("Digite a quantidade de gramas por xícara:", min_value=0.0, value=0.0, step=1.0)
        if st.button("Calcular farinha total (3.b)"):
            total_farinha = xicaras_b * gramas_por_xicara
            st.write(f"A quantidade total de farinha a ser utilizada é: {total_farinha} gramas.")

def exercicio_4():
    st.header("Exercício 4: Verificação da forma para a receita")
    comprimento = st.number_input("Digite o comprimento da forma (cm):", min_value=0.0, value=0.0, step=0.1)
    largura = st.number_input("Digite a largura da forma (cm):", min_value=0.0, value=0.0, step=0.1)
    altura = st.number_input("Digite a altura da forma (cm):", min_value=0.0, value=0.0, step=0.1)
    if st.button("Calcular volume da forma (4.b)"):
        volume_forma = comprimento * largura * altura
        st.write(f"Volume da forma: {volume_forma} mL")

def exercicio_5():
    st.header("Exercício 5: Versão menos calórica")
    ml_leite = 306
    ml_ovos = 200
    ml_farinha = 132
    ml_leite_calorico = ml_leite - (0.20 * ml_leite)
    total_ml_menos_calorico = ml_leite_calorico + ml_ovos + ml_farinha
    st.write(f"Leite condensado (menos 20%): {ml_leite_calorico} mL")
    st.write(f"Total de ml da receita (versão menos calórica): {total_ml_menos_calorico} mL")

def exercicio_6():
    st.header("Exercício 6: Cálculo do CTA")
    aluguel = st.number_input("Aluguel:", min_value=0.0, value=0.0, step=0.1)
    energia = st.number_input("Energia elétrica:", min_value=0.0, value=0.0, step=0.1)
    if st.button("Calcular CTA (Ex. 6)"):
        CTA = aluguel + energia
        st.write(f"O Custo Total de Aquisição (CTA) é: {CTA}")

def exercicio_7():
    st.header("Exercício 7: Precificação")
    DV = st.number_input("Despesas variáveis (DV):", min_value=0.0, value=0.0, step=0.1)
    DF = st.number_input("Despesas fixas (DF):", min_value=0.0, value=0.0, step=0.1)
    ML = st.number_input("Margem de lucro (ML):", min_value=0.0, value=0.0, step=0.1)
    if st.button("Calcular Markup (Ex. 7)"):
        try:
            markup = 100 / (100 - (DV + DF + ML))
            st.write(f"O Markup é: {markup:.2f}")
        except ZeroDivisionError:
            st.write("Erro: A soma dos percentuais não pode ser 100% ou superior.")

def exercicio_8():
    st.header("Exercício 8: Valor médio das encomendas")
    encomendas = [350, 160, 200, 150, 230, 280, 500, 8000, 130, 200]
    st.write("Valores das encomendas:", encomendas)
    if st.button("Calcular valor médio (Ex. 8)"):
        media = sum(encomendas) / len(encomendas)
        st.write(f"O valor médio de cada encomenda é: {media:.2f}")

exercicios = {
    "Exercício 1": exercicio_1,
    "Exercício 2": exercicio_2,
    "Exercício 3": exercicio_3,
    "Exercício 4": exercicio_4,
    "Exercício 5": exercicio_5,
    "Exercício 6": exercicio_6,
    "Exercício 7": exercicio_7,
    "Exercício 8": exercicio_8
}

st.title("Lista de Exercícios - Programação")
selecao = st.selectbox("Escolha um exercício para visualizar:", list(exercicios.keys()))

exercicios[selecao]()
