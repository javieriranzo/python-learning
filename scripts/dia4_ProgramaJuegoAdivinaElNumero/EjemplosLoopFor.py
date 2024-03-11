nombres = ['Juan', 'Jorge', 'Javier', 'Rocío', 'Concha', 'Natalia']
for nombre in nombres:
    posicion_nombre = nombres.index(nombre)
    print(f"En la posición {posicion_nombre} está el nombre {nombre}. Hola " + nombre)
    if nombre.startswith('J'):
        print("Este nombre sí empieza por 'J'")
    else:
        print("Este nombre no empieza por 'J'")
        
numeros = [1, 2, 3, 4, 5]
mi_valor = 0
for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)    
    
palabra = "python"
for letra in palabra:
    print(letra)

# Iteracion en lista compuesta por listas

# Iteracion en diccionarios
mi_diccionario = {
    'clave1':'a',
    'clave2':'b',
    'clave3':'c'
}
for item in mi_diccionario.items(): 
    print(item)
    
for item in mi_diccionario.values():
    print(item)