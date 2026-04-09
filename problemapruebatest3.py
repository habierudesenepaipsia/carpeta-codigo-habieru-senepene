#Desarrolle un programa que permita ingresar 3 números al usuario, y los despligue en orden del número menor al mayor
# Declaración de variables
number1 = 0        #int
number2 = 0        #int
number3 = 0        #int
numberlowest1 = 0  #int
numberlowest2 = 0  #int
numberlowest3 = 0  #int

print("Ingrese sus datos")
number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))
number3 = int(input("Ingrese el tercer número: "))

if number1 < number2:
    #Número 1 es menor que Número 2
    if number1 < number3:
        #Número 1 es menor que Número 2 y menor que Número 3
        numberlowest1 = number1
        if number2 < number3:
            #Número 2 es mayor que Número 1 y menor que Número 3
            numberlowest2 = number2
            numberlowest3 = number3
        else:
            #Número 2 es mayor que Número 1 y mayor que Número 3
            numberlowest2 = number3
            numberlowest3 = number2
    else:
        #Número 1 es menor que Número 2 y mayor que Número 3
        numberlowest1 = number3
        numberlowest2 = number1
        numberlowest3 = number2
else:
    #Número 2 es menor que Número 1
    if number2 < number3:
        #Número 2 es menor que Número 1 y menor que Número 3
        numberlowest1 = number2
        if number1 < number3:
            #Número 1 es mayor que Número 2 y menor que Número 3
            numberlowest2 = number1
            numberlowest3 = number3
        else:
            #Número 1 es mayor que Número 2 y mayor que Número 3
            numberlowest2 = number3
            numberlowest3 = number1
    else:
        #Número 2 es menor que Número 1 y mayor que Número 3
        numberlowest1 = number3
        numberlowest2 = number2
        numberlowest3 = number1

print(f"El orden de los números es el siguiente:{numberlowest1},{numberlowest2},{numberlowest3}")

num1 = int(input("Ingrese el primer numero :"))
num2 = int(input("Ingrese el primer numero :"))
num3 = int(input("Ingrese el primer numero :"))

if num1 > num2:
    print("el numero en orden es ", num1, num2, num3)
else:
    if num1 > num3:
        print("el orden de mayor a menor es ", num1, num3, num2)
    else:
        if num2 > num1:
            print("el orden de mayor a menor es: ", num2, num1, num3)
        else:
            if num2 > num3:
                print("el orden es ", num2, num3, num1)
            else:
                if num3 > num1:
                    print("el orden es ", num3, num1, num2)
                else:
                    print("el orden es ", num3, num2, num1)
        