###
# python incluye muchos tipos de datos, algunos de ellos son:
# int: para números enteros
# float: para números decimales
# str: para cadenas de texto
# bool: para valores booleanos (True o False)
# también existen otros tipos de datos como:
# list: para listas de elementos
# tuple: para tuplas de elementos, las tuplas no son modificables, y como uso son para almacenar datos que no deben cambiar
# set: para conjuntos de elementos únicos, los sets no permiten elementos duplicados y no tienen un orden específico, por ejemplo set([1, 2, 3, 4, 5]) crea un conjunto con los números del 1 al 5
# dict: para diccionarios, los diccionarios son estructuras de datos que almacenan pares de clave-valor, por ejemplo {"nombre": "Juan", "edad": 30} crea un diccionario con la clave "nombre" y el valor "Juan", y la clave "edad" con el valor 30
# none: para representar la ausencia de valor, none es un tipo de dato especial que se utiliza para indicar que una variable no tiene un valor asignado, por ejemplo x = None asigna el valor None a la variable x
# dict es un tipo de dato muy útil para almacenar información estructurada, como por ejemplo información de una persona, un producto, etc.
# range: para representar un rango de números, el tipo de dato range se utiliza para generar una secuencia de números enteros, por ejemplo range(0, 10) genera una secuencia de números del 0 al 9
###
"""
edad = 30
print(edad)  # esto imprime el valor de la variable edad, que es 30
print(
    type(edad)
)  # esto imprime el tipo de dato de la variable edad, que es <class 'int'>

altura = 1.89  # float es decimales
print("la altura es de tipo float por que usa decimales")
print(altura)
print(type(altura))  #

nombre = "Juan"
print(nombre)
print(type(nombre))

# para los booleanos los representaremos con bool. puedes verdader (rtue) o falso (false)
esto_es_verdadero = True
print("esto es verdadero por que es un valor booleano")
print(esto_es_verdadero)

print(type(esto_es_verdadero))
######

esto_es_falso = False

print("esto es falso por que es un valor booleano")

print(esto_es_falso)
print(type(esto_es_falso))
"""
#######
"""
id_numero = 12345
print(id_numero)
apellido = "rodriguez"
print(apellido)
tarifa = 0.54
print(tarifa)
esta_wea_es_real = True
esta_wea_es_falsa_ijolaperra = False
print(esta_wea_es_real, esta_wea_es_falsa_ijolaperra)
"""

numero_documento = 203
print(numero_documento)
print(type(numero_documento))

pi = 3.1415
print(pi)
print(type(pi))

nombre = "Francisco"
print(nombre)
print(type(nombre))

hombre = True
mujer = False

print("Pregunta: ¿Su personaje es hombre?")
print("Si lo es, entonces ", hombre)
print("Si no lo es, entonces ", mujer)
