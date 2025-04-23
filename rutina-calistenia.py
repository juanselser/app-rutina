# -*- coding: utf-8 -*-
# rutina-calistenia.py

import streamlit as st

# Diccionario con las rutinas por día
rutinas = {
    "Día 1 – Push": [
        "12-15 Push-ups explosivos",
        "10 Hindu push-ups",
        "15 Pike push-ups",
        "20 seg plancha + toques de hombro",
        "10 Push-ups con bajada lenta (5 seg)"
    ],
    "Día 2 – Piernas & Core": [
        "20 Sentadillas",
        "10 Sentadillas con salto",
        "10 Estocadas por pierna",
        "20 seg Hollow hold",
        "15 Crunch con elevación de piernas"
    ],
    # Agregá más días si querés
}

# Título
st.title("Rutina Diaria de Calistenia")

# Selección de día
dia = st.selectbox("Elegí el día", list(rutinas.keys()))

# Mostrar ejercicios
st.subheader(f"Rutina para {dia}")
for ejercicio in rutinas[dia]:
    st.write(f"• {ejercicio}")

st.markdown("---")
st.info("Hacé 4 rondas – Descanso: 30 segundos entre rondas")
