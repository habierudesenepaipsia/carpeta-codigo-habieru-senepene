#MUERE MUERE
#Desarrolle una función que reciba un número como argumento,
#y retorne el siguiente número primo que encuentre después del número recibido como parámetro.

############ESTRUCTURA##############

#paso1: Definir la función como tal, con que reciba un número
#paso1,5: Declarar cada variable a usar minuciosamente de manere que luego el código no muera
#paso2: 
#
#paso3:
#       
#paso4: 
#paso5: 
#paso6:

#paso7:

#paso8:
#paso9:


def fubcioc(numingresprim):
    signumprim = 0
    numprimociclo = 0
    numprimfound = False
    nunmadhaf = numingresprim
    while numprimfound == False:
        numprimociclo = 1
        while numprimociclo <= nunmadhaf: 
            if nunmadhaf % numprimociclo == 0:
                signumprim = signumprim + 1
            numprimociclo = numprimociclo + 1
        if signumprim == 2 and numingresprim < nunmadhaf:
            numprimfound = True
            return nunmadhaf
        signumprim = 0
        nunmadhaf = nunmadhaf + 1
       

rtest = int(input("Ingrese su número:"))

resultado = fubcioc(rtest)
print(f"El siguiente número primo a {rtest} es {resultado}.")