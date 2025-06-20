import streamlit as st
import pandas as pd

# creamos la funcion para calcular el subtotal
def calcular_subtotal(producto, precio, cantidad):
    subtotal = float(precio) * float(cantidad)
    
    # creamos la variable nueva_fila para almacenar los datos del producto
    nueva_fila = {
        "Producto": producto,
        "Precio": precio,
        "Cantidad": cantidad,
        "Subtotal": subtotal
    }
    print('execute')
    # creamos el atributo para agregar los datos a la tabla
    st.session_state.table_data = pd.concat(
        [st.session_state.table_data, 
        pd.DataFrame([nueva_fila])], ignore_index=True
        )


#! habrimos una sesion para almacenar los datos de la tabla

#? si no existe table_data en session_state, la creamos (not in / no existe)
if "table_data" not in st.session_state:    
    # Inicializamos la tabla con las columnas requeridas
    st.session_state.table_data = pd.DataFrame(
                    columns=["Producto", "Precio", "Cantidad", "Subtotal"]
                    )
    
# Titulo de la pagina
st.title("On D' toledo - SuperMarket")

# crearemos contenedor para el formulario
with st.form("formulario_producto"):
    
    # Ingresar el nombre del producto
    producto = st.text_input("Nombre del Producto")
    
    # Ingresar el precio del producto
    precio = st.number_input("Precio del Producto", min_value=0.0, step=0.01, format="%.2f")
    
    # Ingresar la cantidad del producto
    cantidad = st.number_input("Cantidad del Producto", min_value=1, step=1)
    
    #botom para agreagr producto a la tabla
    subtotal = st.form_submit_button("Agregar Producto")
    
     # Boton para agregar el producto a la tabla
if subtotal:
    # llama a la funcion para calcular el subtotal
    calcular_subtotal(producto, precio, cantidad)
    
# botom para limpiar la tabla
limpiar_tabla = st.button("Limpiar Tabla")
if limpiar_tabla:
    # Limpiar la tabla en session_state
    st.session_state.table_data = pd.DataFrame(columns=["Producto", "Precio", "Cantidad", "Subtotal"])
    st.success("Tabla limpiada correctamente.")
    
#pintamos la tabla del dataframe
st.dataframe(st.session_state.table_data, use_container_width=True)
#st.dataframe(st.session_state.table_data)
    
if st.button("Calcular Total"):
    # Calcular el total de la tabla
    total = (st.session_state.table_data["Precio"] * st.session_state.table_data["Cantidad"]).sum()
    
    # Mostrar el total en la consola
    st.subheader("El total de la compra es:")
    
    # Mostrar el total en la interfaz
    #st.success(f"${total}" icon="💰")
    st.markdown(f"<span style='font-size:2em; color:green;'>💰 ${total}</span>", unsafe_allow_html=True)