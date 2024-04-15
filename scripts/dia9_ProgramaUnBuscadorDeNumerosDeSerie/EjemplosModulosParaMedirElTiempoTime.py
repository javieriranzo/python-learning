import time


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

inicio_prueba_for = time.time()
prueba_for(10000000)
final_prueba_for = time.time()
tiempo_prueba_for = final_prueba_for-inicio_prueba_for
print(tiempo_prueba_for)

inicio_prueba_while = time.time()
prueba_while(10000000)
final_prueba_while = time.time()
tiempo_prueba_while = final_prueba_while-inicio_prueba_while
print(tiempo_prueba_while)