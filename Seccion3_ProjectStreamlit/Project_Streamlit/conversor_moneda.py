import streamlit as st

#! 1. Ingresar la cantidad de dinero (dolares) a convertir
#! 2. Realizar la formula para convertir la moneda a Pesos(clp)
#! 3. Imprimir el resultado de la conversion se debe realizar con un boton


# titulo de la pagina
st.title("Conversor de dolares a pesos chilenos")

# caja de texto para ingresar la cantidad de dolares
dolares = st.number_input("Ingrese la cantidad de dolares a convertir", min_value=0.0, step=0.01, format="%.2f")

pesos =  dolares * 940 # Tasa de cambio aproximada (1 USD = 940 CLP)

# Convertir a string para mostrar en la interfaz
pesos = str(pesos)

# Boton para realizar la conversion
if st.button("Convertir"):
    
    # Mostrar el resultado de la conversion en streamlit
    st.write(f"Con la cantidad de USD {dolares} obtendrás: {pesos} mil pesos chilenos.")
    
    # Mostrar el resultado de la conversion en la consola
    print(f"Con la cantidad de USD {dolares} obtendrás: {pesos} mil pesos chilenos.")
    
# Boton para limpiar la caja de texto (opcional)
if st.button("Limpiar"):
    st.write("La caja de texto se ha limpiado.")
    dolares = 0.0
    pesos = "0.00"

    






#st.button("Convertir", on_click=print(f"Con la esa cantidad de USD {dolares} obtendras : " + pesos + " mil pesos chilenos."))
