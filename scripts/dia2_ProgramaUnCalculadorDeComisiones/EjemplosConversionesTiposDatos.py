# Conversiones implícitas
num1 = 20
num2 = 30.5 

print(num1)
print(type(num1))
print(num2)
print(type(num2))

num3 = num1 + num2 
print(num3)
print(type(num3)) 

# Conversiones explícitas
num4 = 5.8 
print(num4)
print(type(num4))

num5 = int(num4) 
print(num5)
print(type(num5))

edad = input("Dime tu edad: ") 
print(type(edad))
edad = int(edad) 
print(type(edad))
