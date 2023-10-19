"""
Corrige los errores para que el siguiente programa funcione correctamente cómo se explica a continuación...

Recorre la lista y dependiendo del tipo de dato de cada elemento muestra la siguiente información:
   1. int => "Tienes N años".

   2. float => "El producto vale N€, pero está en oferta por (N*0.85)€", donde el primer precio se muestra con 0 decimales y el segundo, que está en oferta al 85% de su precio original, con 2 decimales.

   3. str => "Te llamas N1 pero todos te conocen cómo N2." N1 será el nombre completo y N2 solo el primer nombre. N1 cambiará la a por una @ y tendrá las iniciales de cada nombre en mayúsculas y el resto en minúsculas. N2 tendrá todas las letras en mayúsculas.

   4. bool => Si es True dice la verdad, sino dice la mentira.

   El resultado de ejecutar este programa debe ser el siguiente:

   Tienes 43 años.
   Te llamas Pedro P@blo, pero todos te conocen cómo PEDRO.
   El producto vale 18€, pero está en oferta por 15.01€
   El producto vale 9€, pero está en oferta por 7.64€
   Te llamas M@rí@ Jesús, pero todos te conocen cómo MARÍA.
   Estás diciendo una mentira.
   Te llamas @n@ Esper@nz@, pero todos te conocen cómo ANA.
   Tienes 25 años.
   Estás diciendo la verdad.
   El producto vale 10€, pero está en oferta por 8.49€
"""
"""
miLista = [43, "pedro pablo", 17.66, 8.99, "maría jesús", True, "ANA esperanza", 25, False, 9.99]

cont = 1
if (cont <= len(miLista)):
    if type(miLista[0]) is int:
        edad = miLista[0]
        print("Tienes " + str(edad) + " años.")

    elif type(miLista[1]) is str:
        nombreCompleto = str(miLista[1])
        nombreCompleto.capitalize()
        nombreCompleto.replace("a","@")
        nombreCorto = str(miLista["pablo"])
        nombreCorto.upper()
        print("Te llamas", nombreCompleto, ", pero todos te conocen cómo", nombreCorto, ".")

    elif type(miLista[2]) is float:
        precio = float(miLista[2])
        precioOferta = precio - 2.65
        print("El producto vale {:.ef}€, pero está en oferta por {}€".format(precio, precioOferta))

    elif type(miLista[3]) is bool:
        verdad = bool(miLista[3])
        if type(miLista[3]) is True :
            print("Estás diciendo una mentira.")
        else:
            print("Estás diciendo la verdad.")
    cont -= 1
"""


miLista = [43, "pedro pablo", 17.66, 8.99, "maría jesús", True, "ANA esperanza", 25, False, 9.99]

cont = 0
if (cont < len(miLista)):
    if type(miLista[cont]) is int:
        edad = miLista[cont]
        print("Tienes " + str(edad) + " años.")

    elif type(miLista[cont]) is str:
        nombreCompleto = str(miLista[cont]).title().replace("a", "@").replace("A", "@")
        nombreCorto = str(miLista[cont]).upper().split(" ")
        print("Te llamas", nombreCompleto, ", pero todos te conocen cómo", nombreCorto, ".")

    elif type(miLista[cont]) is float:
        precio = float(miLista[cont])
        precioOferta = precio * 0.85
        print("El producto vale {:.0f}€, pero está en oferta por {:.2f}€".format(precio, precioOferta))

    elif type(miLista[cont]) is bool:
        verdad = bool(miLista[cont])

        if type(miLista[cont]) is True :
            print("Estás diciendo una mentira.")
        else:
            print("Estás diciendo la verdad.")
    cont += 1
