class Animal: 
    
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    
    def nacer(self):
        print('El animal ha nacido')
    
    def hablar(self):
        print('Este animal emite un sonido')

# De esta manera se realiza la herencia
class Pajaro(Animal): 
    
    # Primera manera de añadir atributos a una clase heredera
    def __init__(self, edad, color, altura_vuelo):
        self.edad = edad
        self.color = color
        self.altura_vuelo = altura_vuelo
        
    # Segunda manera de añadir atributos a una clase heredera
    # def __init__(self, edad, color, altura_vuelo):
    #   super()
    #   self.altura_vuelo = altura_vuelo
    
    def hablar(self):
        print('pio')
    
    def volar(self, cantidad_metros):
        print(f'El pajaro vuela {cantidad_metros} metros')

mi_pajaro = Pajaro(3, 'amarillo', 40)
mi_pajaro.nacer()
# Métodos sobreescritos
mi_pajaro.hablar()
# Métodos propios de la clase
mi_pajaro.volar(100)
mi_animal = Animal(5, 'naranja')
print(mi_animal)

# Herencia múltiple

class Padre:
    def hablar(self):
        print('Hola')

class Madre:
    def reir(self):
        print('JAJA')
    def hablar(self):
        print('¿Qué tal?')

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_hijo = Hijo()
mi_hijo.hablar() # Devolverá 'Hola' porque hereda primero de la clase 'Padre'

mi_nieto = Nieto()
mi_nieto.hablar # Devolverá 'Hola' porque hereda de la clase hijo que hereda primero de la clase 'Padre'

# Ver el orden en el que heredan las clases
print(Nieto.__mro__)



