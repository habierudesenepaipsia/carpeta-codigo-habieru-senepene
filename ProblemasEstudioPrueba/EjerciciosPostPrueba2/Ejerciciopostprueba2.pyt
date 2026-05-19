#Desarrolle un programa que permita ingresar 20 números y despliegue por pantalla cuantos pares y cuantos números impares ingresó el usuario.

###############ESTRUCTURA#############


#paso0: definir las variables a ser ocupadas
#paso1: iniciar un ciclo que tenga número limite 20
#paso2: colocar un input que reciba un número por cada ciclo de los 20
#paso3: hacer un comparador entre cada número ciclado que guarde si el número es par o impar y que guarde cada variable par o impar
# en una variable distinta (contador)
#paso4: hacer un print que muestre al terminar el ciclo, la cantidad de números ingresados impares y pares
#paso5:
#paso6:







numimpares = 0
numpares = 0
numloopuno = 0

while numloopuno < 20:
    numveinuno = int(input("Ingrese veinte números:"))
    if numveinuno % 2 == 0:
        numpares = numpares + 1
    else:
        numimpares = numimpares + 1    

    numloopuno = numloopuno + 1

print(f"La cantidad de números pares son: {numpares}, y la cantidad de números impares son: {numimpares}.")    