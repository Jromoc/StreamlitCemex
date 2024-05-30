import streamlit as st
st.set_page_config(layout="wide")

st.image('cemex logo.png', width=800)

st.write("""
         # Hola prueba cemex
         """)

a = st.text_input("Inserte su busqueda aqui")

b = a + 'aaaar'

st.write(b)

st.image('cemex banner.jpg', width=1200)