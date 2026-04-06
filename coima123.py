"""En un terminal salen dos buses con destino a la ciudad de valdivia,
transportan a 35 pasajeros cada uno, el valor del pasaje
fue de 5500. cual es la recaudacion obtenida"""

# #V.0.0.1
# p_bus_1 = int(input("Pasajeros 1er bus :"))
# p_bus_2 = int(input("Pasajeros 2do bus :"))
# valor_pasaje = int(input("Valoe pasaje :"))
# recaudacion = (p_bus_1 + p_bus_2) * valor_pasaje
# print(f"El número total de pasajeros es: {p_bus_1 + p_bus_2}")
# print(f"El valor del pasaje es: {valor_pasaje}")
# print(f"La recaudación obtenida es: {recaudacion}")

# #V.0.0.2
# bs = 0
# pj = 0
# rc = 0
# tt = 0

# print("ingrese los datos")

# bs = int(input("cantidad de buses: "))
# pj = int(input("cantidad de pasajeros por bus: "))
# rc = int(input("costo del pasaje: "))

# tt = bs * pj * rc

# print(f"la recaudación total es {tt}")

#Atajos de teclado
"""una distribudora de insumos computacionales compro 20 cajas
de mouse. Si cada caja contiene 16 mouse y el valor de cada mouse es de 3500 cuando debio cancelar la distribuidora
por dicha compra"""

# cajas_mouse = #TODO ingreso del usuario
# mouse_por_caja = #TODO: ingreso del usuario
# valor_mouse = #TODO: ingreso del usuario

# total_mouse = cajas_mouse * mouse_por_caja
# total_compra = total_mouse * valor_mouse
# print(f"El número total de mouse comprados es: {total_mouse}")
# print(f"El valor de cada mouse es: {valor_mouse}")
# print(f"El total a cancelar por la compra es: {total_compra}")

"""Una persona tiene 100.000 pesos y decide invertir 70.000 pesos de ellos en bonos hipotecarios
de un 5% (mensual) y el resto en un deposito a plazo a un 10%
(mensual) ¿cuánto dinero ganará esta persona después de "n" meses?"""

# pesos_que_tiene = int(input("Ingrese la cantidad de dinero que tiene: "))
# inversion_total = int(input("Ingrese la cantidad de dinero que desea invertir: "))
# n_meses = int(input("Ingrese el número de meses de inversión: "))
# print("********** Interés de inversiones *************")
# int_bonos = int(input("Ingrese porcentaje de ganancia en bonos : "))
# int_dep = int(input("Ingrese porcentaje interés en depósitos : "))

# dinero_dep = pesos_que_tiene - inversion_total

# inversion_bonos = inversion_total * (int_bonos / 100)
# inversion_deposito = dinero_dep * (int_dep / 100)
# ganancia_mensual = inversion_bonos + inversion_deposito
# print("************* Detalle de ganacias **********************")
# print("Dinero invertido en depósitos :", dinero_dep)
# print(f"Inversión {int_bonos}% : {inversion_bonos}")
# print(f"Depósitos {int_dep}% : {inversion_deposito}")
# print("Total ganacia mensual :", ganancia_mensual)
# print("Total período de ", n_meses, "meses")
# ganancia_total = ganancia_mensual * n_meses
# print(f"{n_meses} meses es: {ganancia_total}")


""" un empleado  de una empresa se le cancela como sueldo base es $520.000.
 ¿Cuál es el sueldo líquido del empleado si los descuentos legales son un 20% del sueldo base?."""

sueldo_base = int(input("ingrese el sueldo base: "))
descuento_legal = sueldo_base * 0.20
sueldo_liquido = sueldo_base - descuento_legal
print(f"El sueldo base del empleado es: {sueldo_base}")
print(f"El descuento legal es: {descuento_legal}")
print(f"El sueldo líquido del empleado es: {sueldo_liquido}")