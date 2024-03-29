from pathlib import Path

# Construit ruta con Path
guia = Path('Valencia', 'Ruzafa')
print(guia)

# Método home: Recuperar la ruta absoluta 
base = Path.home()
print(base)
print(f'{base}{guia}')

# Si se tuviese dos objetos Path, Python los une inteligentemente
guia2 = Path('Europa', 'España')
guia3 = Path('Castellón', 'Vinaros.txt')
guia_total = Path(base, guia2, guia3)
print(guia_total)

# Construir una ruta a partir de otra cambiando el destino final
guia4 = guia3.with_name('AlcudiaDeVeo.txt')
print(guia4)

# Acceder a directorios que están en el medio de otros
print(guia_total.parent.parent.parent)

# Enumerar (listar) los archivos de un directorio
guia_archivos = Path('C:/Users/jiranzo/Documents/Repositorios/Personales/python-learning/resources/dia6_ProgramaUnRecetario')
guia_europa = Path(guia_archivos, "Europa")
print(guia_europa)
for txt in Path(guia_europa).glob('**/*.txt'):
    print(txt)
    
# Calcular rutas relacionadas entre sí. Util para recuperar una porción de una ruta larga. El método relative_to devuelve un objeto Path
guia_relativa = Path('Europa', 'España', 'Valencia', 'Ruzafa', 'BukowskiCraftBeer')
que_hay_en_europa = guia_relativa.relative_to('Europa')
que_hay_en_espana = guia_relativa.relative_to('Europa', 'España')
que_hay_en_valencia = guia_relativa.relative_to('Europa', 'España', 'Valencia')
print(que_hay_en_europa)
print(que_hay_en_espana)
print(que_hay_en_valencia)
