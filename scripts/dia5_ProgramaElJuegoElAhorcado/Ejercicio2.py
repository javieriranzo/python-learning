def devolucion_sin_repetidas(palabra): 
    letras_unicas = set(palabra)
    letras_ordenadas = sorted(letras_unicas)
    return letras_ordenadas

palabra_usuario = input("Introduce una palabra: ")
print(devolucion_sin_repetidas(palabra_usuario))