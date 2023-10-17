
peso = float(input("Introduce tu peso(Kg):"))
estatura = float(input("Introduce tu estatura(cm):"))

indice = peso / (estatura**2)

print(f'Tu indice de mas corporal es {round(indice, 2)}')

