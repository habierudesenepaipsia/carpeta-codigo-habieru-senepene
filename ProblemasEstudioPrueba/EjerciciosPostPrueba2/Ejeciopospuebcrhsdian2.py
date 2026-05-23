# Desarrolle un programa que permita ingresar 20 números 
# y despliegue por pantalla cuantos pares y cuantos números impares ingresó el usuario.

numPairTotal = 0
numOddTotal = 0
index1 = 0
RangeEnd = 1
numEval = 0

print("Este programa evaluará la cantidad de números ingresados, y mostrará cuantos son números pares e impares.")
print("Ingrese los siguientes datos:\n")

# RangeEnd = int(input("Ingrese la cantidad de números que desea ingresar: "))
# index1 = 1
# while index1 <= RangeEnd:
#     numEval = int(input(f"Ingrese el valor del número {index1}°: "))
#     if numEval % 2 == 0:
#         numPairTotal = numPairTotal + 1
#     else:
#         numOddTotal = numOddTotal + 1
#     index1 = index1 + 1

RangeEnd = int(input("Ingrese la cantidad de números que desea ingresar: "))
for index1 in range(1,RangeEnd+1,1):
    numEval = int(input(f"Ingrese el valor del número {index1}°: "))
    if numEval % 2 == 0:
        numPairTotal = numPairTotal + 1
    else:
        numOddTotal = numOddTotal + 1

print(f"La cantidad de números pares es {numPairTotal} y la cantidad de números impares es {numOddTotal}")