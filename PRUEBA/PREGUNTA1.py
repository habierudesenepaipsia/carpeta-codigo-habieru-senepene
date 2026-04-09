#Realizar un programa que solicite ingresar 3 valores enteros y luego muéstrelos siempre negativos.
num1 = int(input("ingrese su primer número:"))
num2 = int(input("ingrese su segundo número:"))
num3 = int(input("ingrese su tercer número:"))
if num1 < 0:
    numlist1 = num1
    print(f"su primer número es;{numlist1}")
    if num2 < 0:
        numlist2 = num2
        print(f"su segundo número es;{numlist2}")
        if num3 < 0:
            numlist3 = num3
            print(f"su tercer número es;{numlist3}")
        else:
            numlist3 = -num3
            print(f"su tercer número es;{numlist3}")    
    else:
        numlist2 = -num2
        print(f"su segundo número es;{numlist2}")
        if num3 < 0:
            numlist3 = num3
            print(f"su tercer número es;{numlist3}")
        else:
            numlist3 = -num3
            print(f"su tercer número es;{numlist3}") 
else:
    numlist1 = -num1
    print(f"su primer número es;{numlist1}")
    if num2 < 0:
        numlist2 = num2
        print(f"su segundo número es;{numlist2}")
        if num3 < 0:
            numlist3 = num3
            print(f"su tercer número es;{numlist3}")
        else:
            numlist3 = -num3
            print(f"su tercer número es;{numlist3}")     
    else:
        numlist2 = -num2
        print(f"su segundo número es;{numlist2}")
        if num3 < 0:
            numlist3 = num3
            print(f"su tercer número es;{numlist3}")
        else:
            numlist3 = -num3
            print(f"su tercer número es;{numlist3}")     
#profe no me mate            