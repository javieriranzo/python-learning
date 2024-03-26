# **kwargs = Argumentos indefinidos que trabajan con diccionarios

def suma(**kwargs): 
    print(type(kwargs))
suma(x=3, y=5, z=7) # Devuelve tipo de dato = dict

def ejemplo2(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
ejemplo2(x=3, y=5, z=7) 

def total(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
print(total(x=3, y=5, z=7))

def ejemploMezclaArgumentos(num1, num2, num3, *args, **kwargs):
    print(f"El primer valor es: {num1}")
    print(f"El segundo valor es: {num2}")
    print(f"El tercer valor es: {num3}")
    
    for arg in args:
        print(f"Los *args son: {arg}")
        
    for clave, valor in kwargs.items():
        print(f"La clave es: {clave} y el valor es: {valor}")
        
ejemploMezclaArgumentos(27, 17, 3, 1992,1961,1957, Javier=32, Concha=63, JavierPadre=67)

