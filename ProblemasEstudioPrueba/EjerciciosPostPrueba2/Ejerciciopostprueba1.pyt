#Desarrolle una función que reciba 2 argumentos(desde y hasta) y retorne la suma de todos los números impares que estén en ese rango.
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