class Cliente:
    def __init__(self, rut: str):
        self.__rut = rut
        self.__correo = " "

    @property
    def rut(self) -> str:
        return self.__rut

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo (self, nuevoCorreo):
        self.__correo = nuevoCorreo




class Empresa(Cliente):
    def __init__(self, rut, razonSocial: str, giro: str, direccionComercial: str, repLegal: str):
        super().__init__(rut)
        self.__razonSocial = razonSocial
        self.__giro = ""
        self.direccionComercial = ""
        self.__repLegal = ""

    @property
    def razonSocial(self):
        return self.__razonSocial

    @property
    def giro(self):
        return self.__giro

    @property
    def direccionComercial(self):
        return self.direccionComercial

    @property
    def repLegal(self):
        return self.__repLegal


    @giro.setter
    def giro (self, ultimoGiro):
        #self.__giro = ultimoGiro
        pass

    @direccionComercial.setter
    def direccionComercial (self, dcAsignada):
        #self.direccionComercial = dcAsignada
        pass


    @repLegal.setter
    def repLegal (self, mostrarRepLegal):
        #self.__repLegal = mostrarRepLegal
        pass

class Persona(Cliente):
    def __init__(self, rut, nombre):
        super().__init__(rut)
        self.__nombre = ""
        self.direccionParticular = ""

    @property
    def nombre(self):
        return self.__nombre

    @property
    def direccionParticular(self):
        return self.direccionParticular


    @nombre.setter
    def nombre (self, ingresarNombre):
        self.__nombre = ingresarNombre

    @direccionParticular.setter
    def direccionParticular (self, ingresarDireccionParticular):
        self.direccionParticular = ingresarDireccionParticular

class Telefono:


####pepe:(((####