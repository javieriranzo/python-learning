nombre_empleado = input("Nombre y apellidos: ") 
ventas_realizadas = int(input("Ventas(€): ")) 
comision_obtenida = round(ventas_realizadas * 13/100, 2)

print(f"Hola {nombre_empleado}, has vendido por una cantidad de {ventas_realizadas}, tu comisión es de {comision_obtenida}€")