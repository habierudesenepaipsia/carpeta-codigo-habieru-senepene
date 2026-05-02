class Celular:
    def __init__ (self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.__precio = precio

    def mostrar_info(self):
        print("Celular: {self.marca} {self.modelo} - precio: ${self.__precio}")

celu1 = Celular("Huawei", "SXI", 1200)
celu2 = Celular("Samsung", "SIII", 600)      

