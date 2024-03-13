# Match en Python es el equivalente al Switch en otros lenguajes
marca_coche = "Volvo"
match marca_coche: 
    case "Volvo":
        print("Tienes un Volvo")
    case "Volkswagen": 
        print("Tienes un Volkswagen")
    case _: 
        print("No sé qué coche tienes")
        
cliente = {
    'nombre': 'Javier Iranzo',
    'edad': 32, 
    'ocupacion': 'Ingeniero' 
}

vehiculo = {
    'marca': 'Ford Focus 1.0 ST Line', 
    'ficha_tecnica': {
        'caballos': 125,
        'color': 'plata'
    }
}

elementos = [cliente, vehiculo, 'dispositivo']

for e in elementos: 
    match e: 
        case {
            'nombre': nombre,
            'edad': edad,
            'ocupacion': ocupacion
        }:
            print(f"Es el cliente {nombre} tiene {edad} años y su puesto es {ocupacion}")
        case {
            'marca': marca,
            'ficha_tecnica': {
                'caballos': caballos,
                'color': color
            }
        }: 
            print(f"Es el vehículo {marca} con {caballos} caballos y de color {color}")
        case _: 
            print("No sé que es ... ")
        