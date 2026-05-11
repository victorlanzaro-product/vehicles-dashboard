import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('vehicles.csv')

st.header('Análise de Anúncios de Venda de Carros')

if st.checkbox('Mostrar histograma do odômetro'):
    fig = px.histogram(df, x='odometer', title='Distribuição do Odômetro')
    st.plotly_chart(fig)

if st.checkbox('Mostrar dispersão odômetro vs preço'):
    fig = px.scatter(df, x='odometer', y='price', title='Odômetro vs Preço')
    st.plotly_chart(fig)
