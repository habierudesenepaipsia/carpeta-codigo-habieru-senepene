#Crear un algoritmo en diagrama de flujo que al leer un número entero positivo (asuma que el número cumple las condiciones),
#imprimir PAR si el número es par e IMPAR si es impar
enteropos = int(input("Ingrese un número positivo:"))
if enteropos > 0:
        if enteropos % 2 == 0:
         print("su número ingresado es par")
        else:
              print("su número ingresado es impar") 
else:
        print("usted ha ingresado un valor negativo, reinténtelo")
        