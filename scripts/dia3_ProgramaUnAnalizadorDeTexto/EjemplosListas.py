mi_lista = ['a', 'b', 'c']
mi_lista_2 = ['d', 'e', 'f']

# Imprimir tipo de dato de una lista
print(type(mi_lista))

# Comprobar largo de una lista
resultado = len(mi_lista)
print(resultado) 

# Indexar listas
print(mi_lista[0])

# Buscar por intervalo
resultado_2 = mi_lista[0:2]
print(resultado_2) 

# Concatenar listas
print(mi_lista + mi_lista_2) 

# Sobreescribir elementos de una lista
mi_lista[0] = "alpha" 
print(mi_lista)

# Añadir elemento a una lista
mi_lista_2.append("g")
print(mi_lista_2)

# Eliminar elemento de una lista
mi_lista_2.pop()  # Si no se le pasa ningún parámetro elimina el último elemento
mi_lista_2.pop(0) # Elimina el elemento que está en la posición 0

# Ordenar lista. El método sort no devuelve nada, no se puede guardar la lista ordenada.
mi_lista3 = ['a', 'z', 's', 'b', 'h']
mi_lista3.sort() 
print(mi_lista3)

# Revertir el orden. 
mi_lista3.reverse()
print(mi_lista3) 