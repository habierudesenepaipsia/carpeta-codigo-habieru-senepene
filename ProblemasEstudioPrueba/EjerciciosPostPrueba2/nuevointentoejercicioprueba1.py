def cicclolal(argummenor: int, argummayor: int):
    argumimpar = 0
    argumciclo = argummenor
    while argumciclo <= argummayor:
        if argumciclo % 2 == 1 or argumciclo == 1:
            argumimpar = argumimpar + argumciclo
        argumciclo = argumciclo + 1
    return argumimpar



test1 = int(input("Ingrese su primer número designado:"))
test2 = int(input("Ingrese su segundo número designado:"))


resultado = cicclolal(test1, test2)

print(f"La cantidad de números impares sumados entre su rango designado es: {resultado}")