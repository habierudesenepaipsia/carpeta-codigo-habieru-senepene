#Desarrolle una funcion que reciba un numero como argumento
#que retorne una lista con las cantidades de elementos segun el argumento recibido, que muestre inicialmente numeros impares y luego por ultimo los numeros pares 
lista1 = []
ekis = int(input("Ingrese un número x límite:"))
for n in range (1,ekis + 1):
    if n % 2 != 0:
        lista1.append(n)
for n in range (ekis, 0, -1):
    if n % 2 == 0:
        lista1.append(n)
print(lista1) 