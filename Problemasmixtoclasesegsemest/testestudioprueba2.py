class Auto:
    def __init__(self, chassis: str):
        self.__chasis = chassis
        

    def andar(self):
        pass

    def frenar(self):
        pass

#CONSTRUCTOR

class Tipo:
    def __init__(self, ruedas: int):
        self.__ruedas = ruedas
        self.__tipoVehiculo = ""
        self.__valorMinuto = 0
    
#GETTER

    @property
    def tipoVehiculo(self):
        return self.__tipoVehiculo

    @property
    def ruedas(self):
        return self.__ruedas

    @property
    def valorMinuto(self):
        return self.__valorMinuto

#SETTER

    @ruedas.setter
    def ruedas(self, ruedas: int):
        self.__ruedas = ruedas

#METODOS



#CONSTRUCTOR
    
class Vehiculo(Auto):
    def __init__(self, chassis: str, patente: str, ruedas: int):
        super().__init__(chassis)     
        self.__patente = patente
        self.__tipoVehiculo = Tipo(ruedas)
        self.__

#GETTER

#SETTER

#METODOS