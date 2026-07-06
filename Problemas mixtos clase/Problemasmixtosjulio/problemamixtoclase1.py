#desarrollar un programa que indique hasta donde desea la serie
#1era regla, la impresion siempre va a ser con 2 numeros
#2da regla, no se puede pasar de la serie a no ser que los numeros calzen
#(1,3)
#(2,4)
#(5,7)
#(6,8)
#(9,11)
#(10,12)
#(13,15)
#(14,16)

input1 = 0
valor1 = 0
valor2 = 2
i1 = 1
banderaserie = False

serievalor = int(input("Ingrese un valor limite para que la serie acabe:"))

seriefinvalor = 0

while seriefinvalor < serievalor:
    if i1 % 2 != 0:
        print(f"({valor1}),({valor2})")
        valor1 = valor1 + 1 
        valor2 = valor2 + 1

    if i1 % 2 == 0:
        print(f"({valor1}),({valor2})")
        valor1 = valor1 + 3 
        valor2 = valor2 + 3

    seriefinvalor = seriefinvalor + 1    
    i1 = i1 + 1




    #############NO LOGRE TERMINARLO###########




    ####VERSION ARREGLADA POST CLASE##########

impar = 1
par = 2

serie = int(input("Ing. número :"))

while impar <= serie: 

   if impar <= serie:
      print("(", impar , "," , (impar + 2), ")")

   if par <  serie - 1:
      print("(", par , "," , (par + 2), ")")

   impar = impar + 4
   par = par + 4

