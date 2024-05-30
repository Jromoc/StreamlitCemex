import streamlit as st

st.write("""
         # Hola prueba cemex
         """)


a = st.text_input("Inserte su busqueda aqui")

def suma(a):
    b = a+3    
    
suma()

st.write(b)