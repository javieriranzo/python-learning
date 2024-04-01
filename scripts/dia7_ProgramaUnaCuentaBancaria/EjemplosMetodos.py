class Pajaro:
    
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    def piar(self):
        print('piopio')
        
    def volar(self, metros): 
        print(f'El pajaro ha volado {metros} metros')
    
    def presentarse(self):
        print(f'Hola soy un {self.especie} y soy de color {self.color}')
        
mi_pajaro = Pajaro('rojo', 'tucan')
mi_pajaro.piar();
mi_pajaro.volar(4)
mi_pajaro.presentarse()