class Animal: 
    
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print('El animal ha nacido')

# De esta manera se realiza la herencia
class Pajaro(Animal): 
    pass

# Imprimir la clase de la que hereda una clase
print(Pajaro.__bases__)
# Comprobar que clases heredan de una clase
print(Animal.__subclasses__())

mi_pajaro = Pajaro('2', 'azul')
print(mi_pajaro.edad)
print(mi_pajaro.color)
mi_pajaro.nacer()