#Celular

#Mod       Atributos         Tipo

#get       -IMEI             :int
#get       -Marca            :str
#get       -Almacenamiento   :float
#set       -Nivel_Bateria    :float
#get       +Sis_Op           :str

#Métodos                      Tipo
 
#+Prender( )                  :bool
#+Llamar(nmrtelfno)           :int
#+Carga()
#+Celular(Imei{constructor})







############TAREA##########
#TRAER LOS 10 OBJETOS EN DIAGRAMA

class Celular:
    #__privado
    #_publico
    def __init__(self, imei): # Indica que es un argumento necesario para instanciar el objeto 
        self.__imei = imei
        self.__marca = ""
        self.__numero = None        
        self.__almacenamiento = 0.0
        self.__nivelbateria = 0.0
        self.__sisop = ""       
        self.so = "Android"

    #Getter
    @property
    def numero(self):
        self.__numero



celu_abdala = Celular(123456789)
celu_abdala.numero = 11111111



print(celu_abdala.numero)
         























        