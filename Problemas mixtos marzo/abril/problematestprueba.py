#La empresa “Sito Man Boy” vende sillas al por mayor, sus ventas han bajado y elaboraron un plan para incentivar la producción, 
#al trabajador se le cancela 120 pesos por cada silla construida, 
#si en el mes supera las 1000 unidades se le cancelará un adicional de 20 pesos adicional por cada silla sobre las 1000. 
totalsillas = int(input("cuantas sillas ha construido en total?:"))
if totalsillas <= 1000:
    bonototal_1 = totalsillas * 120
    print(f"su bono total serian:{bonototal_1}")
else:
    totalsillasdesc = totalsillas - 1000
    bonototal_1 = 1000 * 120
    bonototal_2 = totalsillasdesc * 140
    bonocompleto = bonototal_1 + bonototal_2
    print(f"su bono total serian:{bonocompleto}")
#ta bien esta wea pero es específica, es mejor hacer variables uno por uno y preguntarlas uno por uno, de manera en que
#al final solo quede un if con los cálculos enteros y en el else solo quede un calculo pelado