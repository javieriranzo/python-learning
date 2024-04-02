class Cd: 
    
    def __init__(self, autor, titulo, cantidad_canciones):
        self.autor = autor
        self.titulo = titulo
        self.cantidad_canciones = cantidad_canciones
        
    def __str__(self):
        return f'Album {self.titulo} de {self.autor} con {self.cantidad_canciones} canciones'
    
    def __len__(self):
        return self.cantidad_canciones
    
    def __del__(self):
        print('Objeto eliminado')
        
mi_cd = Cd('Pynk Floyd', 'The Wall', 24)
print(mi_cd)
print(len(mi_cd))

# Borrar instancia de objeto
del mi_cd