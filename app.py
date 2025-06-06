import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Aplicación donde veremos graficos de un conjunto de datos de vehiculos', divider='gray')
car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

hist_check = st.checkbox('Construir histograma')  # crear una casilla
disp_check = st.checkbox('Construir grafico de dispersion')  # crear un casilla

if hist_check:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_check:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispersion de venta de coches')
    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
