# Carácteres
####################################################################
# | caracter | descripcion           | ejemplo      | ejemplo real |
# | /d       | digito numérico       | v\d.\d\d     | v1.0.4       |
# | /w       | caracter alfanumerico | \w\w\w-\w\w  | abc-25       |
# | /s       | espacio en blanco     | número\s\d\d | número 25    |
# | /D       | NO numérico           | \D\D\D\D     | ABCD         |
# | /W       | NO alfanumérico       | \W\W\W       | +-=          |
# | /S       | NO espacio en blanco  | \S\S\S       | 1234         |
####################################################################

# Carácteres cuantificadores
#################################################################################
# | caracter | descripcion                 | ejemplo       | ejemplo real       |
# | +        | 1 o mas veces               | código_\d-\d+ | código_5-5         |
# | {n}      | Se reptite n veces          | \d-\d{4}      | 1-0000             |
# | {n,m}    | Se repite de n a m veces    | w{3,5}        | yo526              |
# | {n,}     | Se repite de n hacia arriba | -\d{4,}-      | -111111-           |
# | *        | Se repite 0 o más veces     | \w\s*\w       | a 2, a   b, fm, s4 |
# | ?        | 1 ó 0                       | casas?        | casa, casas        |
#################################################################################

import re

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al dia al servicio de ayuda online'
patron = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())
busqueda_todas_apariciones = re.findall(patron,texto)
print(busqueda_todas_apariciones)

texto2 = 'Llama al 123-456-7899 ya mismo'
patron2 = r'\d\d\d-\d\d\d-\d\d\d\d'
resultado2 = re.search(patron2, texto2)
print(resultado2)
print(resultado2.group())

texto_cuantificadores = 'Llama a casa, el numero de telefono es 1234-566-9877'
patron_cuantificadores = r'\d{3}-\d{3}-\d{4}'
resultado_cuantificadores = re.search(patron_cuantificadores, texto_cuantificadores)
print(resultado_cuantificadores)

texto_cuantificadores_compile = 'Llama al 559-778-1224'
patron_cuantificadores_compile = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado_cuantificadores_compile = re.search(patron_cuantificadores_compile, texto_cuantificadores_compile)
print(resultado_cuantificadores_compile)
print(resultado_cuantificadores_compile.group())
print(resultado_cuantificadores_compile.group(1))
print(resultado_cuantificadores_compile.group(2))
print(resultado_cuantificadores_compile.group(3))

clave = input('Introduzca la clave que empiece por una letra y que tenga 8 caracteres: ')
patron_clave = r'\D{1}\w{7}'
chequear_clave = re.search(patron_clave, clave)
print(chequear_clave)

texto_busqueda = 'No atendemos los lunes por la tarde'
busqueda_texto = re.search('lunes|martes', texto_busqueda)
print(busqueda_texto)
