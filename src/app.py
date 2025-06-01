
import streamlit as st
import joblib

# Cargar el modelo
modelo = joblib.load('/workspaces/Aplicaci-n-web-ML-con-el-tutorial-Streamlit---Ganyu/models/modelo_suma.pkl')

# Título de la app
st.title("🧮 Calculadora de Suma con ML")

st.write("Este modelo predice la suma de dos números usando regresión lineal.")

# Entradas del usuario
x1 = st.number_input("🔢 Ingresa el primer número:", value=0)
x2 = st.number_input("🔢 Ingresa el segundo número:", value=0)

# Botón para predecir
if st.button("Calcular suma"):
    resultado = modelo.predict([[x1, x2]])
    st.success(f"✅ Resultado (predicción ML): {resultado[0]:.2f}")
