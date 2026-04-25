#Supongamos que el I.P.C. de los meses de Febrero y Marzo fueron 0.3% y 0.6% respectivamente. Crear un algoritmo en diagrama
#de flujo que muestre el valor de un producto actualizado y la diferencia de precio entre el mes de febrero y Marzo.
productoing = int(input("ingrese el último valor de su producto:"))
#supongamos que la wea es 1800
productofebrero = productoing * 0.003
productofinfeb = productoing + productofebrero
productomarzo = productoing * 0.006
productofinmarzo = productomarzo + productoing
print(f"su producto actualmente cuesta {productoing}, en febrero costaba {productofinfeb}, y en marzo {productofinmarzo}.")
#EL CHRISTIAN ES MI SALVADOR, ME HIZO ESTOS PROBLEMAS