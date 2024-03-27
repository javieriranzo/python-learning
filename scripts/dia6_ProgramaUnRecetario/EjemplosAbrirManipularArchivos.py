# Abrir archivo
mi_archivo = open('resources/dia6_ProgramaUnRecetario\Prueba.txt')
# Mostrar archivo. No imprime el contenido. Muestra información sobre el archivo
print(mi_archivo)
# Leer el archivo. No muestra el archivo
archivo_leido = mi_archivo.read()
# Mostrar el archivo
print(archivo_leido)
# Volver el puntero al principio del archivo 
mi_archivo.seek(0)
# Leer una linea del archivo
linea_leida = mi_archivo.readline()
print(linea_leida)
linea_leida = mi_archivo.readline()
print(linea_leida)
linea_leida = mi_archivo.readline()
print(linea_leida)
# Leer todas las líneas y guardarlas en una lista
mi_archivo.seek(0)
lista_todas_lineas = mi_archivo.readlines()
print(lista_todas_lineas)
# Cerrar archivo
mi_archivo.close()
