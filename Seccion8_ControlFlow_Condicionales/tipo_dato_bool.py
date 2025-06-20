# Los booleanos son un tipo de dato que puede tener dos valores: True o False.
# Se pueden utilizar en condiciones para controlar el flujo del programa.

administrador = True
usuario = False

# Ejemplo de uso de booleanos en una condición
print('---' *10 + ' Condicionales con booleanos ' + '---' * 10)

print('--' *10 + ' ejemplo 1 ' + '---' * 10 + '\n')

dos_menor_cuatro = 2 < 4

print(f'2 es menor que 4: {dos_menor_cuatro}')  # Imprime True porque 2 es menor que 4

print('\n' + '--' *10 + ' ejemplo 2 ' + '---' * 10 + '\n')

cinco_menor_10 = 5 > 10
print(f'5 es mayor que 10: {cinco_menor_10}')  # Imprime True porque 5 es menor que 10

print('\n' + '--' *10 + ' ejemplo 3 ' + '---' * 10 + '\n')

a = 100 > 200
print(f'100 es mayor que 200: {a}')  # Imprime False porque 100 no es mayor que 200

print('\n' + '--' *10 + ' ejemplo 4 ' + '---' * 10 + '\n')

c = "beto" == "Beto"
print(f'"beto" es igual a "Beto": {c}')  # Imprime False porque "beto" no es igual a "Beto" (diferencia de mayúsculas y minúsculas)

print('\n' + '--' *10 + ' ejemplo 5 ' + '---' * 10 + '\n')

d = "beto" == "beto"
print(f'"beto" es igual a "beto": {d}')  # Imprime True porque "beto" es igual a "beto"

print('\n' + '--' *10 + ' ejemplo 6 ' + '---' * 10 + '\n')

x = 50 == 50
print(f'50 es igual a 50: {x}')  # Imprime True porque 50 es igual a 50

print('\n' + '--' *10 + ' ejemplo 7 ' + '---' * 10 + '\n')

y = 50 >= 49
print(f'50 es mayor o igual que 49: {y}')  # Imprime True porque 50 es mayor o igual que 49


print('\n' + '--' *10 + ' ejemplo 8 ' + '---' * 10 + '\n')

z = 89 <= 100

print(f'89 es menor o igual que 100: {z}')  # Imprime True porque 89 es menor o igual que 100

print('\n' + '--' *10 + ' ejemplo 9 ' + '---' * 10 + '\n')

g = "gato" != "perro"
print(f'"gato" es diferente de "perro": {g}')  # Imprime True porque "gato" es diferente de "perro"

print('\n' + '--' *10 + ' ejemplo 10 ' + '---' * 10 + '\n')

m = "juan" != "juan"
print(f'"juan" es diferente de "juan": {m}')  # Imprime False porque "juan" es igual a "juan"

print('\n' + '--' *10 + ' ejemplo 11 ' + '---' * 10 + '\n')

print( 5 != 5)  # Imprime False porque 5 es igual a 5

print('\n' + '--' *10 + ' ejemplo 12 ' + '---' * 10 + '\n')

print(50 == 50)  # Imprime True porque 50 es igual a 50

print('\n' + '--' *10 + ' ejemplo 13 ' + '---' * 10 + '\n')