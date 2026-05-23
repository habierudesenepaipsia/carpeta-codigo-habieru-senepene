# Desarrolle una función que reciba un numero como argumento 
# y retorne el 1er dígito de ese número, 
# la función debe validar que el número recibido sea positivo y menor a cien mil, 
# de lo contrario retorna un cero que el argumento no cumple con las restricciones.

def firstDigit(numEval):
    if numEval > 0 and numEval < 100000:
        numEval = str(numEval)
        firstDigit = int(numEval[0])
        return firstDigit
    else:
        print("Número ingresado no cumple con las restricciones")
        return 0
    

print("Este programa evaluará si el número ingresado es positivo y menor que 100.000, y mostrará el primer dígito de el número ingresado.")
print("Ingrese los siguientes datos:\n")

num = int(input("Ingrese el número a evaluar: "))
result = firstDigit(num)

if result > 0:
    print(f"El primer dígito del número ingresado es: {result}")