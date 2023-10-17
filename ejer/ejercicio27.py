producto = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario del producto: "))
numero = int(input("Introduce el número de unidades: "))

coste_total = precio * numero

cadena = "{}-Precio unitario: {:>9.2f}-Unidades: {:>3d}-Coste total: {:>11.2f}".format(producto, precio, numero, coste_total)

print(cadena)
