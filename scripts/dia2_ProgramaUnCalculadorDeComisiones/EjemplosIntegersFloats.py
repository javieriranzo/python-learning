miNumero = 1 
print(miNumero)
print(type(miNumero))

miNumero2 = 1 + 1 
print(miNumero + miNumero) 

miNumero3 = 4.9
miNumero4 = miNumero2 + miNumero3 
print(miNumero4) 
print(type(miNumero4))

edad = input("Dime tu edad: ") 
print("Tu edad es: ")
# Esto está fallando porque cualquier valor que se introduce por el input es tartado como un String
nueva_edad = edad + 1 
print("Vas a cumplir " + nueva_edad)