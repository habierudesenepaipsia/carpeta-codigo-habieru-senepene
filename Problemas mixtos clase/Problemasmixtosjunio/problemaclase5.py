#######FUNCION QUE SE HAGA DESDE AHORA DEBE DECIR QUE HACE Y QUE RETORNA##########

#DESARROLLE UNA FUNCION QUE RECIBA UNA LISTA Y ELIMINE TODOS LOS ELEMENTOS NEGATIVOS DE LA LISTA Y RETORNE LA LISTA ACTUALIZADA
def cacaca1(list: int) -> list:
    lisata1 = []
    for x in list:
        if x >= 0:
            lisata1.append(x)
    return lisata1    

l = cacaca1(1, -2, 3, -4, 5)

print(l)