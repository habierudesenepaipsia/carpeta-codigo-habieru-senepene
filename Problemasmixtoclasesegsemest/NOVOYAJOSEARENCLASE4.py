class Salondebaile:
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



class Informatica:
    def init(self,numsala):
        self._numsala= numsala
        self._horarios=0.0
        self._profesor=int
        self._siglacurs=""
        self._alumn=""
        self._equiposinform={}

    @property
    def profesor(self, otro_profesor):
        if self._profesor == 0:
            self._profesor = otro_profesor
        else:
            self.profesor = None     





class Iglesia:
    def init(self,religion):
        self._religion= religion
        self._pastors={}
        self._hermans={}
        self._horarsermons=0.0
        self._capasiento=int
        self.__disposaudio={}

    @property
    def capasiento(self, max_capa):
        if self._capasiento > 250:
            self._capasiento = max_capa
        else:
            self._capasiento = ""