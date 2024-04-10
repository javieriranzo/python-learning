import numeros

def opcion_elegida_usuario(): 
    print('Bienvenido a Farmacia Python')
    while True: 
        print('[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética')
        try:
            mi_rubro = input('Elija una sección: ').upper()
            ['P', 'F', 'C'].index(mi_rubro)
        except ValueError:
            print('La opción no es válida')
        else: 
            break
    numeros.generar_decorador_numeros(mi_rubro)
    
def iniciar():
    while True: 
        opcion_elegida_usuario()
        try:
            otro_turno = input('¿Quiere obtener otro turno? S/N: ').upper()
            ['S', 'N'].index(otro_turno)
        except ValueError:
            print('La opción no es válida')
        else:
            if otro_turno == 'N':
                print('Gracias por su visita')
                break
            
iniciar()
            