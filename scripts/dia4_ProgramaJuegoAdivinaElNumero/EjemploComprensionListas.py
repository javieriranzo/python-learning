# Comprension -> Manera dinámica de construir una lista. Por ejemplo crear una lista desde un loop
palabra = 'Python'
lista = []
for letra in palabra: 
    lista.append(letra)
print(lista)

palabra2 = 'Javier'
lista2 = [letra for letra in palabra2]
print(lista2)

# Crear una lista con los números pares en el rango [0-20]
lista3 = [n for n in range(0, 21, 2)]
print(lista3)

talla_pies = [10, 20, 30, 40, 50]
talla_metros = [pies * 3.281 for pies in talla_pies]
print(talla_metros)