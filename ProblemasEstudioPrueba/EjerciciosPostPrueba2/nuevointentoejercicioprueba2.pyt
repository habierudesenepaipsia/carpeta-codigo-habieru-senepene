#Desarrolle un programa que permita ingresar 20 números y despliegue por pantalla cuantos pares y cuantos números impares ingresó el usuario.

###############ESTRUCTURA#############

#paso0: definir las variables a ser ocupadas
#paso1: iniciar un ciclo que tenga número limite 20
#paso2: colocar un input que reciba un número por cada ciclo de los 20
#paso3: hacer un comparador entre cada número ciclado que guarde si el número es par o impar y que guarde cada variable par o impar
# en una variable distinta (contador)
#paso3,5: asegurarse de poner un reiniciador de ciclo 
#paso4: hacer un print que muestre al terminar el ciclo, la cantidad de números ingresados impares y pares



numerospares = 0
numerosimpares = 0
numeroscontador = 0
contadorloop = 0
elpepevariablex = 0
variablenum = 0


while contadorloop < 20:
    variablenum = int(input("Ingrese el siguiente número del ciclo:"))
    if variablenum % 2 == 0:
        numerospares = numerospares + 1
    else:
        numerosimpares = numerosimpares + 1
    contadorloop = contadorloop + 1


print(f"En total de sus números ingresados, usted tiene {numerospares} números pares, y {numerosimpares} números impares en total")
