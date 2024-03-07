mi_texto = "Esta es una prueba"; 
resultado = mi_texto[9];
resultado_desde_el_final = mi_texto[-4];
# El método index busca de izquierda a derecha
# Si se busca una letra inexistente, muestra un error
# Si se busca una palabra completa, muestra el índice donde empieza la palabra
# Si se busca una palabra inexistente, muestra un error
# Si se busca una letra repetida, muestra la primera posición donde aparece la letra
resultado_busca_letra = mi_texto.index("n");
resultado_busca_desde_indice = mi_texto.index("a", 5);
resultado_busca_intervalo_indices = mi_texto.index("a", 5, 11);
# El método rindex busca de derecha a izquierda
resultado_rindex = mi_texto.rindex("a");
print(resultado);
print(resultado_desde_el_final);
print(resultado_busca_letra);
print(resultado_busca_desde_indice);
print(resultado_busca_intervalo_indices);
print(resultado_rindex);