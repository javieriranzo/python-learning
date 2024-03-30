import os
from pathlib import Path
from os import system

ruta_recetas = Path('C:/Users/jiranzo/Documents/Repositorios/Personales/python-learning/resources/dia6_ProgramaUnRecetario/Recetas')

def cantidad_recetas(ruta):
    cantidad = 0
    for archivo in Path(ruta).glob('**/*.txt'):
        cantidad += 1
    return cantidad

def mostrar_menu_inicio():
    system('cls') # Si se tratara de un sistema Linux, se tendría que utilizar 'clear'
    print('***************************************')
    print('¡BIENVENIDO AL ADMINISTRADOR DE RECETAS')
    print('***************************************')
    print(f'Las recetas se encuentran en: {ruta_recetas}')
    print(f'El total de recetas actual es: {cantidad_recetas(ruta_recetas)}')
    eleccion_usuario = 'x'
    while not eleccion_usuario.isnumeric() or int(eleccion_usuario) not in range(1,7):
        print('''
              [1] - Leer una receta
              [2] - Crear una receta nueva 
              [3] - Crear una categoría nueva 
              [4] - Eliminar una receta existente
              [5] - Eliminar una categoría existente
              [6] - Salir del programa
              ''')
        eleccion_usuario = input('Elige una opción: ')
    return int(eleccion_usuario)

def mostrar_categorias_recetas(ruta):
    print('Categorías: ')
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1 
    for carpeta in ruta_categorias.iterdir(): # Método que permite iterar dentro del directorio para pasar por cada una de sus carpetas
        nombre_carpeta = str(carpeta.name)
        print(f'[{contador}] - {nombre_carpeta}')
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias

def elegir_categoria(lista_categorias): 
    eleccion_categoria = 'x'
    while not eleccion_categoria.isnumeric() or int(eleccion_categoria) not in range(1, len(lista_categorias) + 1):
        eleccion_categoria = input('Introduce la categoría deseada: ')
    return lista_categorias[int(eleccion_categoria) - 1]

def mostrar_recetas(ruta): 
    print('Recetas: ')
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob('**/*.txt'):
        receta_nombre = str(receta.name)
        print(f'[{contador}] - {receta_nombre}')
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas

def elegir_receta(lista_recetas):
    eleccion_receta = 'x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta) not in range(1, len(lista_recetas) + 1):
        eleccion_receta = input('Introduce la receta deseada: ')
    return lista_recetas[int(eleccion_receta) - 1]

def leer_receta(receta): 
    print(Path.read_text(receta))
    
def crear_receta(ruta): 
    existe = False
    while not existe:
        nombre_receta = input('Escribe el nombre de la receta: ')
        nombre_receta_final = nombre_receta + '.txt'
        contenido_receta = input('Escribe la nueva receta: ')
        ruta_nueva = Path(ruta, nombre_receta_final)
        if not os.path.exists(ruta_nueva): 
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Receta {nombre_receta} ha sido creada')
            existe = True
        else:
            print('La receta ya existe')
            
def crear_categoria(ruta):
    existe = False
    while not existe: 
        nombre_categoria = input('Escribe el nombre de la categoría: ')
        ruta_nueva = Path(ruta, nombre_categoria)
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Categoria {nombre_categoria} ha sido creada')
            existe = True
        else:
            print('La categoría ya existe')
        
def eliminar_receta(receta): 
    Path(receta).unlink()
    print(f'La receta {receta.name} ha sido eliminada')
    
def eliminar_categoria(categoria): 
    Path(categoria).rmdir()
    print(f'La categoria {categoria} ha sido eliminada')

def volver_inicio(): 
    eleccion_usuario = 'x'
    while eleccion_usuario.lower() != 'v': 
        eleccion_usuario = input('Presiona V para volver al menú: ')
        

# Menú de inicio: El usuario elegirá una opción
finalizar_programa = False
while not finalizar_programa:
    menu = mostrar_menu_inicio()
    if menu == 1: 
        mis_categorias = mostrar_categorias_recetas(ruta_recetas)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()
    elif menu == 2: 
        mis_categorias = mostrar_categorias_recetas(ruta_recetas)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
    elif menu == 3:
        crear_categoria(ruta_recetas)
        volver_inicio()
    elif menu == 4: 
        mis_categorias = mostrar_categorias_recetas(ruta_recetas)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        mi_receta = elegir_receta(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 5: 
        mis_categorias = mostrar_categorias_recetas(ruta_recetas)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
    elif menu == 6: 
        finalizar_programa = True