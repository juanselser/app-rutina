# -*- coding: utf-8 -*-
# rutina-calistenia.py

import streamlit as st

# Diccionario con las rutinas por día y enlaces a videos
rutinas = {
    "Día 1 – Push": [
        {"ejercicio": "12-15 Push-ups explosivos", "video": "https://www.youtube.com/watch?v=Eh00_rniF8E"},
        {"ejercicio": "10 Hindu push-ups", "video": "https://www.youtube.com/watch?v=9n1g6c_QF1U"},
        {"ejercicio": "15 Pike push-ups", "video": "https://www.youtube.com/watch?v=1fbU_MkV7NE"},
        {"ejercicio": "20 seg plancha + toques de hombro", "video": "https://www.youtube.com/watch?v=DH6SntGqXqc"},
        {"ejercicio": "10 Push-ups con bajada lenta (5 seg)", "video": "https://www.youtube.com/watch?v=ZBSSR0UZz5Y"}
    ],
    "Día 2 – Piernas & Core": [
        {"ejercicio": "20 Sentadillas", "video": "https://www.youtube.com/watch?v=aclHkVaku9U"},
        {"ejercicio": "10 Sentadillas con salto", "video": "https://www.youtube.com/watch?v=CVaEhXotL7M"},
        {"ejercicio": "10 Estocadas por pierna", "video": "https://www.youtube.com/watch?v=QOVaHwm-Q6U"},
        {"ejercicio": "20 seg Hollow hold", "video": "https://www.youtube.com/watch?v=44ScXWFaViw"},
        {"ejercicio": "15 Crunch con elevación de piernas", "video": "https://www.youtube.com/watch?v=JB2oyawG9KI"}
    ],
    "Día 3 – Pull": [
        {"ejercicio": "10-12 Dominadas (o negatives si no llegas)", "video": "https://www.youtube.com/watch?v=eGo4IYlbE5g"},
        {"ejercicio": "15 Australian pull-ups", "video": "https://www.youtube.com/watch?v=b7hqO3qyr2I"},
        {"ejercicio": "10 Superman rows (con silla o barra baja)", "video": "https://www.youtube.com/watch?v=6FdYx_9OotY"},
        {"ejercicio": "15 Back extensions", "video": "https://www.youtube.com/watch?v=ph3pddqKvZ0"},
        {"ejercicio": "30 seg Dead hang", "video": "https://www.youtube.com/watch?v=6t8QfX_6Hx4"}
    ],
    "Día 4 – Cardio + Core (Alta intensidad)": [
        {"ejercicio": "30” Burpees", "video": "https://www.youtube.com/watch?v=auBLPXO8Fww"},
        {"ejercicio": "30” High knees", "video": "https://www.youtube.com/watch?v=oDdkytliOqE"},
        {"ejercicio": "20” Plank to push-up", "video": "https://www.youtube.com/watch?v=DYGORfD6P1A"},
        {"ejercicio": "15 Leg raises", "video": "https://www.youtube.com/watch?v=JB2oyawG9KI"},
        {"ejercicio": "10 V-ups", "video": "https://www.youtube.com/watch?v=riAutegDqdI"},
        {"ejercicio": "(Circuito 3-4 rondas - descansar 30” entre rondas)", "video": ""}
    ],
    "Día 5 – Full Body control y fuerza isométrica": [
        {"ejercicio": "20” Wall sit", "video": "https://www.youtube.com/watch?v=-cdph8hv0Y0"},
        {"ejercicio": "15 Push up hold (bajar y sostener 2 seg abajo)", "video": "https://www.youtube.com/watch?v=1fbU_MkV7NE"},
        {"ejercicio": "30” Hollow hold", "video": "https://www.youtube.com/watch?v=44ScXWFaViw"},
        {"ejercicio": "20” Plank lateral por lado", "video": "https://www.youtube.com/watch?v=K2VljzCC16g"},
        {"ejercicio": "10 Bulgarian split squats (usar una silla o escalón)", "video": "https://www.youtube.com/watch?v=2C-uNgKwzNI"},
        {"ejercicio": "(Circuito 3 rondas)", "video": ""}
    ],
    "Día 6 – Flow / Movilidad + Core dinámico": [
        {"ejercicio": "10 min rutina de animal flow (movimientos de oso, cangrejo, rana)", "video": "https://www.youtube.com/watch?v=l6ODN5MmRf4"},
        {"ejercicio": "10 min core dinámico (ab scissors, hollow rock, plancha dinámica)", "video": "https://www.youtube.com/watch?v=4dFspDfB7f0"},
        {"ejercicio": "5-10 min de estiramiento activo", "video": "https://www.youtube.com/watch?v=wYH8tGq6Qn0"}
    ],
    "Día 7 – Libre o Active Recovery": [
        {"ejercicio": "Caminata suave", "video": ""},
        {"ejercicio": "Estiramiento profundo", "video": "https://www.youtube.com/watch?v=g_tea8ZNk5A"},
        {"ejercicio": "Respiración y movilidad", "video": "https://www.youtube.com/watch?v=sTANio_2E0Q"},
        {"ejercicio": "Opcional: yoga 20 minutos", "video": "https://www.youtube.com/watch?v=v7AYKMP6rOE"}
    ],
    "Desaceleración (todos los días – 5 minutos)": [
        {"ejercicio": "Estiramiento de espalda, isquios, pecho y hombros", "video": "https://www.youtube.com/watch?v=g_tea8ZNk5A"},
        {"ejercicio": "Respiración diafragmática 1-2 minutos", "video": "https://www.youtube.com/watch?v=0Ua9bOsZTYg"}
    ]
}

# Título
st.title("Rutina Diaria de Calistenia")

# Selección de día
dia = st.selectbox("Elegí el día", list(rutinas.keys()))

# Mostrar ejercicios
st.subheader(f"Rutina para {dia}")
for item in rutinas[dia]:
    if item["video"]:  # Solo mostrar enlace si hay video
        st.write(f"• [{item['ejercicio']}]({item['video']})")
    else:
        st.write(f"• {item['ejercicio']}")

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

# Nota sobre los videos
st.markdown("---")
st.caption("ℹ️ Haz clic en los nombres de los ejercicios para ver videos demostrativos")