from collections import Counter
from collections import defaultdict
from collections import namedtuple

# counter --> se utiliza para ver cuantas veces se repiten los elementos de una lista, strings ... 

# Contar cuantas veces se repite un numero en una lista
numeros = [1,2,2,3,4,5,5,5,5,5,6,2,2,4,56,7,87,5,3,23,54,6,7]
print(Counter(numeros))

# Contar cuantas veces se repite una letra en una palabra
palabra = 'esternocleidomastoideo'
print(Counter(palabra))

# Contar cuantas veces se repite una palabra en una frase (Se utiliza el método split para que almacene los elementos separados por espacio en blanco)
frase = 'Al pan pan y al vino vino'
print(Counter(frase.split(" ")))

# Método most_comon() se utiliza para ver el elemento más frecuente en una lista,  string ... Si no se indica nada por parámetro devuelve una tupla ordenada
# con la cantidad de veces que aparece. Por parámetro recibe la posición del elemento que más se repite por ejemplo si en la lista se repite el que más el número
# 9, si se le pasa como parámetro 1 devolverá el 9,X siendo X la cantidad de veces que se repite
serie = Counter([1,2,3,4,5,6,7,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,1,1,1,1,1,1,1,1,1,1,2,2,2,2])
print(serie.most_common())
print(serie.most_common(1))
print(list(serie))

# defaultdict --> proporciona un valor predeterminado para las claves que no están presentes en el diccionario. 

mi_dic = {'uno':'verde', 'dos':'azul', 'tres':'rojo'}
print(mi_dic['dos'])
# print(mi_dic['cuatro']) --> Esto devolvería error

mi_dic2 = defaultdict(lambda: 'nada')
mi_dic2['uno'] = 'verde'
print(mi_dic2['uno'])
print(mi_dic2['dos'])
print(mi_dic2)

# namedtuple  útil cuando necesitas una clase simple con atributos, pero no necesitas métodos adicionales, y quieres escribir menos código. Es especialmente útil cuando necesitas 
# una forma rápida de definir tipos de datos simples y estructurados.

mi_tupla = (500, 14, 65)
print(mi_tupla[1])

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
javier = Persona('Javier', '180', '90')
print(f'NOMBRE: {javier.nombre} - ALTURA: {javier.altura} - PESO: {javier.peso}')
print(f'NOMBRE: {javier[0]} - ALTURA: {javier[1]} - PESO: {javier[2]}')

