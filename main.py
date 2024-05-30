import streamlit as st
st.set_page_config(layout="wide")

st.sidebar.header("Sidebar Title")
st.sidebar.subheader("Subheading")
st.sidebar.text("Sidebar content goes here.")

st.write("""
         # Hola prueba cemex
         """)


a = st.text_input("Inserte su busqueda aqui")

b = a + 'aaaar'

st.write(b)