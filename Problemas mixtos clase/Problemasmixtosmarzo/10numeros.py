pos1 = 0
conteo = 0
while conteo < 10:
    num1 = int(input("ingrese sus numeros del 1 al 10:"))
    if num1 > 0:
        pos1 += 1
    conteo += 1
if pos1 > 0:
    print(f"usted tiene {pos1} números positivos, gloria a israel, תהילה למדינת ישראל הבוליביארית, ")        
else:
    print("usted no ha ingresado números positivos, reintentelo")
