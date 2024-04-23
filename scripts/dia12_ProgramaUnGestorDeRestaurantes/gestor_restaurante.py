from tkinter import *

# Iniciar tkinter
aplicacion = Tk()

## PANTALLA PRINCIPAL ##

# Definir tamaño de la pantalla. Parámetro: Tamaño de pantalla + posicionEjeX + posicionEjeY
aplicacion.geometry('1020x630+0+0')
# Evitar maximizar pantalla. Parámetros: 0 y 0 para que nos e pueda ampliar ni en el eje de las X ni en el eje de las Y
aplicacion.resizable(0, 0)
# Establecer título de la pantalla
aplicacion.title('Sistema de facturación')
# Establecer color de fondo de pantalla
aplicacion.config(bg='burlywood')

## PANELES PRINCIPALES ## 

# Creación del paner superior. Situar panel en la parte superior de la pantalla. Definir y situar la etiqueta del título
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)
etiqueta_titulo = Label(panel_superior, text='Sistema de facturación', fg='black', font=('Dosis', '58'), bg='burlywood', width=27)
etiqueta_titulo.grid(row=0, column=0)

# Creación del panel izquierdo. Situar el panel izquiero en la pantalla
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)

# Creación del panel costos. Situar el panel costos dentro del panel izquierdo
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

# Creación del panel comidas. Situar el panel comidas dentro del panel izquierdo a la parte derecha
panel_comidas = LabelFrame(panel_izquierdo, text='Comidas:', font=('Dosis', '19', 'bold'), bd=1, relief=FLAT, fg='black')
panel_comidas.pack(side=LEFT)

# Creación del panel bebidas. Situar el panel bebidas dentro del panel izquierdo a la parte derecha
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas:', font=('Dosis', '19', 'bold'), bd=1, relief=FLAT, fg='black')
panel_bebidas.pack(side=LEFT)

# Creación del panel postres. Situar el panel postres dentro del panel izquierdo a la parte derecha
panel_postres = LabelFrame(panel_izquierdo, text='Postres:', font=('Dosis', '19', 'bold'), bd=1, relief=FLAT, fg='black')
panel_postres.pack(side=LEFT)

# Creación del paner derecho. Situar panel en la parte derecha de la pantalla.
panel_derecha = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

# Creación del panel calculadora. Situar panel calculadora dentro del panel derecho
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# Creación del panel recibo. Situar panel calculadora dentro del panel derecho
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# Creación del panel botones. Situar panel calculadora dentro del panel derecho
panel_botones = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# Listas de productos
lista_comidas = ['Pollo', 'Cordero', 'Pescado', 'Kebab', 'Sushi', 'Pizzas', 'Paellas', 'Cocidos']
lista_bebidas = ['Agua', 'Refrescos', 'Cervezas', 'Vino tinto', 'Vino blanco', 'Cócteles', 'Zumos', 'Combinados']
lista_postres = ['Tartas', 'Fruta', 'Bizcochos', 'Helados', 'Granizados', 'Sorbetes', 'Quesos', 'Almibar']

# Crear checkbuttons para cada producto de comida
productos_comida = []
cuadros_comida = []
cantidades_comida = []
contador = 0
for comida in lista_comidas: 
    # Crear checkbuttons
    productos_comida.append('')
    productos_comida[contador] = IntVar() # Clase de Tkinter que permite crear variuable específica
    check_comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', '19', 'bold'), onvalue=1, offvalue=0, variable=productos_comida[contador])
    check_comida.grid(row=contador, column=0, sticky=W)
    # Crear cuadros de entrada de texto
    cuadros_comida.append('')
    cantidades_comida.append('')
    cuadros_comida[contador] = Entry(panel_comidas, font=('Dosis', '18', 'bold'), bd=1, width=6, state=DISABLED, textvariable=cantidades_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1) 
    contador += 1

# Crear checkbuttons para cada producto bebida
productos_bebida = []
cuadros_bebida = []
cantidades_bebida = []
contador = 0
for bebida in lista_bebidas: 
    productos_bebida.append('')
    productos_bebida[contador] = IntVar() # Clase de Tkinter que permite crear variuable específica
    check_bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', '19', 'bold'), onvalue=1, offvalue=0, variable=productos_bebida[contador])
    check_bebida.grid(row=contador, column=0, sticky=W)
    cuadros_bebida.append('')
    cantidades_bebida.append('')
    cuadros_bebida[contador] = Entry(panel_bebidas, font=('Dosis', '18', 'bold'), bd=1, width=6, state=DISABLED, textvariable=cantidades_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1) 
    contador += 1
    
# Crear checkbuttons para cada producto postres
productos_postre = []
cuadros_postre = []
cantidades_postre = []
contador = 0
for postre in lista_postres: 
    productos_postre.append('')
    productos_postre[contador] = IntVar() # Clase de Tkinter que permite crear variuable específica
    check_postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', '19', 'bold'), onvalue=1, offvalue=0, variable=productos_postre[contador])
    check_postre.grid(row=contador, column=0, sticky=W)
    cuadros_postre.append('')
    cantidades_postre.append('')
    cuadros_postre[contador] = Entry(panel_postres, font=('Dosis', '18', 'bold'), bd=1, width=6, state=DISABLED, textvariable=cantidades_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1) 
    contador += 1


# Evitar que la pantalla se cierre
aplicacion.mainloop()