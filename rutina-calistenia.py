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
    "Día 3 – Pull": [
        "10-12 Dominadas (o negatives si no llegas)",
        "15 Australian pull-ups",
        "10 Superman rows (con silla o barra baja)",
        "15 Back extensions",
        "30 seg Dead hang"
    ],
    "Día 4 – Cardio + Core (Alta intensidad)": [
        "30” Burpees",
        "30” High knees",
        "20” Plank to push-up",
        "15 Leg raises",
        "10 V-ups",
        "(Circuito 3-4 rondas - descansar 30” entre rondas)"
    ],
    "Día 5 – Full Body control y fuerza isométrica": [
        "20” Wall sit",
        "15 Push up hold (bajar y sostener 2 seg abajo)",
        "30” Hollow hold",
        "20” Plank lateral por lado",
        "10 Bulgarian split squats (usar una silla o escalón)",
        "(Circuito 3 rondas)"
    ],
    "Día 6 – Flow / Movilidad + Core dinámico": [
        "10 min rutina de animal flow (movimientos de oso, cangrejo, rana)",
        "10 min core dinámico (ab scissors, hollow rock, plancha dinámica)",
        "5-10 min de estiramiento activo"
    ],
    "Día 7 – Libre o Active Recovery": [
        "Caminata suave",
        "Estiramiento profundo",
        "Respiración y movilidad",
        "Opcional: yoga 20 minutos"
    ],
    "Desaceleración (todos los días – 5 minutos)": [
        "Estiramiento de espalda, isquios, pecho y hombros",
        "Respiración diafragmática 1-2 minutos"
    ]
}

# Título
st.title("Rutina Diaria de Calistenia")

# Selección de día
dia = st.selectbox("Elegí el día", list(rutinas.keys()))

# Mostrar ejercicios
st.subheader(f"Rutina para {dia}")
for ejercicio in rutinas[dia]:
    st.write(f"• {ejercicio}")

# Mostrar información adicional según el día
if dia in ["Día 1 – Push", "Día 2 – Piernas & Core", "Día 3 – Pull"]:
    st.markdown("---")
    st.info("Hacé 4 rondas – Descanso: 30 segundos entre rondas")
elif dia == "Día 4 – Cardio + Core (Alta intensidad)":
    st.markdown("---")
    st.info("Circuito de 3-4 rondas - Descanso: 30 segundos entre rondas")
elif dia == "Día 5 – Full Body control y fuerza isométrica":
    st.markdown("---")
    st.info("Circuito de 3 rondas")
elif dia == "Desaceleración (todos los días – 5 minutos)":
    st.markdown("---")
    st.info("Realizar al final de cada entrenamiento")