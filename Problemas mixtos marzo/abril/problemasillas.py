#Desarrolle un sistema que permite ingresar 10 trabajadores, por cada uno de ellos ingresar la cantidad de sillas construidas (sueldo), el cálculo es el siguiente:
#-Por cada silla construida se le paga 1000 pesos. -Si supera las 2000 sillas construidas le pagaremos 20 pesos más sobre las 2000.
#El sistema debe entregar la siguiente estadística, al finalizar los 10 trabajadores:
#A) Total a pagar por todos los trabajadores.
#B) Total de sillas construidas.
#C) Total de bono pagado por sillas sobre 2000
#D) Cuántos trabajadores hicieron más de 2000 sillas.
#E) Cuanto es el promedio de silla entre todos los trabajadores.

####MEVOYASUICIDAR#####
sillconstruid = 1000
bono = 20
contador = 1
trabajadorspaga = 0
bonosill = 0
promedsill = 0
trabajadors = 0
sobrtrabajadors = 0
sillconstruidtrab = 0
totalpaga = 0
while contador <= 10:
    sillconstruidtrab= int(input("Ingrese el número de sillas construídas por trabajador, individualmente: "))
    if contador == 10:   
        if sillconstruidtrab > 2000:
            sobrtrabajadors = sillconstruid + 20
            trabajadorspaga = sillconstruidtrab * sobrtrabajadors       
            print(f"la paga de sus trabajadores es: {trabajadorspaga}")
        else:               
             trabajadorspaga = sillconstruid * sillconstruidtrab
             print(f"la paga de sus trabajadores es: {trabajadorspaga}")  
    contador = contador + 1
    #MERINDOCONCHETUMARE#