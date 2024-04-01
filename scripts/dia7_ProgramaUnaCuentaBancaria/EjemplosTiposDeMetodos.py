# Tipos de métodos
#   - Métodos de instancia: Métodos que se crean utilizando 'def' y el parámetro es obligatorio es 'self'
#       - Acceden y modifican atributos del objeto
#       - Pueden acceder a otros métodos
#       - Pueden modificar el estado de la clase
#   - Métodos de clase: Se escriben con la anotación @classmethod y como parámetro obligatorio reciben 'cls'
#       - No están asociados a las instancias de la clase si no a la clase en si misma
#       - Pueden ser llamados desde la instancia y desde la propia clase
#       - No pueden acceder a los atributos de la instancia pero si que pueden modificar los atributos de la clase
#    - Métodos estáticos: Se escriben con la anotación @staticmethod y no reciben parámetros obligatorios
#       - No pueden acceder a los atributos de la instancia
#       - No pueden modificar los atributos de la clase 
#       - Pueden acceder parámetros de entrada
#       - Los métodos estáticos van ligados a una clase concreta

class Pajaro:
    
    alas = True
    
    # Métodos de instancia
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    def piar(self):
        print('piopio')
        
    def volar(self, metros): 
        print(f'El pajaro ha volado {metros} metros')
        # Los métodos de instancia pueden acceder a otros métodos
        self.piar()
    
    def presentarse(self):
        print(f'Hola soy un {self.especie} y soy de color {self.color}')
        
    def cambiar_color(self): 
        # Los métodos acceder y modificar los atributos de los objetos
        self.color = 'rojo'
        
    # Métodos de clase
    @classmethod
    def poner_huevos(cls, cantidad_huevos): 
        print(f'El pájaro puso {cantidad_huevos} huevos')
        # Permite acceder a los atributos de clase
        cls.alas = False
        print(Pajaro.alas)
        
    # Métodos estáticos
    @staticmethod
    def mirar(): 
        print('El pájaro mira')
        
Pajaro.poner_huevos(4)
Pajaro.mirar()
        