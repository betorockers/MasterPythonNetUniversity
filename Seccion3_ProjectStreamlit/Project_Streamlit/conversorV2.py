import streamlit as st

def convertir_dolares_a_pesos(dolares):
    return dolares * 940  # Tasa de cambio aproximada (1 USD = 940 CLP)

# Solo modo Streamlit
st.title("Conversor de dolares a pesos chilenos")
dolares = st.number_input("Ingrese la cantidad de dolares a convertir", min_value=0.0, step=0.01, format="%.2f")
if st.button("Convertir"):
    pesos = convertir_dolares_a_pesos(dolares)
    resultado = f"Con la cantidad de {dolares:.2f} USD obtendrás: ${pesos:.2f} pesos chilenos."
    st.success(resultado)
    print(resultado)
if st.button("Limpiar"):
    st.write("La caja de texto se ha limpiado.")