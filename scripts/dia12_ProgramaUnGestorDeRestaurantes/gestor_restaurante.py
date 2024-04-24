from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

# Iniciar tkinter
aplicacion = Tk()

operador = ''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postre = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)
    
def borrar_visor_calculadora():
    global operador 
    operador = ''
    visor_calculadora.delete(0, END)
    
def obtener_resultado(): 
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''
    
def revisar_check():
    contador_comida = 0
    for comida in cuadros_comida: 
        if productos_comida[contador_comida].get() == 1:
            cuadros_comida[contador_comida].config(state=NORMAL)
            if cuadros_comida[contador_comida].get() == 0:
                cuadros_comida[contador_comida].delete(0, END)
            cuadros_comida[contador_comida].focus()
        else:
            cuadros_comida[contador_comida].config(state=DISABLED)
            cantidades_comida[contador_comida].set('0')
        contador_comida += 1
        
    contador_bebida = 0
    for bebida in cuadros_bebida: 
        if productos_bebida[contador_bebida].get() == 1:
            cuadros_bebida[contador_bebida].config(state=NORMAL)
            if cuadros_bebida[contador_bebida].get() == 0:
                cuadros_bebida[contador_bebida].delete(0, END)
            cuadros_bebida[contador_bebida].focus()
        else:
            cuadros_bebida[contador_bebida].config(state=DISABLED)
            cantidades_bebida[contador_bebida].set('0')
        contador_bebida += 1
    
    contador_postre = 0
    for postre in cuadros_postre: 
        if productos_postre[contador_postre].get() == 1:
            cuadros_postre[contador_postre].config(state=NORMAL)
            if cuadros_postre[contador_postre].get() == 0:
                cuadros_postre[contador_postre].delete(0, END)
            cuadros_postre[contador_postre].focus()
        else:
            cuadros_postre[contador_postre].config(state=DISABLED)
            cantidades_postre[contador_postre].set('0')
        contador_postre += 1
        
def calcular_total():
    subtotal_comida = 0
    precio = 0
    for cantidad_comida in cantidades_comida:
        subtotal_comida = subtotal_comida + (float(cantidad_comida.get()) * precios_comida[precio])
        precio += 1
    print(f'Subtotal comida: {subtotal_comida}')
    
    subtotal_bebida = 0
    precio = 0
    for cantidad_bebida in cantidades_bebida:
        subtotal_bebida = subtotal_bebida + (float(cantidad_bebida.get()) * precios_bebida[precio])
        precio += 1
    print(f'Subtotal bebida: {subtotal_bebida}')
    
    subtotal_postre = 0
    precio = 0
    for cantidad_postre in cantidades_postre:
        subtotal_postre = subtotal_postre + (float(cantidad_postre.get()) * precios_postre[precio])
        precio += 1
    print(f'Subtotal postre: {subtotal_postre}')
    
    sub_total = subtotal_comida + subtotal_bebida + subtotal_postre
    print(f'Subtotal sin impuestos: {sub_total}')
    impuesto = sub_total * 0.21
    total  = sub_total + impuesto
    print(f'Total: {total}')   
    
    var_costo_comida.set(f'€ {round(subtotal_comida, 2)}')
    var_costo_bebida.set(f'€ {round(subtotal_bebida, 2)}')
    var_costo_postre.set(f'€ {round(subtotal_postre, 2)}')
    var_subtotal.set(f'€ {round(sub_total, 2)}')
    var_impuesto.set(f'€ {round(impuesto, 2)}')
    var_total.set(f'€ {round(total, 2)}')
    
