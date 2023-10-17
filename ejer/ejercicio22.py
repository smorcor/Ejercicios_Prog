frase = input("Escribe una frase: ")
vocal = input("Escribe una vocal: ")
vocal = vocal.lower()
frasem = frase.replace(vocal, vocal.upper())
print("Frase con la vocal en mayúscula:", frasem)

