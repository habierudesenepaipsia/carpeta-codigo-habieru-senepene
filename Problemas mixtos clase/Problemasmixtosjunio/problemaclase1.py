#crear lista con 30 elementos en donde siga la secuencia de valores 1 , 0 , 1 , 0 , 1 , 0 ...

listnum = []



for i in range(30):
    if i % 2 == 0:
        listnum.append(1)

    else:
        listnum.append(0)     

    print(i)


print(listnum)