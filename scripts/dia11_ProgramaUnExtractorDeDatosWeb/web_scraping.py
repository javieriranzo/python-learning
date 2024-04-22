import bs4
import requests

# Crear url base sin paginación
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
# Lista titulos con 4 o 5 estrellas
titulos_con_rango_alto = []

for numero_pagina in range(1, 51):
    # Imprimir detalles de todos los libros 
    url_pagina = url_base.format(numero_pagina)
    resultado = requests.get(url_pagina)
    contenido = bs4.BeautifulSoup(resultado.text, 'lxml')
    libros = contenido.select('.product_pod')
    # Iterar en cada libro
    for libro in libros:
        # Comprobar que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']
            # Agregar titulo a la lista
            titulos_con_rango_alto.append(titulo_libro)
    
# Imprimir libros
for titulos in titulo_libro:
        print(titulos)
    
