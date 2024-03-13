# Random --> Generación de números aleatorios

# Random es una librería de Python que no viene cargado por defecto. Hay que importar la librería
from random import randint
from random import uniform
from random import random
from random import choice
from random import shuffle

# Crear número aleatorio. Se utiliza el método randint. Recibe como parámetro 2 ints que son el intervalo entre los cuales tiene que estar en número aleatorio
aleatorio1 = randint(1, 50) 
print(f"Nº aleatorio entre [1-50]: {aleatorio1}")

# Uniform. Devuelve un aleatorio decimal dentro del intervalo indicado en los parámetros
aleatorio2 = uniform(1, 5)
print(f"Nº aleatorio con decimales entre [1-5]: {aleatorio2}")
# Para utilizar menos decimales, utilizar la funcion round. El último parámetro es la cantidad de decimales
aleatorio3 = round(uniform(1, 5), 1)
print(f"Nº aleatorio con 1 solo decimal entre [1-5]: {aleatorio3}")

# Random. Devuelve un aleatorio decimal entre [0-1]
aleatorio4 = random()
print(f"Nº aleatorio con decimales entre [0-1]: {aleatorio4}")
# Para utilizar menos decimales, utilizar la funcion round. El último parámetro es la cantidad de decimales
aleatorio5 = round(random(), 1)
print(f"Nº aleatorio con 1 solo decimal entre [0-1]: {aleatorio5}")

# Choice. Devuelve un elemento aleatorio en una lista (pueden ser listas u otros iterables)
lista_colores = ['azul', 'verde', 'rojo', 'amarillo', 'blanco', 'negro']
aleatorio6 = choice(lista_colores)

# Shuffle. Se utiliza para mezclar los elementos de una lista
lista_numeros = list(range(5, 55, 5)) # Se crea una lista de números entre 5 y 50 que cree los elementos de 5 en 5
shuffle(lista_numeros) # Shuffle no se puede utilizar con elementos inmutables
print(f"La lista mezclada es: {lista_numeros}.")