def generar_recibo(): 
    texto_recibo.delete(1.0, END)
    numero_recibo = f'Nº - {random.randint(1000, 9999)}'
    fecha_recibo = f'{datetime.datetime.now().day}/{datetime.datetime.now().month}/{datetime.datetime.now().year} - {datetime.datetime.now().hour}:{datetime.datetime.now().minute}\n'
    texto_recibo.insert(END, f'DATOS:\t{numero_recibo}\t\t{fecha_recibo}')
    texto_recibo.insert(END, f'*'*63+ '\n')
    texto_recibo.insert(END, 'Prod.\t\tCant.\tPrecio\n')
    texto_recibo.insert(END, f'-'*75 + '\n')
    
    posicion_comida = 0
    for comida in cantidades_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[posicion_comida]}\t\t{comida.get()}\t€{int(comida.get()) * precios_comida[posicion_comida]}\n')
        posicion_comida += 1
    posicion_bebida = 0
    for bebida in cantidades_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[posicion_bebida]}\t\t{bebida.get()}\t€{int(bebida.get()) * precios_bebida[posicion_bebida]}\n')
        posicion_bebida += 1
    posicion_postre = 0
    for postre in cantidades_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[posicion_postre]}\t\t{postre.get()}\t€{int(postre.get()) * precios_postre[posicion_postre]}\n')
        posicion_postre += 1
    
    texto_recibo.insert(END, f'-'*75 + '\n')
    texto_recibo.insert(END, f'Precio comida: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Precio bebida: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Precio postre: \t\t\t{var_costo_postre.get()}\n')
    texto_recibo.insert(END, f'-'*75 + '\n')
    texto_recibo.insert(END, f'Subtotal: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'IVA (21%): \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'TOTAL: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*'*63+ '\n')
    texto_recibo.insert(END, '¡Esperamos su visita de nuevo!')
    
def guardar_recibo():
    info_recibo = texto_recibo.get(1.0, END)
    recibo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    recibo.write(info_recibo)
    recibo.close()
    messagebox.showinfo('¡Atención!', 'Su recibo ha sido guardado')
    
def resetear_pantalla(): 
    texto_recibo.delete(0.1, END)
    for cantidad in cantidades_comida:
        cantidad.set('0')
    for cantidad in cantidades_bebida:
        cantidad.set('0')
    for cantidad in cantidades_postre:
        cantidad.set('0')  
    
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postre:
        cuadro.config(state=DISABLED)
        
    for producto in productos_comida:
        producto.set(0)
    for producto in productos_bebida:
        producto.set(0)
    for producto in productos_postre:
        producto.set(0)
    
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')

## PANTALLA PRINCIPAL ##

# Definir tamaño de la pantalla. Parámetro: Tamaño de pantalla + posicionEjeX + posicionEjeY
aplicacion.geometry('1210x630+0+0')
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
panel_costos = Frame(panel_izquierdo, bd=1, bg='azure4', relief=FLAT, padx=50)
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
    check_comida = Checkbutton(panel_comidas, text=comida.title(), font=('Dosis', '19', 'bold'), onvalue=1, offvalue=0, variable=productos_comida[contador], command=revisar_check)
    check_comida.grid(row=contador, column=0, sticky=W)
    # Crear cuadros de entrada de texto
    cuadros_comida.append('')
    cantidades_comida.append('')
    # Establecer valores por defecto a 0
    cantidades_comida[contador] = StringVar()
    cantidades_comida[contador].set(0)
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
    check_bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=('Dosis', '19', 'bold'), onvalue=1, offvalue=0, variable=productos_bebida[contador], command=revisar_check)
    check_bebida.grid(row=contador, column=0, sticky=W)
    cuadros_bebida.append('')
    cantidades_bebida.append('')
    # Establecer valores por defecto a 0
    cantidades_bebida[contador] = StringVar()
    cantidades_bebida[contador].set(0)
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
    check_postre = Checkbutton(panel_postres, text=postre.title(), font=('Dosis', '19', 'bold'), onvalue=1, offvalue=0, variable=productos_postre[contador], command=revisar_check)
    check_postre.grid(row=contador, column=0, sticky=W)
    cuadros_postre.append('')
    cantidades_postre.append('')
    # Establecer valores por defecto a 0
    cantidades_postre[contador] = StringVar()
    cantidades_postre[contador].set(0)
    cuadros_postre[contador] = Entry(panel_postres, font=('Dosis', '18', 'bold'), bd=1, width=6, state=DISABLED, textvariable=cantidades_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1) 
    contador += 1


