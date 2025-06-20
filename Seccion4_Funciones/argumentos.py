def multiplicar(a,b,c):
    d = a * b * c
    print(f"el resultado de la multiplicacion es: {d}")  
    
# Llamada a la funcion
# se le llama argumento al valor que se le pasa a la funcion
multiplicar(2, 3, 4)
multiplicar(c=15, a=8, b=9)
multiplicar(8, b=9, c=15) # se puede omitir el primer argumento si se especifica el nombre del segundo y tercer argumento