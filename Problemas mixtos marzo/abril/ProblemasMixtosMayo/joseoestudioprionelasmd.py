#Desarrolle un programa en donde el usuario ingrese un número de N digitos,
#  y debes indicar cuantos números pares e impares tiene.



numloop1 = int(input("Ingrese su número de multiples dígitos:"))
contadornum1 = 0
contadornum2 = 0
num1x = 0


while numloop1 > 0:
    num1x =  numloop1 % 10
    if num1x % 2 == 0:
        contadornum1 = contadornum1 + 1

    else:
        contadornum2 = contadornum2 + 1
    numloop1 = numloop1 // 10


print(f"Los números son {contadornum1} pares y {contadornum2} de impares.")    