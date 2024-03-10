print(" --- ¡¡BIENVENIDO AL ANALIZADOR DE TEXTOS!! --- ")

texto = input("Introduce el texto: ")
letras = []
texto = texto.lower()

letras.append(input("Ingresa la primera letra: ").lower()) # letras[0]
letras.append(input("Ingresa la segunda letra: ").lower()) # letras[1]
letras.append(input("Ingresa la tercera letra: ").lower()) # letras[2]

print("\n")

print("Cantidad de letras:")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Se ha encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Se ha encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Se ha encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")

print("\n")

print("Cantidad de palabras: ")
cantidad_palabras = texto.split() # Separa el texto por espacios en blanco
print(f"La cantidad de palabras que hay en el texto es {len(cantidad_palabras)}")

print("\n")

print("Letras de inicio y de fin: ")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"La letra de inicio es: '{letra_inicio.upper()}'")
print(f"La letra de fin es: '{letra_fin}'")

print("\n")

print("Invertir texto")
palabras = texto.split()
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"El texto invertido es '{texto_invertido}'")

print("\n")

print("Comprobar si la palabra 'Python' está en el texto: ")
buscar_python = 'python' in texto
dic = {
    True: "sí",
    False: "no"
}
print(f"La palabra 'Python' {dic[buscar_python]} está en el texto")