# input

# si queremos entrada por teclado usamos la funcion input

nombre_usuario = input("ingresa tu nombre: ")
print("hola como estas", nombre_usuario)

# para entrada de enteros usamos int
edad = int(input("Ingrese su edad:"))
print("tu edad es", edad)

usd = float(input("Ingrese la cantidad en USD:"))
print("la cantidad en USD es", usd)

# para .split usamos el metodo split para separar palabras
nombres, apellidos, ciudad, pais = input(
    "Ingrese su nombre, apellido, ciudad y pais separados por espacios: "
).split()

print(
    "su nombre es",
    nombres,
    "su apellido es",
    apellidos,
    "su ciudad es",
    ciudad,
    "y su pais es",
    pais,
)
