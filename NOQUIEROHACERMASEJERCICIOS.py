#desarrolle un programa que permita ingresar una nota. La nota debe estar entre 1 y 7, de lo contrario, enviar un mensaje al usuario de "nota invalida"
nota_1 = float(input("Ingrese su 1era nota entre el rango de 1.0 y 7.0:"))
if 1.0 <= nota_1:
    print("nota correcta, su nota es:",nota_1)
    if 7.0 <= nota_1:
        print("nota correcta, su nota es:",nota_1)
else:
    print("valor inválido, reingrese.")        