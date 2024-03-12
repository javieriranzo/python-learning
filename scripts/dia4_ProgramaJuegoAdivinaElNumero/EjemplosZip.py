nombres = ['Javier', 'Natalia', 'Laura']
edades = ['31', '32', '33']
ciudades = ['Albalat', 'Vinaros', 'Bétera']
combinados = list(zip(nombres, edades, ciudades))
print(combinados)
for nombre, edad, ciudad in combinados:
    print(f"{nombre} vive en {ciudad} y tiene {edad} años")