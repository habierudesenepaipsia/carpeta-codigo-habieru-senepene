#Suponga que un individuo desea invertir su capital en un banco y desea saber cuanto dinero ganara después de un mes si el banco
#paga a razón de 2% mensual.
capitaling = int(input("ingrese su dinero que desea invertir:"))
capitalmes = capitaling * 0.02
capitalfin = capitalmes + capitaling
print(f"su dinero invertido subira a {capitalfin} en un mes")