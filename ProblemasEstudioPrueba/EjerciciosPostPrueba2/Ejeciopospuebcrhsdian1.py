# Desarrolle una función que reciba 2 argumentos(desde y hasta) 
# y retorne la suma de todos los números impares que estén en ese rango

# def odd_addition(numberFrom: int, numberTo: int):
#     numberOddAddition = 0
#     while numberFrom <= numberTo:
#         if numberFrom % 2 == 1:
#             numberOddAddition = numberOddAddition + numberFrom
#         numberFrom = numberFrom + 1
#     return numberOddAddition

def odd_addition(numberFrom: int, numberTo: int):
    numberOddAddition = 0
    for numberFrom in range(numberFrom,numberTo+1,1):
        if numberFrom % 2 == 1:
            numberOddAddition = numberOddAddition + numberFrom
    return numberOddAddition



print("Este programa sumará todos los números impares del rango ingresado")
print("Ingrese los siguientes datos:\n")

numStart = int(input("Ingrese el número del principio del rango: "))
numEnd = int(input("Ingrese el número final del rango: "))

result = odd_addition(numStart, numEnd)

print(f"La suma de los números impares es: {result}")