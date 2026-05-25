#listas
#cuando nosotros trabajamos con estructuras de datos, existen 2 principales, las estaticas y las dinamicas, aunque ahora son más como mutables e inmutables
#NO SE PUEDE OCUPAR REMOVE EN LAS SIGUIENTES PRUEBAS
numeros = [7,3]
#agregar al final de la lista de elementos
numeros.append(8)

numeros.append(2)

print(numeros)

numeros.insert(1,9)


print(numeros)

#eliminar
del numeros[2]
#numeros.remove(3)

print(numeros)

#recorrer una lista 
for e in numeros:
    print("Elemento :", e)

print("Cantidad de elementos: ", len(numeros))


ultimo_indice = len(numeros) - 1

#n = len(numeros) # - 1

#for i in range(n - 1):
    #print()

#OTRA MANERA DISIMILAR

print("Recorrer lista desde el último hasta el primero")
for i in range(ultimo_indice, -1, -1):
   e = numeros[i]
   print("Elemento", e )    



for x in range (10000000):
    numeros.append(x)        


print(numeros)    