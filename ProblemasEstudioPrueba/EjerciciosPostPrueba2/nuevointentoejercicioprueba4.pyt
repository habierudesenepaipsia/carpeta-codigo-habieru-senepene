#Desarrolle una función que reciba un numero como argumento y retorne el 1er dígito de ese número, 
# la función debe validar que el número recibido sea positivo y menor a cien mil,
# de lo contrario retorna un cero que el argumento no cumple con las restricciones

####################ESTRUCTURA############

#paso1:definir funcion con un número x ingresado
#paso1,5: definir variables a usar bajo la funcion y modificarlas en caso de ser necesitado luego
#paso2: poner un if que no deje que continue si el número es igual o mayor a cien mil o si no es positivo,
#       de lo contrario el programa solo retorna un 0 con su propio return
#paso3: hacer un ciclo con el número x ingresado especifico de un ciclo,
#            hacer una division completa con el numero x ciclo en 10, y luego ingresar  un if que chequee si el número
#            ciclado es menor a dies, en caso de que si, el programa regresa ese número        
#paso5: fuera de la función, poner un input con su propia variable que guarde el número ingresado por el usuario
#paso6: colocar una variable que haga uso de la funcion ya hecha
#paso7: hacer un if que tire print y muestre el número final en comparación del inicial, y un else que en caso de que las condiciones
#        establecidas en el def no se cumplan, tire un mensaje de error


def functionpepe(numexingres):
    numexingresciclo = numexingres
    numayor = 0
    numaer = 0
    numvariba = 0
    if numexingres < 100000 and numexingres > 0:
        while numexingresciclo > 10:
            numexingresciclo = numexingresciclo // 10
            if numexingresciclo < 10:
                return numexingresciclo 

    else:
        print("Su número no cabe dentro de las especificaciones, reingrese")
        return 0 
    

test1 = int(input("Ingrese su número:"))

resultado = functionpepe(test1)


if resultado > 0:
    print(f"El primer dígito de su código es {resultado} del número {test1}.")
else:
    print("E R R O R")    