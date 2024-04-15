import timeit

def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero): 
    lista = [] 
    contador = 1
    while contador <= numero: 
        lista.append(contador)
        contador += 1
    return lista

declaracion_prueba_for = '''
prueba_for(10)
'''

setup_prueba_for= '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''

duracion_prueba_for = timeit.timeit(declaracion_prueba_for, setup_prueba_for, number = 10000000)
print(duracion_prueba_for)

declaracion_prueba_while = '''
prueba_while(10)
'''

setup_prueba_while = '''
def prueba_while(numero): 
    lista = [] 
    contador = 1
    while contador <= numero: 
        lista.append(contador)
        contador += 1
    return lista
'''

duracion_prueba_while = timeit.timeit(declaracion_prueba_while, setup_prueba_while, number = 10000000)
print(duracion_prueba_while)