var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# Panel costo comida
etiqueta_costo_comida = Label(panel_costos, text='Comida', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_comida.grid(row=0, column=0)
texto_costo_comida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# Panel costo bebida
etiqueta_costo_bebida = Label(panel_costos, text='Bebida', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_bebida.grid(row=1, column=0)
texto_costo_bebida = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1, padx=41)

# Panel costo postre
etiqueta_costo_postre = Label(panel_costos, text='Postres', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_costo_postre.grid(row=2, column=0)
texto_costo_postre = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_costo_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

# Panel subtotal
etiqueta_subtotal = Label(panel_costos, text='Subtotal', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_subtotal.grid(row=0, column=2)
texto_subtotal = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# Panel impuestos
etiqueta_impuesto = Label(panel_costos, text='Impuestos', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_impuesto.grid(row=1, column=2)
texto_impuesto = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3, padx=41)

# Panel total
etiqueta_total = Label(panel_costos, text='Total', font=('Dosis', 12, 'bold'), bg='azure4', fg='white')
etiqueta_total.grid(row=2, column=2)
texto_total = Entry(panel_costos, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# Botones
botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []
botones_creados = []
columnas = 0
for boton in botones: 
    boton = Button(panel_botones, text=boton.title(), font=('Dosiis', 14, 'bold'), fg='white', bg='azure4', bd=1, width=9)
    boton.grid(row=0, column=columnas)
    columnas += 1
    botones_creados.append(boton)

botones_creados[0].config(command=calcular_total)
botones_creados[1].config(command=generar_recibo)
botones_creados[2].config(command=guardar_recibo)
botones_creados[3].config(command=resetear_pantalla)
    
# Area de recibo
texto_recibo = Text(panel_recibo, font=('Dosis', 12, 'bold'), bd=1, width=42, height=10)
texto_recibo.grid(row=0, column=0)

# Area calculadora 
visor_calculadora = Entry(panel_calculadora, font=('Dosis', 16, 'bold'), width=32, bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

# Botones calculadora
botones_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', '=', 'AC', '0', '/']
botones_guardados = []
fila = 1
columna = 0
for boton in botones_calculadora: 
    boton = Button(panel_calculadora, text=boton.title(), font=('Dosis', 16, 'bold'), fg='white', bg='azure4', bd=1, width=8)
    boton.grid(row=fila, column=columna)
    botones_guardados.append(boton)
    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0
        
botones_guardados[0].config(command=lambda : click_boton('7'))
botones_guardados[1].config(command=lambda : click_boton('8'))
botones_guardados[2].config(command=lambda : click_boton('9'))
botones_guardados[3].config(command=lambda : click_boton('+'))
botones_guardados[4].config(command=lambda : click_boton('4'))
botones_guardados[5].config(command=lambda : click_boton('5'))
botones_guardados[6].config(command=lambda : click_boton('6'))
botones_guardados[7].config(command=lambda : click_boton('-'))
botones_guardados[8].config(command=lambda : click_boton('1'))
botones_guardados[9].config(command=lambda : click_boton('2'))
botones_guardados[10].config(command=lambda : click_boton('3'))
botones_guardados[10].config(command=obtener_resultado)
botones_guardados[10].config(command=borrar_visor_calculadora)
botones_guardados[11].config(command=lambda : click_boton('*'))
botones_guardados[14].config(command=lambda : click_boton('0'))
botones_guardados[15].config(command=lambda : click_boton('/'))



# Evitar que la pantalla se cierre
aplicacion.mainloop()