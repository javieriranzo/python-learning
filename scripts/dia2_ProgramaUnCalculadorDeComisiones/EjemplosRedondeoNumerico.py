cantidad_personas = 7; 
precio_compra = 90; 

print(precio_compra / cantidad_personas); 
print(round(precio_compra / cantidad_personas));
print(round(precio_compra / cantidad_personas, 2));

# En este caso se muestra que el tipo es float porque el redondeo se está haciendo en el momento de la impresión de la variable
valor_1 = 95.6; 
print(round(valor_1));
print(type(valor_1)); 

# En este caso se muestra que el tipo es integer porque el redondeo se está haciendo en el momento de la declaración de la variable
valor_2 = round(95.6); 
print(valor_2);
print(type(valor_2));