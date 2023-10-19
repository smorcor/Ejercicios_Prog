"""
Escribe un algoritmo en pseudocódigo que lea un número y te diga si es par o impar.
El número no puede ser negativo ni mayor de 10, en tal caso solo mostrará un mensaje de error.
"""

"""
Inicio
    Escribe "Dime un número: "
    lee num
    Si (num > 0 and num < 10) entonces
        
        si (type(num / 2) is int)entonces
            Escribe num +"es par."
        
        si (type(num / 2) is not int)entonces
            Escribe num +"es impar."
    sino 
        lee error.


Fin

Inicio

    Escribe "Dime un número: "
    lee num

    Si (num > 0 and num < 10) entonces
        Escribe "error"
    sino
        si (num % 2 == 0) entonces
            escribe "Es par."
        sino
            escribe "Es impar."
            
Fin
"""