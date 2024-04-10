# Generadores
def generar_numeros_perfumeria():
    for n in range(1, 10000):
        yield f'P - {n}'
        
def generar_numeros_farmacia():
    for n in range(1, 10000):
        yield f'F - {n}'
        
def generar_numeros_cosmetica():
    for n in range(1, 10000):
        yield f'C - {n}'
        
numero_perfumeria = generar_numeros_perfumeria()
numero_farmacia = generar_numeros_farmacia()
numero_cosmetica = generar_numeros_cosmetica()
    
# Decoradores
def generar_decorador_numeros(rubro):
    print('\n' + '*' * 23)
    print('Su numero es: ')
    if rubro == 'P':
        print(next(numero_perfumeria))
    if rubro == 'F':
        print(next(numero_farmacia))
    if rubro == 'C':
        print(next(numero_cosmetica))
    print('Espere y será atendido')
    print('\n' + '*' * 23)
