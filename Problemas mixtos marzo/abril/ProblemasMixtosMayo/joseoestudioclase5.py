#desarrolle un programa en el que el usuario ingrese 2 números, y el sistema va a indicar si esos 2 números son amigos
#220 y 284 es un ejemplo
mainreg = 0
indexnum1 = 1
indexnum2 = 1
chequeonum1 = 0
chequeonum2 = 0
register = 0
inputinicial1 = int(input("Ingrese su primer número:"))
inputinicial2 = int(input("Ingrese su segundo número:"))

while indexnum1 < inputinicial1:
    inputmod1 = inputinicial1 % indexnum1
    if inputmod1 == 0:
        chequeonum1 = chequeonum1 + indexnum1
    indexnum1 = indexnum1 + 1    
while indexnum2 < inputinicial2:
    inputmod2 = inputinicial2 % indexnum2
    if inputmod2 == 0:
        chequeonum2 = chequeonum2 + indexnum2
    indexnum2 = indexnum2 + 1
if chequeonum1 == inputinicial2 and chequeonum2 == inputinicial1:
    print("Los números son amigos.")
else:
    print("Los números no son amigos.")                