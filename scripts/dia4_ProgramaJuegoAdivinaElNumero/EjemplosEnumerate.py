lista = ['a', 'b', 'c']
indice = 0
for item in lista:
    print(indice, item)
    indice += 1
    
# Usando enumerate
lista2 = ['d', 'e', 'f']
for indice, item2 in enumerate(lista2): 
    print(indice, item2)
    
# Crear tuple a partir de una lista
lista3 = ['g', 'h', 'i']
tuple = list(enumerate(lista3))
print(tuple)
print(tuple[1][0])
print("python".trim())