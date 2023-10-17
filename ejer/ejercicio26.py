productos = input("Escribe tu lista de la compra separada por comas: ")
partes = productos.split(",")
for productos in partes:
    print(productos.strip())