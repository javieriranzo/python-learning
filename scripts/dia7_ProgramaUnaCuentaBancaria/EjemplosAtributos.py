class Pajaro: 
    
    # Atributos de clase
    alas = True
    
    #Constructor de la clase (Atributos de instancia)
    def __init__ (self, color, especie):
        self.color = color
        self.especie = especie

mi_pajaro = Pajaro('verde', 'tucán')
mi_pajaro2 = Pajaro('negro', 'avestruz')

print(mi_pajaro.color)
print(mi_pajaro.especie)
print(f'Mi pajaro es un {mi_pajaro.especie} y su color es {mi_pajaro.color}')
print(mi_pajaro2.color)
print(mi_pajaro2.especie)
print(f'Mi pajaro es un {mi_pajaro2.especie} y su color es {mi_pajaro2.color}')

print(Pajaro.alas)
print(mi_pajaro.alas)
print(mi_pajaro2.alas)