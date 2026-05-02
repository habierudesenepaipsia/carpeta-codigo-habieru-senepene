#Confeccione un algoritmo en diagrama de flujo que al leer el neto de una factura, calcule el I.V.A. y de cómo salida
#el total de la factura
factura = float(input("ingrese su factura:"))
iva = factura * 0.19
facturatotal = iva + factura
print(f"Su total de la factura es {facturatotal}")