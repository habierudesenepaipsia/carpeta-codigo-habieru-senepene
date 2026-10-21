class VehiculoElectrico:
    def __init__(self, codigo: str, marca: str, modelo: str, tarifaBase: int, bateria: float, cargaActual: int):
        self.__codigo: codigo
        self.__marca: marca
        self.__modelo: modelo
        self.__tarifaBase: tarifaBase
        self.__bateria: bateria
        self.__cargaActual: cargaActual
        self.__disponible: None
        self.cargarBateria: 0.0
        self.calcularCosto: 0 = 0


    @property
    def codigo(self):
        return self.__codigo

    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    
    @property
    def bateria(self):
        return self.__bateria

    @property
    def cargaActual(self):
        return self.__cargaActual
    
    @property
    def tarifaBase(self):
        return self.__tarifaBase
    
    @property
    def disponible(self):
        return self.__disponible

    @property
    def cargarBateria(self):
        return self.__cargarBateria

    @property
    def calcularCosto(self):
        return self.__calcularCosto



    @cargarBateria.setter
    def cargarBateria(self, porcentaje: float):
        if porcentaje <= 100:
            self.__cargarBateria = porcentaje
            return True
        else:
            self.__cargarBateria = 100
            return self.__cargarBateria

    @calcularCosto.setter
    def calcularCosto(self, minutos: int):
        if minutos > 0:
            self.__calcularCosto = self.__tarifaBase * minutos
            return True
        else:
            self.__calcularCosto = 0
            return self.__calcularCosto




class RegistroAlquiler:
    def __init__(self, idAlquiler: str, vehiculo: VehiculoElectrico, minutos: int, costoTotal: int):
        self.__idAlquiler: idAlquiler
        self.__vehiculo: vehiculo
        self.__minutos: minutos
        self.__costoTotal: costoTotal

    @property
    def idAlquiler(self):
        return self.__idAlquiler
    @property
    def vehiculo(self):
        return self.__vehiculo
    @property
    def minutos(self):
        return self.__minutos
    @property
    def costoTotal(self):
        return self.__costoTotal
 


class Cliente:
    def __init__(self, rut: str, nombre: str, saldo: int):
        self.__rut: rut
        self.__nombre: nombre
        self.__saldo: saldo
        self.__alquileres: []
        self.recargarSaldo: 0 = None
        self.alquilarVehiculo: vehiculo = None
        self.__validarRut: rut = None


    @property
    def rut(self):
        return self.__rut

    @property
    def nombre(self):
        return self.__nombre

    @property
    def saldo(self):
        return self.__saldo

    @property
    def alquileres(self):
        return self.__alquileres

    @property
    def recargarSaldo(self):
        return self.__recargarSaldo

    @property
    def alquilarVehiculo(self):
        return self.__alquilarVehiculo

    @property
    def validarRut(self):
        return self.__validarRut


    @rut.setter
    def rut(self, rut: str):
        if len(rut) >= 9 and len(rut) <= 12:
            self.__rut = rut
            return True
        else:
            return print("RUT inválido. Debe tener entre 9 y 12 caracteres.")
    
    @saldo.setter
    def saldo(self, saldo: int):
        if saldo >= 0:
            self.__saldo = saldo
            return True
        else:
            return print("Saldo inválido. Debe ser un valor positivo.")



class AutoElectrico(VehiculoElectrico):
    def __init__(self, pasajeros: int, patente: str, codigo: str, marca: str, modelo: str, tarifaBase: int, bateria: float, cargaActual: int):
        super().__init__(codigo, marca, modelo, tarifaBase, bateria, cargaActual)
        self.__pasajeros: pasajeros
        self.__patente: patente
        self.calcularCosto: 0 = 0
    


    @property
    def pasajeros(self):
        return self.__pasajeros

    @property
    def patente(self):
        return self.__patente

    @property
    def calcularCosto(self):
        return self.__calcularCosto

    @patente.setter
    def patente(self, patente: str):
        if len(patente) == 6:
            self.__patente = patente
            return True
        else:
            return print("Patente inválida. Debe tener 6 caracteres.") 

    @tarifaBase.setter
    def tarifaBase(self, tarifaBase: int):
        if tarifaBase >= 0:
            self.__tarifaBase = tarifaBase
            return True
        else:
            return print("Tarifa base inválida. Debe ser un valor positivo.")
            
            


class ScooterElectrico(VehiculoElectrico):
    def __init__(self, codigo, bateria, tarifaBase, disponible, cascoIncluido: bool):
        super().__init__(codigo, bateria, tarifaBase, disponible)
        self.__cascoIncluido: cascoIncluido
        self.calcularCosto: 0 = 0

    @property
    def cascoIncluido(self):
        return self.__cascoIncluido
    @property
    def calcularCosto(self):
        return self.calcularCosto
    @property
    def disponible(self):
        return self.__disponible
    @property
    def codigo(self):
        return self.__codigo

     



        