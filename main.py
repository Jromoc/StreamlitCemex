import streamlit as st
st.set_page_config(layout="wide")
# Custom HTML/CSS for the banner
custom_html = """
<div class="banner">
    <img src="C:\Users\josee\OneDrive\Documents\7mo Concentracion\Bloque 2\Reto\StreamlitCemex\cemex logo.png" alt="Banner Image">
</div>
<style>
    .banner {
        width: 160%;
        height: 200px;
        overflow: hidden;
    }
    .banner img {
        width: 100%;
        object-fit: cover;
    }
</style>
"""

st.write("""
         # Hola prueba cemex
         """)


a = st.text_input("Inserte su busqueda aqui")

b = a + 'aaaar'

st.write(b)