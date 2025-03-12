import streamlit as st
import math

st.title("Lista I: Comandos de Atribuição, Entrada/Saída, Expressões")
st.write("Disciplina: Programação - Prof. MSc. Denise do Rocio Maciel")
st.write("SweetTech - A revolução dos doces com tecnologia!")

# =============================================================================
# Exercício 1: Impressão de mensagem
# =============================================================================
st.header("Exercício 1")
st.write("Minha vida vai melhorar agora que estou aprendendo a programar… pelo menos o computador vai entender meus problemas!")

# =============================================================================
# Exercício 2: Recebendo e imprimindo uma frase
# =============================================================================
st.header("Exercício 2")
frase = st.text_input("Digite a frase abaixo:", 
    "Programar um sistema de confeitaria é igual fazer um bolo: se errar a sintaxe, o código embatuma!")
if st.button("Imprimir frase (Ex. 2)"):
    st.write(frase)

# =============================================================================
# Exercício 3: Bolo de Leite Condensado com 3 Ingredientes
# =============================================================================
st.header("Exercício 3")
st.write("Parabéns, “Doce programador”, agora você está pronto para começar a receita!")

# 3.a – Quantidade de xícaras de farinha
with st.container():
    st.subheader("3.a – Quantidade de xícaras de farinha")
    xicaras = st.number_input("Digite a quantidade de xícaras de farinha necessárias:", 
                              min_value=0.0, value=0.0, step=0.1)
    if st.button("Exibir quantidade (3.a)"):
        st.write(f"Você informou {xicaras} xícaras de farinha.")

# 3.b – Calcular a quantidade total de farinha em gramas
with st.container():
    st.subheader("3.b – Quantidade total de farinha (em gramas)")
    xicaras_b = st.number_input("Digite a quantidade de xícaras de farinha:", 
                                min_value=0.0, value=0.0, step=0.1, key="xicaras_b")
    gramas_por_xicara = st.number_input("Digite a quantidade de gramas por xícara:", 
                                        min_value=0.0, value=0.0, step=1.0)
    if st.button("Calcular farinha total (3.b)"):
        total_farinha = xicaras_b * gramas_por_xicara
        st.write(f"A quantidade total de farinha a ser utilizada é: {total_farinha} gramas.")

# 3.c – Receber dados dos ingredientes
with st.container():
    st.subheader("3.c – Dados dos ingredientes")
    st.write("**Leite Condensado:**")
    qtd_leite = st.number_input("Quantidade de latas/caixas de leite condensado:", 
                                min_value=0, value=0, step=1, key="qtd_leite")
    gramas_leite = st.number_input("Quantidade de gramas por lata/caixa:", 
                                   min_value=0.0, value=0.0, step=1.0, key="gramas_leite")
    
    st.write("**Farinha de Trigo:**")
    qtd_farinha = st.number_input("Quantidade de xícaras de farinha:", 
                                  min_value=0.0, value=0.0, step=0.1, key="qtd_farinha")
    gramas_farinha = st.number_input("Quantidade de gramas por xícara:", 
                                     min_value=0.0, value=0.0, step=1.0, key="gramas_farinha")
    
    st.write("**Ovos:**")
    qtd_ovos = st.number_input("Quantidade de ovos:", 
                               min_value=0, value=0, step=1, key="qtd_ovos")
    
    if st.button("Exibir dados dos ingredientes (3.c)"):
        st.write("**Dados informados:**")
        st.write(f"Leite condensado: {qtd_leite} lata(s)/caixa(s) com {gramas_leite} gramas cada")
        st.write(f"Farinha: {qtd_farinha} xícara(s) com {gramas_farinha} gramas cada")
        st.write(f"Ovos: {qtd_ovos}")

# 3.d – Reorganização da tela utilizando containers (já utilizada nos itens acima)

# =============================================================================
# Exercício 4: Verificando a forma para a receita
# =============================================================================
st.header("Exercício 4: Verificação da forma para a receita")

# 4.a – Cálculo dos ml de cada ingrediente (valores fixos fornecidos)
st.subheader("4.a – Cálculo dos ml dos ingredientes")
# Conversões fornecidas:
# Leite condensado: 395g ≈ 306 mL
# Ovos: 4 ovos ≈ 200 mL
# Farinha: 120g ≈ 132 mL
ml_leite = 306
ml_ovos = 200
ml_farinha = 132
total_ml = ml_leite + ml_ovos + ml_farinha
st.write(f"Leite condensado: {ml_leite} mL")
st.write(f"Ovos: {ml_ovos} mL")
st.write(f"Farinha de trigo: {ml_farinha} mL")
st.write(f"Total de ml da receita: {total_ml} mL")

