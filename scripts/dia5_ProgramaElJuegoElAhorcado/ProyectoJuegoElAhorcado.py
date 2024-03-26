from random import choice


intentos = 6
aciertos = 0
lista_palabras = ['casa', 'almohada', 'cocina', 'habitacion', 'puerta', 'terraza']
letras_correctas = []
letras_incorrectas = []
juego_acabado = False


def eleccion_palabra_aleatoria(lista_palabras):
    palabra_aleatoria = choice(lista_palabras)
    letras_unicas = len(set(palabra_aleatoria))
    return palabra_aleatoria, letras_unicas

def eleccion_letra_usuario():
    letra_ingresada = ''
    lista_letras = 'abcdefghijklmnñopqrstuvwxyz'
    es_valida = False
    while not es_valida:
        letra_ingresada = input('Elige una letra: ')
        if letra_ingresada in lista_letras and len(letra_ingresada) == 1:
            es_valida = True
        else:
            print('Elige una letra correcta')
    return letra_ingresada

def mostrar_tablero(palabra):
    lista_oculta = []
    for letra in lista_oculta: 
        if letra in letras_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))
        
def comprobar_si_esta_letra(letra_elegida, palabra_oculta, intentos, coincidencias): 
    juego_acabado = False; 
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas: 
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print(f'Ya has encontrado la letra {letra_elegida} prueba otra letra')
    else: 
        letras_incorrectas.append(letra_elegida)
        intentos -= 1
    if intentos == 0:
        juego_acabado = derrota()
    elif coincidencias == letras_unicas:
        juego_acabado = victoria(palabra_oculta)
    return intentos, juego_acabado, coincidencias
        
def derrota():
    print('Te has quedado sin vidas')
    print('La palabra oculta era ' + palabra_aleatoria)
    return True

def victoria(palabra_oculta):
    mostrar_tablero(palabra_oculta)
    print('Correcto, la palabra era ' + palabra_oculta)
    return True    

print('########################################')
print('### BIENVENIDO AL JUEGO DEL AHORCADO ###')
print('########################################')

nombre_jugador = input("Ingresa tu nombre: ")
print(f'Hola, {nombre_jugador.upper()}, empezamos a jugar. Tienes {intentos} vidas')

palabra_aleatoria, letras_unicas = eleccion_palabra_aleatoria(lista_palabras)
while not juego_acabado:
    print('\n' + '*' * 20 + '\n')
    mostrar_tablero(palabra_aleatoria)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Tienes {intentos} vidas')
    letra = eleccion_letra_usuario()
    intentos, terminado, aciertos = comprobar_si_esta_letra(letra, palabra_aleatoria, intentos, aciertos)
    juego_acabado = terminado
    
       
 



        
