# *args = argumentos. Se utiliza para definir funciones genéricas que tengas un número variable de argumentos

def suma (a,b):
    return a + b
print(suma(5,5))

def sumar_args(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(sumar_args(1,2,4,5,6,7,8,9,0,20))

def sumar_args_sum(*args):
    return sum(args)
print(sumar_args_sum(4,5,6,7,4,23,434,68,3,2,435,7,534,3))