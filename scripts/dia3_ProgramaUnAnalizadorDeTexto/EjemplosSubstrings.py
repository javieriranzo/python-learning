texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento_texto_1 = texto[2]
fragmento_texto_2 = texto[2:5]    # Extrae desde el carácter 2 hasta el 5 pero sin incluirlo
fragmento_texto_3 = texto[2:]     # Extrae desde el carácter 2 hasta el final
fragmento_texto_4 = texto[:5]     # Extrae desde el principio hasta el carácter 5 pero sin incluirlo
fragmento_texto_5 = texto[0:10:1] # Extrae desde el carácter 0 hasta el 10 salteándolo de 1 en 1
fragmento_texto_6 = texto[2::2]   # Extrae desde el carácter 2 hasta el final salteándolo de 2 en 2
fragmento_texto_7 = texto[::3]    # Extrae desde el principio hasta el final salteándolo de 3 en 3
fragmento_texto_8 = texto[::-1]   # Extrae la cadena de texto al revés
print(fragmento_texto_1)
print(fragmento_texto_2)
print(fragmento_texto_3)
print(fragmento_texto_4)
print(fragmento_texto_5)
print(fragmento_texto_6)
print(fragmento_texto_7)
print(fragmento_texto_8)