import os
import shutil
import send2trash # type: ignore

# Imprimir el directorio de trabajo
print(os.getcwd()) 

# Crear archivo que no existe con contenido
archivo = open('curso.txt', 'w')
archivo.write('Hola mundo')
archivo.close()
print('Archivo creado')

# Mover archivos
shutil.move('curso.txt', '//home//jiranzo//Repositorios//Personales//python-learning//scripts//dia9_ProgramaUnBuscadorDeNumerosDeSerie')

# Eliminar archivos
# os.unlink         --> Elimina archivo en una ruta que se le pasa por parámetro
# os.rmdir          --> Elimina una carpeta vacía que se le pasa por parámetro
# shutil.rmtree     --> Elimina todo el contenido que se encuentra en la ruta que se pasa por parámetro - ¡¡CUIDADO IRREVERSIBLE!!
# Módulo send2trash --> Elimina el archivo que se le pasa por parámetro
send2trash.send2trash('curso.txt')
print('Archivo eliminado')

# Recorrer rutas de archivos
# os.walk --> Almacena primero la ruta donde se está, después las subcarpetas de la ruta y después los archivos de la ruta.
# Crea tuplas con 3 tipos de información: Ruta - Subcarpetas - Archivos
ruta = '//'
for carpeta, subcarpeta, archivo in os.walk(ruta):
     print(f'En la ruta: {carpeta}')
     print(f'Subcarpetas: ')
     for sub in subcarpeta:
         print(f'\t{sub}')
     print(f'Archivos: ')
     for arch in archivo:
         print(f'\t{arch}')
     print('\n')

# Listar archivos que empiecen por algo que se desee. En el ejemplo se listan los archivos que empiecen por 'ab'
ruta2 = '//'
for carpeta, subcarpeta, archivo in os.walk(ruta2):
    print(f'En la ruta: {carpeta}')
    print(f'Subcarpetas: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print(f'Archivos: ')
    for arch in archivo:
        if arch.startswith('ab'):
            print(f'\t{arch}')
    print('\n')