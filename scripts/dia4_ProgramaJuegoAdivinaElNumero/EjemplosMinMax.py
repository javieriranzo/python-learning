# min - max --> Se utilizan para averiguar los elementos máximos y mínimos de una colección

# Pruebas con Strings
nombre = 'Javier'
print(min(nombre)) # Saca la "J" primero porque primero busca por mayúsculas
print(min(nombre.lower())) # Saca la "a" porque es la primera alfabéticamente

# Pruebas con listas
mi_lista_numeros = [1, 2, 3, 4, 5]
mi_lista_letras = ['a', 'b', 'c', 'd']
mayor_numeros = max(mi_lista_numeros)
menor_numeros = min(mi_lista_numeros)
mayor_letras = max(mi_lista_letras)
menor_letras = min(mi_lista_letras);
print(f"El mayor de los números es: {mayor_numeros}")
print(f"El menor de los números es: {menor_numeros}")
print(f"La mayor de las letras es: {mayor_letras}")
print(f"La menor de las letras es: {menor_letras}")

# Pruebas con diccionarios
mi_diccionario = {
    'c1': 1,
    'c2': 2,
    'c3': 3
}

print(max(mi_diccionario)) # Muestra la clave más alta
print(min(mi_diccionario)) # Muestra la clave más baja
print(max(mi_diccionario.values())) # Muestra el valor más alto
print(min(mi_diccionario.values())) # Muestra el valor más bajo
