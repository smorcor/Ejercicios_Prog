
impsiniva = float(input("Importe sin IVA: "))

tipoiva = float(input("Tipo de IVA: "))

precio = impsiniva + (impsiniva *(tipoiva /100))

print("El precio final del articulo es ", precio,)
