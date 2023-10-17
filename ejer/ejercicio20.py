numero = input("Por favor, introduce un número de teléfono con formato +34-XXXXXXXXX-XX: ")

lista = numero.split('-')

if len(lista) == 3 and lista[0] == "+34" and len(lista[1]) == 9 and len(lista[2]) == 2:
    numero_sin_prefijo_extension = lista[1]
    print("Número de teléfono sin prefijo y extensión:", numero_sin_prefijo_extension)
else:
    print("El número de teléfono no tiene el formato correcto.")

