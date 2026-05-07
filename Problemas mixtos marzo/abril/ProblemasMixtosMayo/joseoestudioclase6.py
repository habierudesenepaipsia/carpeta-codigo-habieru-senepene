#1: el usuario ingresa un número, y el programa debe desplegar si es primo
#2: usuario ingrese cuantos números primos desea desplegar desde el 2




######### PRIMER PROBLEMA ########
mainreg = 0
indexnum1 = 1
indexnum2 = 1
numcontador = 0
chequeonum1 = 0
chequeonum2 = 0
register = 0
inputinicial1 = int(input("Ingrese su primer número:"))

while indexnum1 <= inputinicial1:
    nummod = inputinicial1 % indexnum1
    if nummod == 0:
        numcontador = numcontador + 1
    indexnum1 = indexnum1 + 1
if numcontador == 2:
    print("Su número es primo.")
else:
    print("Su número no es primo.")       
######### SEGUNDO PROBLEMA #########
