fecha = input("Por favor, introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")

partes = fecha.split("/")
dia, mes, año = partes
dia = int(dia)
mes = int(mes)
año = int(año)
print("Día:", dia)
print("Mes:", mes)
print("Año:", año)