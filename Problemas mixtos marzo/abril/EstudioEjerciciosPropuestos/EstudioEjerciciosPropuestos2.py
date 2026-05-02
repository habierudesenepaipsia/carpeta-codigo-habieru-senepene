#Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá
#por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo
#base y comisiones.
sueldobase = int(input("ingrese su sueldo base:"))
sueldo3mes = sueldobase * 3
comisionbase = sueldobase / 10
comision3mes = comisionbase * 3
sueldototal = sueldo3mes + comision3mes
#test
print(f"Respecto a su sueldo base, usted recibirá {comision3mes} extra en comisiones en este mes, y su sueldo total por las 3 ventas más sus comisiones es {sueldototal}.")