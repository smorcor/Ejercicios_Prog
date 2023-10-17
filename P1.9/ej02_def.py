def mult(horas, coste):
    return f"Importe total: {horas*coste}"


horas = int(input("Horas de trabajo: "))
coste = float(input("Coste por hora: "))


print(mult(horas, coste))