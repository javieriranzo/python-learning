import bs4
import requests

titulo_pagina = requests.get('https://www.escueladirecta.com/courses/')
contenido = bs4.BeautifulSoup(titulo_pagina.text, 'lxml')

# Recuperar todas las imagenes de la web
imagenes_web = contenido.select('img')
for imagen in imagenes_web:
    print(imagen)
    
# Recuperar las imagenes con una clase
imagenes_cursos = contenido.select('.course-box-image')
for imagen_curso in imagenes_cursos:
    print(imagen_curso)
    
# Recuperar unicamente la url de las imagenes
url_imagenes = contenido.select('.course-box-image')[0]['src']
print(url_imagenes)
# Descargar imagen
imagen = requests.get(url_imagenes)
f = open('resources/dia11_ProgramaUnExtractorDeDatosWeb/mi_imagen.jpg', 'wb')
f.write(imagen.content)
f.close
