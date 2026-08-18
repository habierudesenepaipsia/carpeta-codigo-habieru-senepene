#Celular

#Mod       Atributos         Tipo

#get       -IMEI             :int
#get       -Marca            :str
#get       -Almacenamiento   :float
#set       -Nivel_Bateria    :float
#get       -Sis_Op           :str

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