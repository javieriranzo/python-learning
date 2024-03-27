# Método open() recibe dos parámetros
# - 1: Ruta donde se encuentra el archivo
# - 2: Método de apertura del archivo. Tipos de apertura:
#   - 'r' -> Solo lectura
#   - 'w' -> Solo escritura. Si el archivo existe, reescribe el contenido. Si el archivo no existe lo crea
#   - 'a' -> Escritura y actualización. Si el archivo existe, escribe el nuevo contenido al final. Si el archivo no existe lo crea

mi_archivo = open('resources/dia6_ProgramaUnRecetario/Prueba.txt', 'r')
archivo_leido = mi_archivo.read()
print(archivo_leido)
mi_archivo.close()



