# Módulo introducido en la versión 3.4 de Python

from pathlib import Path
from pathlib import PureWindowsPath

carpeta = Path('C:/Users/jiranzo/Documents/Repositorios/Personales/python-learning/resources/dia6_ProgramaUnRecetario/Prueba2.txt')

# Abrir documentos utilizando el módulo pathlib (Ahora 'carpeta' es un elemento Path)
# No hace falta utilizar los métodos open y close
print(carpeta.read_text())

# Devolver el nombre del archivo
print(carpeta.name)

# Devolver la extensión del archivo
print(carpeta.suffix)

# Devolver el nombre sin la extensión del archivo
print(carpeta.stem)

# Comprobar la existencia del archivo 
if not carpeta.exists():
    print('El archivo NO existe')
else:
    print('El archivo SI existe')
    
# Transformar cualquier ruta en una ruta con formato de Windows
carpeta_windows = PureWindowsPath(carpeta)
print(carpeta_windows)