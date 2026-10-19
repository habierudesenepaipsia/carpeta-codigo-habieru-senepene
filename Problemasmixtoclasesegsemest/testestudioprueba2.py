class Auto:
    def __init__(self, chassis: str):
        self.__chasis = chassis
        

    def andar(self):
        pass

    def frenar(self):
        pass

class Tipo:
    def __init__(self, ruedas: int, ):









class Vehiculo(Auto):
    def __init__(self, chassis: str, patente: str, ruedas: int):
        super().__init__(chassis)     
        self.__patente = patente
        self.__tipoVehiculo = Tipo(ruedas)
        self.__



