# En un diccionario las claves no se pueden repetir, pero sí que se pueden repetir los valores
mi_diccionario = {
    'clave1':'valor1', 
    'clave2':'valor2'
}
print(type(mi_diccionario))
print(mi_diccionario)

# Consultar elementos del diccionario
resultado = mi_diccionario['clave1']
print(resultado)

mi_cliente = {
    'nombre':'Javier',
    'apellido': 'Iranzo',
    'altura': 1.80,
    'edad': 31
}
consulta = mi_cliente['apellido']
print(consulta)

mi_diccionario2 = {
    'clave1': 55,
    'clave2': [10, 20, 30],
    'clave3': {
        's1': 100,
        's2': 200,
        's3': 300
    }
}
print(mi_diccionario2['clave1'])
print(mi_diccionario2['clave2'][1])
print(mi_diccionario2['clave3']['s3'])

mi_diccionario3 = {
    'c1':['a', 'b', 'c'],
    'c2':['d', 'e', 'f']
}
print(mi_diccionario3['c2'][1].upper())

# Agregar elementos a un diccionario
mi_diccionario4 = {
    1: 'a', 
    2: 'b'
}
mi_diccionario4[3] = 'c'
print(mi_diccionario4)

# Sobreescribir elementos de un diccionario
mi_diccionario4[2] = 'B' 
print(mi_diccionario4)

# Conocer todas las claves de un diccionario
print(mi_diccionario4.keys())

# Conocer todos los valores de un diccionario
print(mi_diccionario4.values())

# Conocer todos los elementos de un diccionario
print(mi_diccionario4.items)