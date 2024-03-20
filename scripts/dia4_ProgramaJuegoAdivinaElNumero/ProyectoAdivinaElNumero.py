from random import randint




respuesta_jugador = 0
intentos = 0
numero_aleatorio = randint(1, 100)
nombre_jugador = input("Introduce tu nombre: ")

print(f"Hola {nombre_jugador}, tienes que adivinar el número aleatorio entre 1 - 100 en 8 intentos")
print("### BIENVENIDO A ADIVINA UN NUMERO ###")

while(intentos < 8): 
    respuesta_jugador = int(input("Introduce el número: "))
    intentos += 1
    if (respuesta_jugador not in range(1,101)):
        print(f"El número {respuesta_jugador} está fuera de los rangos")
    elif(respuesta_jugador > numero_aleatorio):
        print(f"{respuesta_jugador} es mayor que el numero buscado")
    elif(respuesta_jugador < numero_aleatorio):
        print(f"{respuesta_jugador} es menor que el numero buscado")
    else: 
        print(f"¡Correcto! La respuesta: {respuesta_jugador} coincide con el número: {numero_aleatorio}")
        break

if(respuesta_jugador != numero_aleatorio):
    print(f"Llevas {intentos} intentos, se te acabaron las oportunidades")   
    print(f"El número que buscabamos era: {numero_aleatorio}") 