# Funcion normal
def devuelve_cuatro(): 
    return 4

print(devuelve_cuatro())

# Funcion generadora
def devuelve_cuatro_generadora(): 
    yield 4
    
g = devuelve_cuatro_generadora()
print(next(g))

def mult_10(): 
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista

print(mult_10())

def mult_10_generadora():
    for x in range(1, 5):
        yield x * 10

h = mult_10_generadora()
print(next(h))
print(next(h))
print(next(h))
print(next(h))

def suma_uno_generadora(): 
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x
    
i = suma_uno_generadora()
print(next(i))
print(next(i))
print(next(i))
