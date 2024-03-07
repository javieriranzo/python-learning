# Concatenación de Strings
n1 = "Jav"; 
n2 = "ier"; 
print(n1+n2); 

# Multiplicación de strings
n3 = "Javier"; 
print(n3*10);

# String usando saltos de línea sin usar \n"
poema = """ Con diez cañones por banda viento en popa
a toda vela no surca el mal si no vuela
un velero bergantín
"""
print(poema);

# Comprobar si hay una palabra dentro de un String
print("velero" in poema);
print("cielo" in poema);
print("velero" not in poema);
print("cielo" not in poema); 

# Comprobar largo de un String
print(len(poema));