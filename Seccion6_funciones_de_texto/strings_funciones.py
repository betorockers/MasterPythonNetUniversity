# funcion len()

texto = 'python'
cantidad_caracteres=len(texto)
print(f'La cantidad de caracteres en "{texto}" es: {cantidad_caracteres}')

texto_hola_cantidad = len('hola')
print(f'La cantidad de caracteres en "hola" es: {texto_hola_cantidad}')

print(len("betoledus"))

print(len(""))
print(len("@!%/#&"))
#print(len(5)) # Esto generará un error porque len() espera un objeto iterable(string), no un número

# multiplicacion de strings
print("---" * 30)

# concatenacion

print("beto" + " ledus")
print("beto " + "ledus")
print("beto" + "ledus")
print("beto" + " " + "ledus")
print("beto" "ledus")  # Repite la cadena 3 veces