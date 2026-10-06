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

#----------------------------------------------
class Persona:
   def __init__(self, rut: str, nombre: str):
      self.__rut = rut
      self.__nombre = nombre

   @property
   def rut(self):
      return self.__rut

   @property
   def nombre(self):
      return self.__nombre

   @rut.setter
   def rut(self, rut: str):
      self.__rut = rut

   @nombre.setter
   def nombre(self, nombre: str):
      self.__nombre = nombre


class Cliente(Persona):

   def __init__(self, rut, nombre, giro):
      super().__init__(rut, nombre)
      self.__giro = giro
      self.__billetera = [TarjetaCredito]

   @property
   def giro(self):
      return self.__giro

   @giro.setter
   def giro(self, giro: str):
      self.__giro = giro 

   def agregar_tc(self,tc_nueva: TarjetaCredito):
      existe = False
      for tc in self.__las_tc:
         if tc_nueva.numero == tc.numero:
            existe = True

      if not existe:
         self.__las_tc.append(tc_nueva)
         return True
      else:
         return False

   def cantidad_tcs(self):
      return len(self.__las_tc)

   def __str__(self):
      #{type(self).__name__}"
      quien_soy = f"Rut: {self.rut}, Nombre: {self.nombre}, Giro: {self.giro} \n"
      quien_soy += f"Soy Cliente de tipo {Cliente.__bases__}"
      return quien_soy

   
   
#---------------------------------------------

cli = Cliente("1-9", "Juanito", "Ferreteria")
print(cli)





      