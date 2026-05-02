#Crear un algoritmo en diagrama de flujo que al ingresar dos números imprima el mayor de ellos o IGUALES si son iguales
val1 = input("ingrese su primer número:")
val2 = input("ingrese su segundo número:")
if val1 < val2:
    print(f"su número mayor es:{val2}")
elif val1 == val2:
    print(f"ambos números son de igual valor")
else:
    print(f"su número mayor es:{val1}")   