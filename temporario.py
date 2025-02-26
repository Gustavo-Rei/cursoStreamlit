import streamlit as st
st.header("Cabeçalho")
st.toggle("Toggle")
st.text_area("Enter text")
st.text_input("")
st.selectbox("Qual a sua cor favorita?", ("Azul","Vermelho","Verde"))
options = st.multiselect(
  'Quais são suas cores favoritas?',
  ['Azul', 'Vermelho', 'Verde', 'Branco'],
  ['Rosa', 'Amarelo'])
st.checkbox('Sorvete')
st.checkbox('Café')
st.checkbox('Refrigerante')
st.button("Botão Salvar")

