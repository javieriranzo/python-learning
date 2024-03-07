texto = "Este es el texto de Javier"; 

# Método para convertir String en mayúsculas
resultado_metodo_upper = texto.upper(); 
print(resultado_metodo_upper);

# Método para convertir String en minúsculas
resultado_metodo_lower = texto.lower(); 
print(resultado_metodo_lower);

# Método para separar String en elementos y guardarlos en una lista tomando como separador los espacios
resultado_metodo_split = texto.split(); 
resultado_metodo_split_separador = texto.split("t"); 
print(resultado_metodo_split);
print(resultado_metodo_split_separador);

# Método para unir Strings
resultado_parte_1 = "Aprender";
resultado_parte_2 = "Python";
resultado_parte_3 = "es";
resultado_parte_4 = "genial";
resultado_partes_unidas = " ".join([
    resultado_parte_1,
    resultado_parte_2,
    resultado_parte_3,
    resultado_parte_4
]);
print(resultado_partes_unidas);

# Método para buscar en un determinado carácter dentro del String. La diferencia entre el .index y el .find es que cuando el 
# método find intenta buscar una carácter que no existe en lugar de devolver un error, devuelve -1
resultado_metodo_find = texto.find("J");
print(resultado_metodo_find);
resultado_metodo_find_no_encontrado = texto.find("G");
print(resultado_metodo_find_no_encontrado);

# Método para reemplazar un String por otro
resultado_metodo_replace = texto.replace("Javier", "Natalia"); 
print(resultado_metodo_replace);
resultado_metodo_replace_caracter = texto.replace("e", "x");
print(resultado_metodo_replace_caracter);