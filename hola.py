nota_1 = float(input("ingrese su primera nota: "))
nota_2 = float(input("ingrese su segunda nota: "))
nota_3 = float(input("ingrese su tercera nota: "))

promedio_final = (nota_1 + nota_2 + nota_3) / 3
if promedio_final >= 4.0:
    print(f"su promedio final es: {promedio_final:.2f}, usted aprobó")
else:
    print(f"su promedio final es:{promedio_final:.2f}, usted reprobó por flojo e inútil")
#joseando en clase
#estudiar condiciones SIMPLES DOBLES MULTIPLES
#desarrolle un ejercicio que permita ingresar la edad de una persona y despliegue si es mayor de edad