import streamlit as st
st.header("Cabeçalho")
st.toggle("Toggle")
st.text_area("Enter text")
st.text_input("")
st.selectbox("Qual a sua cor favorita?", ("Azul","Vermelho","Verde"))

st.button("Botão Salvar")

st.multiselect("Select numbers", [1, 2, 3], default="1")
