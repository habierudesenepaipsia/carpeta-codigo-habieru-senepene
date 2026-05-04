#Desarrolle un sistema que permita ingresar 10 números (sólo números positivos), al terminar de ingresar el décimo número positivo, desplegar cuántos números pares ingreso.
#DEBE SER COM CICLO FOR
ciclaje = 0
num = 0
x = 0
numpositivcheck = 0
numpositivcount = 0
contador = 0
indexfin = 10
index = 0
for ciclaje in range(0,indexfin):
    num = int(input(f"Ingrese el número positivo {ciclaje+1}:"))
    if num <= 0:
        ciclaje = ciclaje - 1
        print("Número inválido, reingrese")
        num = int(input(f"Ingrese el número positivo \n"))
        numpositivcheck = num % 2
        if numpositivcheck == 0:
            numpositivcount = numpositivcount + 1 
    else:
        numpositivcheck = num % 2
        if numpositivcheck == 0:
            numpositivcount = numpositivcount + 1    
print(f"Usted ha ingresado {numpositivcount} números positivos ")