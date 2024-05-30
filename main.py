import streamlit as st
st.set_page_config(layout="wide")



st.write("""
         # Hola prueba cemex
         """)
st.image('cemex logo.png')

a = st.text_input("Inserte su busqueda aqui")

b = a + 'aaaar'

st.write(b)