var1 = True
var2 = False
print(type(var1))
print(var1)

numero = 5 > 2+3
print(type(numero))
print(numero)

numero2 = 5 == 2+3
print(type(numero2))
print(numero2)

numero3 = 5 != 2+3
print(type(numero3))
print(numero3)

numero4 = 5 >= 2+3
print(type(numero4))
print(numero4)

numero5 = 5 <= 2+3
print(type(numero5))
print(numero5)

# Los booleanos también se pueden declarar de la siguiente manera
numero6 = bool(5 <= 2+3)
print(type(numero6))
print(numero6)

# Para generar un valor falso 
numero7 = bool()
print(type(numero7))
print(numero7)

# Comprobar valores en una coleccion
mi_lista = [1, 2, 3, 4]
control_1 = 5 in mi_lista
print(type(control_1))
print(control_1)
control_2 = 5 not in mi_lista
print(type(control_2))
print(control_2)