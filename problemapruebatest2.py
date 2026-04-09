# Desarrolle un programa que permita ingresar 3 números al usuario y despliegue el mayor delos números ingresados.
num_1 = float(input("ingrese su primer número:"))
num_2 = float(input("ingrese su segundo número:"))
num_3 = float(input("ingrese su tercer número:"))
if num_1 > num_2:
    if num_1 > num_3:
        print (f"el numero mayor es:{num_1}")
    else:
        print (f"el numero mayor es:{num_3}")
else:
    if num_2 < num_3:
        print (f"el numero mayor es:{num_3}")
    else:
        print (f"el numero mayor es:{num_2}")       