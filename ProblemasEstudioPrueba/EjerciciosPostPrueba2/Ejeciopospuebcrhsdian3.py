# Desarrolle una función que reciba un número como argumento, 
# y retorne el siguiente número primo que encuentre después del número recibido como parámetro.

def nextPrime(numEval: int):
    index1 = numEval
    numShown = 0
    numDiv = 0
    while numEval != numShown:
        index2 = 1
        while index2 <= index1:
            if index1 % index2 == 0:
                numDiv = numDiv + 1
            index2 = index2 + 1

        if numEval < index1 and numDiv == 2:
            numShown = index1
            return numShown

        numDiv = 0
        index1 = index1 + 1
    

print("Este programa evaluará el número ingresado y entregará el siguiente número primo con respecto a este.\n")

num = int(input("Ingrese un número a evaluar: "))
result = nextPrime(num)

print(f"El número primo siguiente al número ingresado es: {result}")