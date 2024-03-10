# Los tuples son similares a las listas, pero son inmutables (no se pueden modificar). 
# Ocupan menos memoria que las listas
# Se utilizan para estructuras que no van a querer ser modificadas.
mi_tuple1 = (
    1, 2, 3, 4, 5
); 

print(mi_tuple1);

# Pueden contener valores de distintos tipos
mi_tuple2 = (
    1, 'Hola', 45.6
);
print(mi_tuple2);

# Leer elemento de un tuple
print(mi_tuple1[2]); 
print(mi_tuple2[-1]);

# Asignar contenido de un tuple a distintas variables
# Tiene que haber la misma cantidad de elementos dentro del tuple que de variables
# También se pueden utilizar con las listas y con los diccionarios
# Se asignará los elementos a las variables por orden 
mi_tuple3 = (
    1, 2, 3
);
x, y, z = mi_tuple3; 
print(x); # Imprime 1
print(y); # Imprime 2
print(z); # Imprime 3

# Conocer el largo de un tuple
mi_tuple4 = (
    1, 2, 3, 4
);
print(len(mi_tuple4));

# Método count: Pide un valor como parámetro y lo que hace es permitir contar la cantidad de apariciones de un valor dentro del tuple
# También se pueden utilizar con las listas y con los diccionarios
mi_tuple5 = (
    1, 2, 3, 4, 5, 27, 27
); 
print(mi_tuple5.count(27)); 

# Método index: Indica la posición en la que se encuentra el valor pasado por parámetro dentro del tuple
# También se pueden utilizar con las listas y con los diccionarios
mi_tuple6 = (
    'Hola', 'me', 'llamo', 'Javier'
)
print(mi_tuple6.index('Javier'));