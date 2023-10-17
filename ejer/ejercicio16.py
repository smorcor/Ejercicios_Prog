barrasVnodia = int(input("Barras de pan vendidas que son del día: "))
barradia = 3.49
print(f"Precio barra del día: {barradia}€")
barranodia = barradia * (1 - 0.6)
print(f"Barras que no son del día: {barranodia}€")
final = barrasVnodia * barranodia
print(f"Coste final total de todas las barras no frescas es de {final}€")