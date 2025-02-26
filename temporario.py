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

color = st.color_picker("Pick A Color", "#00f900")
st.write("Sua cor é", color)



st.feedback("stars")

st.checkbox('Sorvete')
st.checkbox('Café')
st.checkbox('Refrigerante')


st.button("Botão Salvar")

df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 4, "is_widget": True},
        {"command": "st.ballons", "rating": 5, "is_widget": True},
        {"command": "st.time_imput", "rating": 3, "is_widget": True},
    ]
)

edited_df = st.data_editor(df)
