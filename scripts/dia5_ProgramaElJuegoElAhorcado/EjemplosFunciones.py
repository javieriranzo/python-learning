precios_cafe = [('Capuchino', 1.5),('Americano', 2),('Mokka', 2.5)]

# Funcion para conocer el cafe mas caro
def cafe_mas_caro(lista_precios): 
    precio_mayor = 0
    cafe_mayor = ''
    for cafe, precio in lista_precios: 
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mayor = cafe
        else:
            pass
    return(cafe_mayor, precio_mayor)

cafe, precio = cafe_mas_caro(precios_cafe)
print(f'El cafe mas caro es {cafe} con un precio de {precio} €')