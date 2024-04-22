import bs4
import requests

titulo_pagina = requests.get('https://www.escueladirecta.com/p/excel-aplicado-al-analisis-financiero')
contenido = bs4.BeautifulSoup(titulo_pagina.text, 'lxml')
container = contenido.select('.container p')
for div in container:
    print(div.getText())