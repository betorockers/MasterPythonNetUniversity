def multiplicador_palabras(texto, cantidad):
    
    return texto * cantidad

resultado = multiplicador_palabras("betoRock \n", 20)
print(resultado)  # Imprime "betoRock " repetido 20 veces

def multiplicador_notacion(texto: str, cantidad = int) -> str:
    return texto * cantidad

resultado_notacion= multiplicador_notacion("betoRock ", 50)
print(resultado_notacion)  # Imprime "betoRock" repetido 50 veces