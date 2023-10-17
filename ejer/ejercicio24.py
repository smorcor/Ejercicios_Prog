precio = input("Por favor, introduce el precio del producto en euros (con dos decimales): ")

try:
    preciof = float(precio)
except ValueError:
    print("La entrada no es un número válido.")
    exit()

euros = int(preciof)
centimos = int((preciof - euros) * 100)

print(f"El precio es de {euros} euros y {centimos} céntimos.")
