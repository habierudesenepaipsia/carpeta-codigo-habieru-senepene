#Desarrolle un programa que agregue a una lista los números ingresados por el usuario que cumplan la siguiente condición:
#1, x debe ser positivo.
#2, x el último dígito debe ser multiplo de 2.
#3, x codigo de salida es 999 
#Requerimientos
#A: x debe crear una funcion llamada cumple que reciba un argumento númerico (el numero ingresado por el usuario) 
#   y retorne verdadero o falso si se debe agregar a la lista
#Restricciones
#x No puede ocupar ni transformar el número a un string o a una variable cadena, debe trabajar con el número directamente

def cumple(num: int) -> bool:
    if num > 0:
        if (num % 10) % 2 == 0:
            return True
        else:
            return False
    else:
        return False

listnum = []
num = 0

while num != 999:
    num = int(input("ingrese el siguiente número:"))
    num1 = cumple(num)
    
    if num1 == True:    
        listnum.append(num)
              
    else:
        if num == 999:
            print("lista terminada")
        else:
            print("número incorrecto, reingrese") 

print(listnum)        