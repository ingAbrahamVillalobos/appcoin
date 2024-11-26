import streamlit as st
import os

# Configura el puerto asignado dinámicamente por Render
port = int(os.environ.get("PORT", 8501))

# Configura la página principal (opcional, para evitar advertencias de Streamlit)
st.set_page_config(page_title="Lanzar una moneda", layout="wide")

st.header('Lanzar una moneda')

st.write('Esta aplicación aún no es funcional. En construcción.')

