def precio():
    precio = impsiniva + (impsiniva *(tipoiva /100))
    print(f"El precio final del articulo es  {precio},")
impsiniva = float(input("Importe sin IVA: "))

tipoiva = float(input("Tipo de IVA: "))

precio()