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
        return self.__numero

    #Setter
    @numero.setter
    def numero(self, nuevo_numero):
        if len(nuevo_numero) >= 5:
            self.__numero = nuevo_numero
        else:
            self.__numero = None


#Instaciar una clase para crear un objeto

celu_abdala = Celular(123456789)
celu_abdala.numero = "+569666666"
print("Número " , celu_abdala.numero)
celu_abdala.numero = "66"
print("Número " , celu_abdala.numero)
celu_abdala.so = "MAC"
print("OS", celu_abdala.os)


print(celu_abdala.numero)
         























        