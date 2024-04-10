def decorar_saludo(funcion): 
    def modificar_palabra(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')
    return modificar_palabra

def mayusculas(texto): 
    print(texto.upper())
    
def minusculas(texto):
    print(texto.lower())
    
minusculas('PyThOn')
mayusculas('PyThOn')

minusculas_decorada = decorar_saludo(minusculas)
minusculas_decorada('JaViEr')
mayusculas_decorada = decorar_saludo(mayusculas)
mayusculas_decorada('JaViEr')