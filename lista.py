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
        gramas_por_xicara = st.number_input("Digite a quantidade de gramas por xícara:", min_value=0.0, value=120.0, step=1.0)
        if st.button("Calcular farinha total (3.b)"):
            total_farinha = xicaras_b * gramas_por_xicara
            st.write(f"A quantidade total de farinha a ser utilizada é: {total_farinha} gramas.")
    
    with st.container():
        st.subheader("3.c – Receber todos os dados da receita")
        latas_leite = st.number_input("Quantidade de latas de leite condensado:", min_value=0, value=1)
        gramas_leite = st.number_input("Gramas por lata de leite:", min_value=0.0, value=395.0)
        xicaras_farinha = st.number_input("Xícaras de farinha:", min_value=0.0, value=1.0)
        gramas_por_xicara = st.number_input("Gramas por xícara de farinha:", min_value=0.0, value=120.0, key="gramas_xicara_c")
        ovos = st.number_input("Quantidade de ovos:", min_value=0, value=4)
        if st.button("Exibir dados (3.c)"):
            st.write(f"Leite condensado: {latas_leite} latas de {gramas_leite}g")
            st.write(f"Farinha: {xicaras_farinha} xícaras de {gramas_por_xicara}g")
            st.write(f"Ovos: {ovos} unidades")

def exercicio_4():
    st.header("Exercício 4: Verificação da forma para a receita")
    
    with st.container():
        st.subheader("4.a – Cálculo de mL por ingrediente")
        leite_ml = 395 * 306  # 395g * 306mL
        ovos_ml = 4 * 200     # 4 ovos * 200mL
        farinha_ml = 120 * 132 # 120g * 132mL
        total_ml = leite_ml + ovos_ml + farinha_ml
        st.write(f"Total de mL da receita: {total_ml} mL")
    
    with st.container():
        st.subheader("4.b – Volume da forma retangular")
        comprimento = st.number_input("Comprimento (cm):", min_value=0.0, value=20.0)
        largura = st.number_input("Largura (cm):", min_value=0.0, value=10.0)
        altura = st.number_input("Altura (cm):", min_value=0.0, value=5.0)
        if st.button("Calcular volume (4.b)"):
            volume = comprimento * largura * altura
            st.write(f"Volume da forma: {volume} mL (Cabe na forma? {'Sim' if volume >= total_ml else 'Não'})")
    
    with st.container():
        st.subheader("4.c – Área do papel (forma retangular)")
        base = st.number_input("Base (cm):", min_value=0.0, value=20.0)
        altura_papel = st.number_input("Altura (cm):", min_value=0.0, value=10.0)
        if st.button("Calcular área (4.c)"):
            area = base * altura_papel
            st.write(f"Área do papel: {area} cm²")
    
    with st.container():
        st.subheader("4.d – Volume da forma cilíndrica")
        raio = st.number_input("Raio (cm):", min_value=0.0, value=5.0)
        altura_cilindro = st.number_input("Altura (cm):", min_value=0.0, value=10.0)
        if st.button("Calcular volume (4.d)"):
            volume_cilindro = math.pi * (raio ** 2) * altura_cilindro
            st.write(f"Volume do cilindro: {volume_cilindro:.2f} mL")
    
    with st.container():
        st.subheader("4.e – Área do papel (forma redonda)")
        raio_papel = st.number_input("Raio (cm):", min_value=0.0, value=5.0, key="raio_papel")
        altura_papel_redondo = st.number_input("Altura (cm):", min_value=0.0, value=10.0, key="altura_papel_redondo")
        if st.button("Calcular área (4.e)"):
            area_base = math.pi * (raio_papel ** 2)
            area_lateral = 2 * math.pi * raio_papel * altura_papel_redondo
            st.write(f"Área da base: {area_base:.2f} cm² | Área lateral: {area_lateral:.2f} cm²")

def exercicio_5():
    st.header("Exercício 5: Versão menos calórica")
    latas_leite = st.number_input("Quantidade de latas de leite:", min_value=0, value=1)
    gramas_leite = st.number_input("Gramas por lata:", min_value=0.0, value=395.0)
    if st.button("Calcular redução (5)"):
        leite_reduzido = gramas_leite * 0.80  # Redução de 20%
        st.write(f"Leite condensado ajustado: {leite_reduzido}g (20% menos)")
        st.success("Aviso: Esta é a versão menos calórica!")

def exercicio_6():
    st.header("Exercício 6: Cálculo do CTA")
    with st.container():
        st.subheader("Custos Fixos")
        aluguel = st.number_input("Aluguel:", value=1500.0)
        energia = st.number_input("Energia:", value=300.0)
        internet = st.number_input("Internet:", value=100.0)
        agua = st.number_input("Água:", value=80.0)
    
    with st.container():
        st.subheader("Custos Variáveis")
        leite = st.number_input("Leite condensado:", value=200.0)
        ovos = st.number_input("Ovos:", value=50.0)
        farinha = st.number_input("Farinha:", value=30.0)
        gas = st.number_input("Gás:", value=150.0)
        embalagem = st.number_input("Embalagem:", value=20.0)
    
    with st.container():
        st.subheader("Despesas e Impostos")
        administrativas = st.number_input("Despesas administrativas:", value=500.0)
        impostos = st.number_input("Impostos (ICMS):", value=300.0)
        frete = st.number_input("Frete:", value=100.0)
    
    if st.button("Calcular CTA (Ex. 6)"):
        custo_fixo = aluguel + energia + internet + agua
        custo_variavel = leite + ovos + farinha + gas + embalagem
        despesas = administrativas + impostos + frete
        CTA = custo_fixo + custo_variavel + despesas
        st.write(f"CTA Total: R$ {CTA:.2f}")

def exercicio_7():
    st.header("Exercício 7: Precificação")
    DV = st.number_input("Despesas variáveis (%):", min_value=0.0, max_value=100.0, value=15.0)
    DF = st.number_input("Despesas fixas (%):", min_value=0.0, max_value=100.0, value=10.0)
    ML = st.number_input("Margem de lucro (%):", min_value=0.0, max_value=100.0, value=20.0)
    custo_produto = st.number_input("Custo do produto (R$):", value=50.0)
    
    if st.button("Calcular (Ex. 7)"):
        try:
            markup = 100 / (100 - (DV + DF + ML))
            preco_venda = custo_produto * markup
            margem_giro = preco_venda - custo_produto
            st.write(f"Markup: {markup:.2f}")
            st.write(f"Preço de venda: R$ {preco_venda:.2f}")
            st.write(f"Margem de giro: R$ {margem_giro:.2f}")
        except ZeroDivisionError:
            st.error("Erro: A soma dos percentuais não pode ser 100% ou mais!")

def exercicio_8():
    st.header("Exercício 8: Valor médio das encomendas")
    encomendas = [350, 160, 200, 150, 230, 280, 500, 8000, 130, 200]
    st.write("Valores originais:", encomendas)
    
    # Remover outlier (8.000)
    encomendas_filtradas = [v for v in encomendas if v != 8000]
    
    if st.button("Calcular média sem outlier (Ex. 8)"):
        media = sum(encomendas_filtradas) / len(encomendas_filtradas)
        st.write(f"Valor médio ajustado: R$ {media:.2f}")

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
selecao = st.selectbox("Escolha um exercício:", list(exercicios.keys()))
exercicios[selecao]()
