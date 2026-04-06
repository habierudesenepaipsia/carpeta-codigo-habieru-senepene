nota_1 = float(input("cuál es su primera nota recordada?: "))
if nota_1 >= 1.0:
    if nota_1 <= 7.0:
        next
    else:
        print("valor incorrecto, coloque un valor bajo 7.0")
        exit()
else:
    print("valor incorrecto, coloque un valor sobre 1.0")
    exit()        
nota_2 = float(input("cuál es su segunda nota recordada?: "))
if nota_2 >= 1.0:
    if nota_2 <= 7.0:
        next
    else:
        print("valor incorrecto, coloque un valor bajo 7.0")
        exit()
else:
    print("valor incorrecto, coloque un valor sobre 1.0")
    exit()
nota_3 = float(input("cuál es su segunda nota recordada?: "))
if nota_3 >= 1.0:
    if nota_3 <= 7.0:
        next
    else:
        print("valor incorrecto, coloque un valor bajo 7.0")
        exit()
else:
    print("valor incorrecto, coloque un valor sobre 1.0")
    exit()
promedio_1 = (nota_1 + nota_2 + nota_3) / 3
if promedio_1 <= 3.99:
    print(f"su promedio es {promedio_1:.2f}, usted ha reprobado")
else:
    print(f"su promedio es {promedio_1:.2f}, usted ha aprobado")
#no voy a josear en clase