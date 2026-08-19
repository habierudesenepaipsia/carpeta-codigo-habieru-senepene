class salondebaile:
    def init(self,numsalon):
        self._numsalon= numsalon
        self._horario= 0.0
        self._ubicacion=""
        self.__listainv={}
        self._capacidadmax=int
        self.__personal={}


    #getter
    @property
    def personal(self):
        return self.__personal


    #setter
    @personal.setter
    def personal(self, nuevo_personal):
        if len(nuevo_personal) >= 0:
            self.__personal = nuevo_personal
        else:
            self.__personal = None



class claseinformatica:
    def init(self,numsalon):
        self.horarios=0.0
        self.profesor=int
        self.siglacurs=""
        self.alumn=""
        self.equipos={}








class iglesia:
    def init(self,religion):
        self.pastors={}
        self.hermans={}
        self.horarsermons=0.0
        self.capasiento=int
        self.disposaudio={}


