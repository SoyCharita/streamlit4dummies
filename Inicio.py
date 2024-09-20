import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
     page_title="Mi primera prueba de Streamlite",
     page_icon="❤️",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# Info sobre mi app!"
     }
 )


st.title("Mi primera App en Streamlit")
st.write("¡¡¡Hola Mundo!!!")

col1, col2 = st.columns(2) # Anchos iguales
#col1, col2 = st.columns([2, 1]) # Anchos proporcionales
with col1:
    st.write("A cat")
    st.button("A button")
col2.button("Another button")
col2.write("A dog")

with st.expander("Título del expander"):
    # Este contenido se muestra solo cuando se expande el elemento
    st.write("Hola mundo")

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    # Este contenido se muestra en la pestaña 1
    st.write("Hola mundo")

with tab2:
    # Este contenido se muestra en la pestaña 2
    st.write("¿Que tal, festival?")

# En lugar de llamar a st directamente, llamamos a st.sidebar
st.sidebar.write('Esto está en el sidebar')
if st.sidebar.button('Mi botón opcional'):
    st.balloons()

import time
if st.button("Click me!"):
    st.write("Uno")
    e2 = st.empty()
    e3 = st.empty()
    e3.write("Tres")
    time.sleep(2)
    e2.write("Dos")
    time.sleep(2)
    e3.empty()
    e2.empty()

st.subheader("Datos")
N = 10
df = pd.DataFrame(100*np.random.randn(5, N), columns=('col%d' % i for i in range(N)))
st.dataframe(df)  # Same as st.write(df)

st.subheader("Gráficos")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])
st.line_chart(chart_data)

st.subheader("Foto de gato porque internet")
st.image("https://cataas.com/cat/cute")