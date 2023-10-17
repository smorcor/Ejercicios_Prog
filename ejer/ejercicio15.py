dinero = float(input("Introduce el dinero que quieras depositar: "))
año1 = dinero * (1 + 0.04)
año2 = año1 * (1 + 0.04)
año3 = año2 * (1 + 0.04)

print("Tu capital en el primer año es de {:.2f}€".format(año1))
print("Tu capital en el segundo año es de {:.2f}€".format(año2))
print("Tu capital en el tercer año es de {:.2f}€".format(año3))