# 4.b – Cálculo do volume da forma retangular
st.subheader("4.b – Volume da forma retangular")
comprimento = st.number_input("Digite o comprimento da forma (cm):", 
                                min_value=0.0, value=0.0, step=0.1, key="comprimento")
largura = st.number_input("Digite a largura da forma (cm):", 
                          min_value=0.0, value=0.0, step=0.1, key="largura")
altura = st.number_input("Digite a altura da forma (cm):", 
                         min_value=0.0, value=0.0, step=0.1, key="altura")
if st.button("Calcular volume da forma (4.b)"):
    volume_forma = comprimento * largura * altura
    st.write(f"Volume da forma: {volume_forma} mL")
    if volume_forma == total_ml:
        st.write("O conteúdo cabe na forma (volume igual aos ml da receita).")
    elif volume_forma > total_ml:
        st.write("A forma é grande o suficiente para a receita.")
    else:
        st.write("A forma não é grande o suficiente para a receita.")

# 4.c – Cálculo da área do papel para untar a forma retangular
st.subheader("4.c – Área do papel para untar a forma retangular")
base_ret = st.number_input("Digite a base do papel (cm):", 
                             min_value=0.0, value=0.0, step=0.1, key="base_ret")
altura_ret = st.number_input("Digite a altura do papel (cm):", 
                             min_value=0.0, value=0.0, step=0.1, key="altura_ret")
if st.button("Calcular área do papel (4.c)"):
    area_ret = base_ret * altura_ret
    st.write(f"Área do papel: {area_ret} cm²")

# 4.d – Cálculo do volume da forma redonda (cilindro)
st.subheader("4.d – Volume da forma redonda (cilindro)")
altura_cil = st.number_input("Digite a altura do cilindro (cm):", 
                             min_value=0.0, value=0.0, step=0.1, key="altura_cil")
raio_cil = st.number_input("Digite o raio do cilindro (cm):", 
                           min_value=0.0, value=0.0, step=0.1, key="raio_cil")
if st.button("Calcular volume do cilindro (4.d)"):
    volume_cil = math.pi * (raio_cil ** 2) * altura_cil
    st.write(f"Volume do cilindro: {volume_cil:.2f} mL")

# 4.e – Cálculo da área do papel para untar a forma redonda (círculo)
st.subheader("4.e – Área do papel para untar a forma redonda")
raio_papel = st.number_input("Digite o raio do papel (cm):", 
                             min_value=0.0, value=0.0, step=0.1, key="raio_papel")
if st.button("Calcular área do papel (4.e)"):
    area_circulo = math.pi * (raio_papel ** 2)
    st.write(f"Área do papel (círculo): {area_circulo:.2f} cm²")

# =============================================================================
# Exercício 5: Ajuste na Receita - Versão menos calórica
# =============================================================================
st.header("Exercício 5: Versão menos calórica")
st.write("Reduzindo 20% da quantidade de leite condensado.")
ml_leite_calorico = ml_leite - (0.20 * ml_leite)
total_ml_menos_calorico = ml_leite_calorico + ml_ovos + ml_farinha
st.write(f"Leite condensado (menos 20%): {ml_leite_calorico} mL")
st.write(f"Total de ml da receita (versão menos calórica): {total_ml_menos_calorico} mL")
st.write("Esta é a versão menos calórica da receita.")

# =============================================================================
# Exercício 6: Custo Total de Aquisição (CTA)
# =============================================================================
st.header("Exercício 6: Cálculo do CTA")
st.write("Informe os valores dos custos, despesas e impostos:")

st.subheader("Custos Fixos")
aluguel = st.number_input("Aluguel:", min_value=0.0, value=0.0, step=0.1, key="aluguel6")
energia = st.number_input("Energia elétrica:", min_value=0.0, value=0.0, step=0.1, key="energia6")
internet = st.number_input("Internet:", min_value=0.0, value=0.0, step=0.1, key="internet6")
agua = st.number_input("Água:", min_value=0.0, value=0.0, step=0.1, key="agua6")

