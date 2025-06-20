# indices 

texto = "Python"

print(texto[0]) # buscamos el primer caracter
print(texto[1]) # buscamos el segundo caracter
print(texto[2]) # buscamos el tercer caracter
print(texto[3]) # buscamos el cuarto caracter
print(texto[4]) # buscamos el quinto caracter
print(texto[5]) # buscamos el sexto caracter
print(texto[-1]) # buscamos el ultimo caracter
print(texto[-2]) # buscamos el penultimo caracter
print(texto[-3]) # buscamos el antepenultimo caracter
print(texto[-4]) # buscamos el anteantepenultimo caracter
print(texto[-5]) # buscamos el anteanteantepenultimo caracter
print(texto[-6]) # buscamos el anteanteanteantepenultimo caracter

for i in range(len(texto)):
    print(texto[i]) # recorremos el texto con un bucle for

print()


otro_texto = "Python es un lenguaje de programacion"
cantidad_caracteres = len(otro_texto)
ultimo_caracter = otro_texto[cantidad_caracteres - 1] # obtenemos el ultimo caracter
print(cantidad_caracteres) # mostramos la cantidad de caracteres del texto
print(otro_texto[20])
print(ultimo_caracter)