import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Análisis de Anuncios de Coches")

# Encabezado
st.header("Exploración de datos")

# Cargar el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear casillas de verificación
show_histogram = st.checkbox('Mostrar histograma del odómetro')
show_scatter = st.checkbox('Mostrar gráfico de dispersión (odómetro vs precio)')

# Generar histograma si la casilla está marcada
if show_histogram:
    st.write('Histograma de la variable odómetro')
    fig_hist = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig_hist, use_container_width=True)

# Generar gráfico de dispersión si la casilla está marcada
if show_scatter:
    st.write('Gráfico de dispersión entre el odómetro y el precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre el odómetro y el precio")
    st.plotly_chart(fig_scatter, use_container_width=True)