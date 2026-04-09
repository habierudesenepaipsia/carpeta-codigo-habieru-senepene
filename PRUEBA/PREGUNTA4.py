#D.	Desarrolle un programa que permita ingresar 3 números y desplegarlos de forma descendente (mayor a menor).
num1 = int(input("ingrese su primer número:"))
num2 = int(input("ingrese su segundo número:"))
num3 = int(input("ingrese su tercer número:"))
if num1 < num2:
    #Número 1 es menor que Número 2
    if num1 < num3:
        #Número 1 es menor que Número 2 y menor que Número 3
        numberlow1 = num1
        if num2 < num3:
            #Número 2 es mayor que Número 1 y menor que Número 3
            numberlow2 = num2
            numberlow3 = num3
        else:
            #Número 2 es mayor que Número 1 y mayor que Número 3
            numberlow2 = num3
            numberlow3 = num2
    else:
        #Número 1 es menor que Número 2 y mayor que Número 3
        numberlow1 = num3
        numberlow2 = num1
        numberlow3 = num2
else:
    #Número 2 es menor que Número 1
    if num2 < num3:
        #Número 2 es menor que Número 1 y menor que Número 3
        numberlow1 = num2
        if num1 < num3:
            #Número 1 es mayor que Número 2 y menor que Número 3
            numberlow2 = num1
            numberlow3 = num3
        else:
            #Número 1 es mayor que Número 2 y mayor que Número 3
            numberlow2 = num3
            numberlow3 = num1
    else:
        #Número 2 es menor que Número 1 y mayor que Número 3
        numberlow1 = num3
        numberlow2 = num2
        numberlow3 = num1

print(f"El orden de los números es el siguiente:{numberlow3},{numberlow2},{numberlow1}")
