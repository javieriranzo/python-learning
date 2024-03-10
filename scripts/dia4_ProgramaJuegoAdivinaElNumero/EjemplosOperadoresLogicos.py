mi_bool_1 = (4 < 5) and (5 > 6) # Retorna false porque ambas comparaciones deben ser verdaderas al usar el and
mi_bool_2 = (55 =55) and ('perro' == 'perro') # Retorna true porque ambas comparaciones son verdaderas
mi_bool_3 = (3 == 4) or (5 == 5) # Retorna true porque una de las comparaciones es verdaderas
mi_bool_4 = (3 == 4) or (5 == 6) # Retorna false porque ninguna de las dos comparaciones son verdaderas

texto = "Esta frase es breve"
mi_bool_5 = ('frase' in texto) and ('breve' in texto) # true
mi_bool_6 = ('frase' in texto) and ('Javier' in texto) # false
mi_bool_7 = ('frase' in texto) or ('Javier' in texto) # true
mi_bool_8 = ('Javier' in texto) or ('Iranzo' int texto) # false

mi_bool_9 = not ('a' != 'a') # ¿a es diferente a a? 
 