st.subheader("Custos Variáveis")
estoque = st.number_input("Estoque:", min_value=0.0, value=0.0, step=0.1, key="estoque6")
leite_custo = st.number_input("Lata de leite condensado (valor):", min_value=0.0, value=0.0, step=0.1, key="leite_custo6")
ovos_custo = st.number_input("Ovos (valor):", min_value=0.0, value=0.0, step=0.1, key="ovos_custo6")
farinha_custo = st.number_input("Xícara de farinha de trigo (valor):", min_value=0.0, value=0.0, step=0.1, key="farinha_custo6")
gas = st.number_input("Gás:", min_value=0.0, value=0.0, step=0.1, key="gas6")
embalagem_variavel = st.number_input("Embalagem (custos variáveis):", min_value=0.0, value=0.0, step=0.1, key="embalagem_variavel6")

st.subheader("Despesas")
cozinha = st.number_input("Setor da cozinha:", min_value=0.0, value=0.0, step=0.1, key="cozinha6")
vendas = st.number_input("Setor das vendas:", min_value=0.0, value=0.0, step=0.1, key="vendas6")
administrativo = st.number_input("Setor administrativo:", min_value=0.0, value=0.0, step=0.1, key="administrativo6")
anuidade = st.number_input("Anuidade de domínio:", min_value=0.0, value=0.0, step=0.1, key="anuidade6")
mensalidade = st.number_input("Mensalidade do MEI:", min_value=0.0, value=0.0, step=0.1, key="mensalidade6")
transporte = st.number_input("Valor do transporte (Frete):", min_value=0.0, value=0.0, step=0.1, key="transporte6")
embalagem_despesas = st.number_input("Valor da embalagem (despesas):", min_value=0.0, value=0.0, step=0.1, key="embalagem_despesas6")

st.subheader("Impostos")
icms = st.number_input("ICMS:", min_value=0.0, value=0.0, step=0.1, key="icms6")

if st.button("Calcular CTA (Ex. 6)"):
    custos_fixos = aluguel + energia + internet + agua
    custos_variaveis = estoque + leite_custo + ovos_custo + farinha_custo + gas + embalagem_variavel
    despesas = cozinha + vendas + administrativo + anuidade + mensalidade + transporte + embalagem_despesas
    CTA = custos_fixos + custos_variaveis + despesas + icms
    st.write(f"O Custo Total de Aquisição (CTA) é: {CTA}")

# =============================================================================
# Exercício 7: Precificação - Markup e Margem de Giro
# =============================================================================
st.header("Exercício 7: Precificação")
st.write("Informe os valores percentuais (em %) para o cálculo do Markup:")
DV = st.number_input("Despesas variáveis (DV):", min_value=0.0, value=0.0, step=0.1, key="DV7")
DF = st.number_input("Despesas fixas (DF):", min_value=0.0, value=0.0, step=0.1, key="DF7")
ML = st.number_input("Margem de lucro (ML):", min_value=0.0, value=0.0, step=0.1, key="ML7")
if st.button("Calcular Markup (Ex. 7)"):
    try:
        markup = 100 / (100 - (DV + DF + ML))
        st.write(f"O Markup é: {markup:.2f}")
    except ZeroDivisionError:
        st.write("Erro: A soma dos percentuais não pode ser 100% ou superior.")

st.write("Agora, informe os valores para calcular a Margem de Giro:")
preco_venda = st.number_input("Preço de venda:", min_value=0.0, value=0.0, step=0.1, key="preco_venda7")
custo_produto = st.number_input("Custo do produto:", min_value=0.0, value=0.0, step=0.1, key="custo_produto7")
if st.button("Calcular Margem de Giro (Ex. 7)"):
    margem_giro = preco_venda - custo_produto
    st.write(f"A Margem de Giro é: {margem_giro}")

# =============================================================================
# Exercício 8: Valor médio das encomendas
# =============================================================================
st.header("Exercício 8: Valor médio das encomendas")
# Dados das encomendas
encomendas = [350, 160, 200, 150, 230, 280, 500, 8000, 130, 200]
st.write("Valores das encomendas:", encomendas)
if st.button("Calcular valor médio (Ex. 8)"):
    media = sum(encomendas) / len(encomendas)
    st.write(f"O valor médio de cada encomenda é: {media:.2f}")
    # Cálculo opcional: média sem considerar o outlier (8000)
    encomendas_sem_outlier = [valor for valor in encomendas if valor != 8000]
    media_sem_outlier = sum(encomendas_sem_outlier) / len(encomendas_sem_outlier)
    st.write(f"Valor médio sem o outlier (8000): {media_sem_outlier:.2f}")
