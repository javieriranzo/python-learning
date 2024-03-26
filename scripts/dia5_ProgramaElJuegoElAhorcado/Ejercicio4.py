import math

def es_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(numero)) + 1, 6):
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
    return True

def contar_primos(numero):
    contador = 0
    for i in range(numero + 1):
        if es_primo(i):
            print(i, end=" ")
            contador += 1
    print()  # Imprimir una nueva línea para mejor presentación
    return contador

# Ejemplo de uso
limite = 20
cantidad_primos = contar_primos(limite)
print(f"La cantidad de números primos en el rango de 0 a {limite} es: {cantidad_primos}")
