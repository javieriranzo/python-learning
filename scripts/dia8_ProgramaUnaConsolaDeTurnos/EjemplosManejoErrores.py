# Estructura bloque try - except - else - finally
# try:
#   Código que se quiere probar
# except: 
#   Código a ejectuar si hay error
# else: 
#   Código que se va a ejecutar si no hay error
# finally
#   Código que se ejecute pase lo que pase

def suma(): 
    n1 = int(input('Introduce el número 1: '))
    n2 = int(input('Introduce el número 2: '))
    print(n1 + n2)
    
try: 
    suma()
except:
    print('Algo no ha funcionado bien')
else:
    print('Datos correctos')
finally:
    print('Programa finalizado')
    
# Manejo de excepciones
def resta(): 
    n1 = int(input('Introduce el número 1: '))
    n2 = int(input('Introduce el número 2: '))
    print(n1 - n2)
    
try:
    resta()
except ValueError:
    print('El dato introducido no es un número')
else: 
    print('Datos correctos')
finally:
    print('Programada finalizado')
    
# Ejemplo pedir numero por teclado
def pedir_numero(): 
    while True: 
        try: 
            numero = int(input('Introduce un número: '))
        except:
            print('El valor introducido no es un número')
        else:
            print(f'Ingresaste el número {numero}')
            break
    print('Programa finalizado')