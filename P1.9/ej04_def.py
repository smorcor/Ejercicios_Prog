def cel():
    fahren = float(input("Temperatura en farenheit: "))
    celcius = ((fahren -32 ) / (9/5))
    return f"Su temperatura es de {celcius}  grados Celsius"



print(cel())