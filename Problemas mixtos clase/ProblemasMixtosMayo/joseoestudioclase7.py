#haga una funcion que devuelva un numero primo
def esprimo (numero):
    cont = 0
    for x in range (1, numero + 1, 1):
        if numero % x == 0:
            cont = cont + 1
    return cont == 2        





 














n = int(input("ingrese su número:"))
if esprimo(n):
    print("es primo")
else:
    print("no es primo")    