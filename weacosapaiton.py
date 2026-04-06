nota_1 = float(input("cuál es su última nota recordada?: "))
if nota_1 >= 1.0:
    if nota_1 <= 7.0:
        if nota_1 >= 4.0:
            print("usted ha aprobado.")
        else:
            print("usted ha reprobado.")    
    else:
        print("valor incorrecto, coloque un valor bajo 7.0")
        exit()
else:
    print("valor incorrecto, coloque un valor sobre 1.0")
    exit()        
#el pepe ete sech potaxio los que saben el contexto    