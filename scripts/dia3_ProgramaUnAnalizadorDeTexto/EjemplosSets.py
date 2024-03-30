# Forma 1 de crear los set - Indicando la palabra set y con ([]) porque al crear el set solo permite un argumento
mi_set = set([
    1, 2, 3, 4, 5
])
print(type(mi_set))
print(mi_set)

# Forma 2 de crear los set - Sin indicar la palabra set y envuelto entre {}
mi_set2 = {
    1, 2, 3
}
print(type(mi_set2))
print(mi_set2)

# Los set son elementos únicos por lo tanto no pueden tener repeticiones. 
# Si se agregan elementos repetidos. Python los descarta automáticamente.
# Los set no admiten en su interior ni listas ni diccionarios porque no son elementos inmutables. Sí que admiten tuples por ser elementos inmutables
mi_set3 = set([
    1, 2, 3, 4, 5, 5, 6, 7, 7, 8, 8, 8, 8, 9, 10
])
print(type(mi_set3))
print(mi_set3)

# Conocer el largo de un set
mi_set4 = set([
    'Hola', 'me', 'llamo', 'Javier'
])
print(type(mi_set4))
print(len(mi_set4))

# Comprobar si existe un elemento dentro de un set. Se puede hacer con listas también y con diccionarios se puede hacer si se buscan las claves
mi_set5 = set([
    'Hola', 'me', 'llamo', 'Natalia'
])
print('Natalia' in mi_set5)
print('Javier' in mi_set5)

# Unión de sets
# Al imprimir mi_set8 al aparecer el valor 3 tanto en mi_set6 como en mi_set7, se elimina. 
mi_set6 = set([1, 2, 3])
mi_set7 = set([3, 4, 5])
mi_set8 = mi_set6.union(mi_set7)
print(type(mi_set8))
print(mi_set8)

# Método add. Agregar elementos a un set
mi_set9 = set([1, 2, 3])
mi_set9.add(4)
mi_set9.add(3)
print(type(mi_set9))
print(mi_set9)

# Metodo remove. Eliminar elementos de un set
mi_set10 = set([
    'Hola',
    'Bienvenido',
    'a mi casa'
])
print(type(mi_set10))
print(mi_set10)
mi_set10.remove('Hola')
print(mi_set10)

# Método discard. Funciona igual que remove pero si se le pasa por parámetro un elemento que no existe, no da error, continua la ejecución
mi_set11 = set([
    'Hola',
    'Bienvenido',
    'a mi coche'
])
print(type(mi_set11))
print(mi_set11)
mi_set11.discard('Hola')
print(mi_set11)
mi_set11.discard('Adios')

# Método clear. Vacía el set de sus valores
mi_set12 = set([1, 2, 3, 4, 5])
print(type(mi_set12))
print(mi_set12)
mi_set12.clear()
print(mi_set12)

# Método pop. Elimina el primer elemento del set. Al no tener un orden cada vez se eliminará uno diferente
mi_set13 = set(['a', 'b', 'c', 'd', 'e', 'f'])
print(type(mi_set13))
print(mi_set13)
valor_set_eliminado = mi_set13.pop()
print(valor_set_eliminado)