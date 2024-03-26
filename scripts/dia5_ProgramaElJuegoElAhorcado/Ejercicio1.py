# Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros. Si la suma de los 3 numeros es
# mayor a 15, va a devolver el número mayor. Si la suma de los 3 numeros es menor a 10, va a devolver el número menor.
# Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el número de valor intermedio.

def devolver_distintos(a, b, c):
    suma = a + b + c
    if (suma > 15):
        return max(a, b, c)
    elif(suma < 10):
        return min(a, b, c)
    elif(suma >= 10 or suma <= 15):
        numeros = [a, b, c]
        numeros.remove(max(numeros))
        numeros.remove(min(numeros))
        return numeros[0]

numero_introducido1 = int(input("Introduce el primer numero: "))
numero_introducido2 = int(input("Introduce el segundo numero: "))
numero_introducido3 = int(input("Introduce el tercer numero: "))

resultado = devolver_distintos(numero_introducido1, numero_introducido2, numero_introducido3)
print(f"Resultado: {resultado}")