#Desarrolle un programa que permita ingresar un número, si es negativo debemos enviar un mensaje al usuario “Número inválido, reingrese”
#y debe volver a ingresar otro número, si es positivo enviamos un mensaje “Número correcto” y termina el programa.
num1 = int(input("Ingrese su número:"))
if num1 < 0:
    #el número es incorrecto y debe volver a ingresar un valor
    print("Número inválido, reingrese.")
    num2 = int(input("Ingrese su número:"))
    if num2 < 0:
        #es incorrecto y finiquita el programa
        print(":/")
    else:
        print("Número correcto")    

else:
    #funciona el número y es correcto(?)
    print("Número correcto")     