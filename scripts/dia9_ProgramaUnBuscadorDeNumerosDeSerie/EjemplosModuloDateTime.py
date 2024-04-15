import datetime
from datetime import datetime
from datetime import date

# mi_hora = datetime.time(17, 7, 35)
# print(type(mi_hora))
# print(mi_hora)
# print(mi_hora.hour)
# print(mi_hora.minute)
# print(mi_hora.second)

# mi_dia = datetime.date(2024, 7, 27)
# print(mi_dia)
# print(mi_dia.year)
# print(mi_dia.day)
# print(mi_dia.month)
# print(mi_dia.ctime())
# print(mi_dia.today())

mi_hora2 = datetime(2024, 7, 27, 14, 20, 00)
print(mi_hora2)
mi_hora2 = mi_hora2.replace(month = 8)

fecha_nacimiento = date(1992, 7, 27)
fecha_casamiento = date(2027, 5, 25)
solteria = fecha_casamiento - fecha_nacimiento
print(solteria)
