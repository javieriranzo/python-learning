# Módulo de sistema operativo
import os 
from pathlib import Path

# Obtener el directorio de trabajo actual
ruta = os.getcwd()
print(f'El directorio de trabajo actual es: {ruta}')

# Cambiar de directorio
ruta = os.chdir('C:\\Users\\jiranzo\\Documents\\Repositorios\\Personales\\python-learning\\resources\\dia6_ProgramaUnRecetario')
# No muestra la nueva ruta, porque solo con el método chdir ha cambiado el directorio
print(f'Ahora la ruta de trabajo actual es: {ruta}')

# Se prueba a abrir e imprimir un archivo que está situado en la nueva ruta que se le pasa utilizando el método chdir
archivo = open('Prueba.txt')
print(archivo.read())

# Crear carpeta
# ruta = os.makedirs('C:\\Users\\jiranzo\\Documents\\Repositorios\\Personales\\python-learning\\resources\\dia6_ProgramaUnRecetario\\otracaepta')

# Eliminar carpetas
# os.rmdir('C:\\Users\\jiranzo\\Documents\\Repositorios\\Personales\\python-learning\\resources\\dia6_ProgramaUnRecetario\\otracaepta')

# Una ruta tiene que estar compuesta por dos elementos: El nombre de la ruta y el nombre del archivo. Para esto se puede utilizar los métodos basename y dirname
ruta = 'C:\\Users\\jiranzo\\Documents\\Repositorios\\Personales\\python-learning\\resources\\dia6_ProgramaUnRecetario\\Prueba.txt'
elemento = os.path.basename(ruta)
print(elemento)
elemento = os.path.dirname(ruta)
print(elemento)
# Recuperar el 'elemento' con la información de la ruta y el nombre del archivo dentro de una tupla
elemento = os.path.split(ruta)
print(elemento)

# Abrir archivo que está en una ruta distinta a la ruta de trabajo 
archivo_fuera_ruta_trabajo = open('C:\\Users\\jiranzo\\Documents\\Repositorios\\Personales\\python-learning\\resources\\dia6_ProgramaUnRecetario\\Prueba.txt')
print(archivo_fuera_ruta_trabajo.read())

# Como crear rutas para que sean interpretadas por cualquier sistema operativo
# Para ello se utiliza el módulo path (importado arriba)
carpeta = Path('C:/Users/jiranzo/Documents/Repositorios/Personales/python-learning/resources/dia6_ProgramaUnRecetario')
archivo2 = carpeta / 'Prueba2.txt'
mi_archivo = open(archivo2)
print(mi_archivo.read())




