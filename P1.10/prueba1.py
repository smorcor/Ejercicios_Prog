def mayor(n1,n2) :
    if n1<n2 :
        print(n2)
    elif n2<n1 :
        print(n1)
    else:
        print(0)
num1 = input("Escribe un número: ")

num2 = input("Escribe otro número: ")
print(mayor(num1,num2))
