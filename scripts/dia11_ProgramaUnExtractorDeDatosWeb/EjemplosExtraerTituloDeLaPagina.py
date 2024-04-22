import bs4
import requests

titulo_pagina = requests.get('https://escueladirecta-blog.blogspot.com/')
print(type(titulo_pagina))
print(titulo_pagina)
print(titulo_pagina.text)

contenido = bs4.BeautifulSoup(titulo_pagina.text, 'lxml')
print(contenido)
print(contenido.select('title')) # Lo devuelve en una lista porque una etiqueta puede aparecer varias veces
print(len(contenido.select('link'))) # Cantidad que aparece la etiqueta <link>
print(contenido.select('title')[0].getText()) # Recupera solo el texto de la etiqueta