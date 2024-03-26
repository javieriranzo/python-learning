def chequear_numero_tres_cifras(num):
    return num in range(100, 1000)

lista_auxiliar = []
def chequear_lista_numeros_tres_cifras(lista): 
    for n in lista:
        if n in range(100, 1000): 
            lista_auxiliar.append(n)
        else:
            pass
    return lista_auxiliar

resultado = chequear_numero_tres_cifras(100)
print(resultado)
resultado2 = chequear_lista_numeros_tres_cifras([55, 680, 1000])
print(resultado2)
