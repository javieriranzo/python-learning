monedas = 5
while monedas > 0: 
    print(f"Tengo {monedas} monedas")
    monedas -= 1
    
respuesta = 's'
while respuesta == 's':
    respuesta = input('¿Quieres seguir? s/n: ')
else:
    print('Hasta luego')
    
nombre = input('Introduce tu nombre: ')
for letra in nombre:
    while letra != 'r':
        print(letra)
        break;
        
    