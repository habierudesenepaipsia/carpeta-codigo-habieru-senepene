#desarrolle un programa que permita ingresar N números, y al finalizar despliegue el promedio sólo de los números positivos
val1 = 0
val2 = 0
conti1 = 1
conti2 = int(input("ingrese cuántos números desea ingresar:"))
while conti2 >= conti1:
    num1 = int(input("Ingrese sus números:"))
    if num1 > 0:
       val1 = val1 + 1
       val2 = val2 + num1
    conti1 = conti1 + 1
promedio = val2 / val1    
if val1 > 0:
    print(f"usted tiene {val1} números positivos, el promedio de ellos es {promedio}.")
else:
    print("usted no ha ingresado números positivos, reinténtelo")            