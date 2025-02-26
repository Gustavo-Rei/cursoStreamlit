import streamlit as st
st.header("Cabeçalho")
st.toggle("Toggle")
st.text_area("Enter text")
st.text_input("")
st.selectbox("Qual a sua cor favorita?", ("Azul","Vermelho","Verde"))
options = st.multiselect(
    "Quais cores são suas favoritas?",
    ["Verde", "Amarelo", "Vermelho", "Azul"],
    ["Amarelo", "Vermelho"],
)

color = st.color.picker("Pick A Color","#00f900")
st.feedback("stars")

st.checkbox('Sorvete')
st.checkbox('Café')
st.checkbox('Refrigerante')



st.button("Botão Salvar")

