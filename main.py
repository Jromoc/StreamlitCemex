import streamlit as st

st.write("""
         # Hola prueba cemex
         """)


a = st.text_input("Inserte su busqueda aqui")

b = a + 'r'

st.write(b)