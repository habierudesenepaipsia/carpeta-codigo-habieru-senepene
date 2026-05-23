positivos = 0
suma = 0
x = 1
z = int(input("Cuantos números desea ingresar: "))
while x <= z:
   num = int(input(f"Ing. número [{x} de {z}]: "))
   if num > 0:
      suma = suma + num
      positivos = positivos + 1

   x = x + 1

print(f"Positivos ingresados = {positivos}")

if positivos > 0:
   #Truncar(división entera) promedio = suma // positivos
   #Redondear 
   promedio = suma / positivos
   #Redondear(aproximar) promedio = round(promedio, 1)
   print(f"Promedio = {promedio}")
