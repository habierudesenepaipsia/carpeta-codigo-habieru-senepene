class TarjetaCredito:
   # region Contructor
   def __init__(self, numero:int, nombre:str, vencimiento:int, cvv:int):
      self.__numero = numero
      self.__nombre = nombre
      self.__vencimiento = vencimiento
      self.__cupo = 50000
      self.__clave = 9999
      self.__cvv = cvv
      #Variable auxiliar
      self.__cargos = []
      self.__abonos = []
   # endregion

   # region Getter

   @property
   def numero(self):
      return self.__numero
   
   @property
   def nombre(self):
      return self.__nombre
   
   @property
   def vencimiento(self):
      return self.__vencimiento

   @property
   def cupo(self):
      return self.__cupo

   @property
   def clave(self):
      return self.__clave

   @property
   def cvv(self):
      return self.__cvv

   # endregion


   # region Setter
   @cupo.setter
   def cupo(self, nuevo_cupo: int):
      self.__cupo = nuevo_cupo

   @clave.setter
   def clave(self, nueva_clave: int):
      pass

   # endregion


   #Sobrescritura de métodos heredados
   def __str__(self):
      return f"(numero:{self.__numero}), (Nombre: {self.__nombre}), (Cupo: ${self.__cupo})"


   def cargo(self, glosa: str,monto: int) -> bool:
      #TODO: Juanito Todos, agregar validar si esxiet saldo para efectuar un cargo
      self.__cargos = [(glosa,monto),(glosa,monto)]
      self.__abonos = [(glosa,monto)]















tc = TarjetaCredito(1111, "Emilia", "2026", "123")

print(tc)
tc.comprar("Completo", 60000)
tc.cupo = 80000
tc.comprar("Completo", 60000)
tc.comprar("Completo", 60000)
tc.comprar("Completo", 60000)
tc.comprar("Completo", 60000)
tc.comprar("Completo", 60000)
tc.comprar("Completo", 60000)
tc.comprar("Bebida", -1000)
      
      