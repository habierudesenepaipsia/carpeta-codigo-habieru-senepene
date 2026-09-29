#YASISIMEGUTAYA
#SADINMSUYHTNBGRMEENCANTA
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



   def deuda(self) -> int:
      return self.__suma_cargos() - self.__suma_abonos()

   def abono(self, glosa: str,monto: int) -> bool:
      if monto <= self.deuda():
         tupla_abonos = (glosa, monto)
         self.__abonos.append(tupla_abonos)
         return True

      return False

   def __suma_cargos(self):
      suma = 0
      for c in self.__cargos:
         suma += c[1]

      return suma


   def __suma_abonos(self):
      suma = 0
      for a in self.__abonos:
         suma += a[1]

      return suma

   def saldo(self):
      return self.__cupo -  self.deuda()


   def cargo(self, glosa: str, monto :int) -> bool:
      if monto <= self.saldo():
         self.__cargos.append((glosa, monto))
         return True
      else:
         return False
     

   def estado_cuenta(self) -> str:
      estado = ""
      for cargos in self.__cargos:
         estado += f" C | {cargos[0]} | {cargos[1]} | 0 |\n"

      for abonos in self.__abonos:
         estado += f" A | {abonos[0]} | 0 | {abonos[1]} |\n"


      return estado        
   
#---------------------------------------------


tc = TarjetaCredito(1111, "Emilia", "2026", "123")

print(tc)
tc.cargo("Completo1", 1000)
tc.cargo("Completo2", 2000)
tc.cargo("Completo3", 3000)
tc.cargo("Completo4", 4000)
tc.abono("Efectivo", 1000)
tc.abono("Efectivo", 1000)
tc.cupo = 55000
tc.cargo("Choripan", 46999)
print(tc.estado_cuenta())
print("Deuda: ", tc.deuda())
print("Saldo: ", tc.saldo())

      