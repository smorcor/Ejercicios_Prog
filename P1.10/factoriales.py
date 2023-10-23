def factorial(num: int):
    if num <= 1:
        return 1
    total = 1
    while (num > 1):
        total *= num
        num -= 1

    return total

def factorialStr(num: int):
    str_total = 1
    str_total = str_total*num
    while num > 1:
        
        print(f"{num} x", end=" ")
        num -= 1
        str_total = str_total*num
        str_total1 = str(str_total)
    while num == 1 :
        print(f"1 = {str_total}")
        num -= 1 


numero = int(input("Introduce un número: "))
print(f"{numero}! = " + str(factorial(numero)))
print(factorialStr(numero))