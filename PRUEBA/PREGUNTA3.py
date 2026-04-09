#Desarrolle un programa que permita ingresar la estatura y peso,
#si al dividir el peso por la estatura al cuadrado el valor es menor a 25 desplegaremos por pantalla peso normal, si sobrepasa los 25 mostraremos sobrepeso.
estatura = float(input("Ingrese su estatura:"))
peso = int(input("Ingrese su peso:"))
#valores ingresados
imc = peso / (estatura ** 2)
#imc listo
if imc < 25:
    print(f"su peso es{imc:.2f}, su peso es normal") 
#es flaco y normal
else:
    print(f"su peso es{imc:.2f}, usted sufre sobrepeso")    
#sufre obesidad