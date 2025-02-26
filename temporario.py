import streamlit as st  # Importa a biblioteca Streamlit para criar a interface web
import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados

# Cabeçalho principal da aplicação
st.header("Cabeçalho")

# Widget de alternância (toggle switch)
st.toggle("Toggle")

# Área de texto para entrada de dados do usuário
st.text_area("Enter text")

# Campo de entrada de texto simples (seria ideal adicionar um label significativo)
st.text_input("Digite algo")

# Caixa de seleção para escolha de uma única opção entre as disponíveis
st.selectbox("Qual a sua cor favorita?", ("Azul", "Vermelho", "Verde"))

# Seleção múltipla, permitindo ao usuário escolher mais de uma cor
options = st.multiselect(
    "Quais cores são suas favoritas?",
    ["Verde", "Amarelo", "Vermelho", "Azul"],
    ["Amarelo", "Vermelho"],  # Valores padrão já selecionados
)

# Seletor de cores, permitindo ao usuário escolher uma cor
color = st.color_picker("Pick A Color", "#00f900")
st.write("Sua cor é", color)  # Exibe a cor escolhida

# Widget de feedback com estrelas (Função experimental do Streamlit)
st.feedback("stars")

# Três caixas de seleção para preferências de bebidas
st.checkbox('Sorvete')
st.checkbox('Café')
st.checkbox('Refrigerante')

# Botão de ação para salvar (não há funcionalidade associada, apenas exibição)
st.button("Botão Salvar")

# Criação de um DataFrame com informações sobre alguns comandos do Streamlit
df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.balloons", "rating": 5, "is_widget": True},  # Correção de 'st.ballons' para 'st.balloons'
        {"command": "st.time_input", "rating": 3, "is_widget": True},  # Correção de 'st.time_imput' para 'st.time_input'
    ]
)

# Editor de tabela interativo, permitindo ao usuário modificar os dados do DataFrame
edited_df = st.data_editor(df)
