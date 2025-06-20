nombre_completo = input("Ingrese su nombre completo: ")

def imprimir(nombre_completo):
    print(f"Hola {nombre_completo}")
    
# Llamada a la funcion
imprimir(nombre_completo)
#imprimir("Juan Perez")
#imprimir("Maria Lopez")

def sumar(a, b):
    """
    Esta funcion recibe dos numeros y retorna la suma de ellos.
    """
    c = a + b
    print(f"La suma de {a} + {b} es: {c}")
    
# Llamada a la funcion
sumar(5, 10)