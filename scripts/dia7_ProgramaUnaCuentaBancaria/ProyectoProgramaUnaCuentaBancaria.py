from os import system

class Persona: 
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona): 
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        
    def __str__(self): 
        return f'Nombre: {self.nombre} \n Apellido: {self.apellido} \n Número de cuenta: {self.numero_cuenta} \n Balance: {self.balance}'
    
    def depositar(self, cantidad): 
        self.balance += cantidad
        print(f'El depósito de {cantidad}€ ha sido realizado')
        
    def retirar(self, cantidad): 
        if self.balance >= cantidad:
            self.balance -= cantidad
            print(f'El retiro de {cantidad}€ ha sido realizado')
        else:
            print(f'No se puede realizar el retiro de {cantidad}€. Fondos insuficientes')
    
def crear_cliente(): 
    nombre = input('Introuduce el nombre del cliente: ')
    apellido = input('Introduce el apellido del cliente: ')
    numero_cuenta = input('Introduce el numero de cuenta del cliente: ')
    cliente_nuevo = Cliente(nombre, apellido, numero_cuenta)
    return cliente_nuevo

def mostrar_menu_inicio(): 
    print('##########################')
    print('BIENVENIDO AL BANCO PYTHON')
    print('##########################')
    eleccion_usuario = 'x'
    while not eleccion_usuario.isnumeric() or int(eleccion_usuario): 
        print('''
              [1] - Depositar dinero
              [2] - Retirar dinero 
              [3] - Salir del programa
              ''')
        eleccion_usuario = input('Elige una opción: ')
    return int(eleccion_usuario)

system('cls')
mi_cliente = crear_cliente()
print(mi_cliente)
opcion = 0

while opcion != 'S':
    print('Elije: Depositar (D), Retirar (R), o Salir (S)')
    opcion = input()

    if opcion == 'D':
        monto_dep = int(input("Monto a depositar: "))
        mi_cliente.depositar(monto_dep)
    elif opcion == 'R':
        monto_ret = int(input("Monto a retirar: "))
        mi_cliente.retirar(monto_ret)
    
    print(mi_cliente)
    print("Gracias por operar en Banco Python")
        
    