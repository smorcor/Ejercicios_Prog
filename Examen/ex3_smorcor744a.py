"""
Escribe un programa en Python que lea una palabra y la encripte:

    1. Pedir la palabra hasta que cumpla que tiene un mínimo de 8 letras.
    
    2. Después, transformar o encriptar la palabra de la siguiente manera:
        - Sin bucles, pero escribiendo varias instrucciones si lo necesitáis.
        - Eliminar espacios.
        - Consonantes a mayúsculas
        - La vocal a pasa a ser una @.
        - La vocal e pasa a ser un 3.
        - La vocal i pasa a ser un 1.
        - El resto de vocales serán minúsculas.
        - Si tiene solo 8 letras, añade un * al principio y un # al final.

    3. Ejemplos:

    > cPedro PAblO    1984
    > Su palabra encriptada es P3DRoP@BLo1984

    > Introduzca una palabra: ArIADNa2
    > Su palabra encriptada es *@R1@DN@2#

    > Introduzca una palabra: USER       89
    > Introduzca una palabra *mínimo 8 letras*: USER  893465
    > Su palabra encriptada es uS3R893465

"""
"""palabra = str(input("Introduzca una palabra: "))
#Mientras palabra tenga menos de 8 caracteres 
while len(palabra) < 8 :
    palabra = str(input("Introduzca una palabra *mínimo 8 letras*: "))
#Cuando tenga 8 o mas
if len(palabra) >= 8 :
    #Quitamos los espacios y todo en mayusculas
    palabra.split(" ")
    palabra.upper()
    #Le damos valor a las vocales 
    vocal_a = palabra.find("A")
    vocal_e = palabra.find("E")
    vocal_i = palabra.find("I")
    vocal_o = palabra.find("O")
    vocal_u = palabra.find("U")
    #Remplazamos las vocales y las sustituimos
    palabra.replace(str(vocal_a), "@")
    palabra.replace(str(vocal_e), "3")
    palabra.replace(str(vocal_i), "1")
    palabra.replace(str(vocal_o), "o")
    palabra.replace(str(vocal_u), "u")

    #Cuando tenga 8 caracteres hacemos lo que nos dice
    if len(palabra) == 8 :
        print("Su palabra encriptada es "+"*" + palabra + "#")
    else:
        print(f"Su palabra encriptada es {palabra}")
"""
palabra = input("Introduzca una palabra: ").replace(" ", "")

while len(palabra) < 8 :
    palabra = str(input("Introduzca una palabra *mínimo 8 letras*: ")).replace(" ", "")

palabra = palabra.upper().replace("A", "@").replace("E", "3").replace("I", "1").replace("O", "o").replace("U", "u")

if len(palabra) == 8 :
    palabra = "*" + palabra + "#"

print(palabra)