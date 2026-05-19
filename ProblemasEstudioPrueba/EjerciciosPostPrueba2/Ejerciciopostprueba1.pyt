#Desarrolle una función que reciba 2 argumentos(desde y hasta) y retorne la suma de todos los números impares que estén en ese rango.




########ESTRUCTURA########
#paso 1: definir la función, dentro debe tener 2 argumentos distintos que representen un rango de números.
#paso 2:hacer un ciclo con el rango de números ingresados
#paso 2,5: poner un evaluador de números para determinar si el número en cuestión del ciclo es par o impar, en caso de ser impar:
#paso 3:poner un contador sumatorio de números impares dentro del rango
#paso 4:retornar hacia la funcion la cantidad ya lista de números impares sumados
#paso






def sucbub(arguminic: int ,argumfini: int):
    argumimpar = 0
    while arguminic <= argumfini:
        if arguminic % 2 == 1:
            argumimpar = arguminic + argumimpar
        arguminic = arguminic + 1
    return argumimpar    



arguminicio = int(input("Ingrese su primer número:"))
argumfinito = int(input("Ingrese su segundo número:"))
funuciu = sucbub(arguminicio, argumfinito)

print(f"Entre los 2 números que ha ingresado, la suma de sus números impares es {funuciu}")