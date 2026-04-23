#pregunta al usuario cuántos números quiere ingresar, y el programa adopta esa cantidad para los números solicitados#pos1 = 0
pos1 = 0
conteo = 0
canum = int(input("Cuantos números quiere ingresar?:"))
while conteo < canum:
    num1 = int(input("ingrese sus numeros del 1 al 10:"))
    if num1 > 0:
        pos1 += 1
    conteo += 1
if pos1 > 0:
    print(f"usted tiene {pos1} números positivos, gloria a israel, תהילה למדינת ישראל הבוליביארית,      ")        
else:
    print("usted no ha ingresado números positivos, reintentelo")
