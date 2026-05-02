#edad adolescente, adulto o niño
#con if y else sin elif
edad = int(input("Ingrese su edad: "))
if edad < 0:
    print("Edad no válida")
else:
    if edad < 13:
        print("Eres un niño")
    else:
        if edad < 18:
            print("Eres un adolescente")
        else:
            print("Eres un adulto")
            