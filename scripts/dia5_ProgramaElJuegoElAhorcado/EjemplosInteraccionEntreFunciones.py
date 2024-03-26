from random import shuffle

# Crear lista inicial con los palitos
palitos = ['-', '--', '---', '----']

# Funcion de mezclar los palitos para que no se encuentren en orden
def mezclar(lista_palitos):
    shuffle(lista_palitos)
    return lista_palitos
mezclar(palitos)

# Pedir al usuario que elija un palito
def eleccion_jugador():
    intento = ''
    while(intento not in ['1', '2', '3', '4']):
        intento = input('Elige un numero del 1 al 4: ')
    return int(intento)

# Comprobar el resultado
def comprobar_resultado(lista_palitos, eleccion_jugador): 
    if(lista_palitos[eleccion_jugador - 1]) == '-':
        print('Te toca lavar los platos')
    else: 
        print('Te libras')
    print(f'Tu eleccion ha sido {lista_palitos[eleccion_jugador - 1]}')
    
palitos_mezclados = mezclar(palitos)
eleccion = eleccion_jugador()
resultado = comprobar_resultado(palitos_mezclados, eleccion)