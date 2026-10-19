#CLASE TELÉFONO------------------------------------------------------
class Telefono:
   def __init__(self, numero: str):
      self.numero = numero

   def llamar(self, fecha, hora, numero, minutos_hablados) -> bool:
      #muchas intrucciones que solo hace teléfono
      pass


#CLASE CELULARPREPAGO---------------------------------------------
class CelularPrepago(Telefono):
   def __init__(self, numero, imei, fecha_compra, minutos, saldo, megas):
      super().__init__(self, numero)
      self.__imei = imei
      self.__fecha_compra = fecha_compra
      self.__minutos = minutos
      self.__saldo = saldo
      self.__megas = megas
      self.__llamados = []


   #GETTER-----
   @property
   def imei(self):
      return self.__imei

   @property
   def fecha_compra(self):
      return self.__fecha_compra

   @property
   def minutos(self):
      return self.__minutos

   @property
   def saldo(self):
      return self.__saldo

   @property
   def megas(self):
      return self.__megas

   #SETTER----
   @fecha_compra.setter
   def nombre(self, fecha_compra: str):
      if len(fecha_compra) >= 10:
         self.__fecha_compra = fecha_compra


   #MÉTODOS---------------------------------------------------------------

   def navegar(self, megas) -> bool:
      if megas >= 1:
         self.__saldo = self.__saldo - (megas * 10)
         return True
      else:
         return False


   def detalle_llamados(self) -> list:
      return self.__llamados


   def reiniciar(self) -> bool:
      self.__minutos = 0
      self.__llamados.clear


   def cargar(self, monto) -> bool:
      if monto >= 1500:
         self.__saldo = self.__saldo + monto
         return True
      else:
         return False


   def llamar(self, fecha, hora, numero, minutos_hablados):
      super().llamar(fecha, hora, numero, minutos_hablados)

      if self.__saldo >= (30 * minutos_hablados):
         self.__saldo = self.saldo - (30 * minutos_hablados)
         self.__llamados.append((fecha, hora, numero, minutos_hablados))
         self.__minutos = self.__minutos + minutos_hablados
         return True
      else:
         return False


#CLASE CLIENTE-----------------------------------------------
class Cliente:

   def __init__(self, rut):
      if len(rut) == 13:
         self.__rut = rut
      else:
         self.__rut = ""

      self.__correo = ""

   @property
   def rut(self):
      return self.__rut

   @property
   def correo(self):
      return self.__correo

   @correo.setter
   def correo(self, correo: str):
      if len(correo) != 0 and correo != None:
         self.__correo = correo 


   #Sobrescritura del padre
   def __str__(self):
      #{type(self).__name__}"
      quien_soy = f"Rut: {self.rut}, Nombre: {self.nombre}, Giro: {self.giro} \n"
      quien_soy += f"Soy Cliente de tipo {Cliente.__bases__}"


class Empresa(Cliente):
   def __init__(self, rut: str, razon_social: str):
      super().__init__(rut)
      self.__razon_social = razon_social
      self.__giro = ""
      self.direccion_comercial = ""
      self.__representante_legal = ""

   #GETTER-----
   @property
   def razon_social(self):
      return self.__razon_social

   @property
   def giro(self):
      return self.__giro

   @property
   def representante_legal(self):
      return self.__representante_legal

   #SETTER----
   @giro.setter
   def correo(self, giro: str):
      self.__giro = giro

   @representante_legal.setter
   def correo(self, rp: str):
      self.__representante_legal = rp


#CLASE PERSONA-----------------------------------------------------------------------------------
class Persona(Cliente):
   def __init__(self, rut: str, nombre: str):
      super().__init__(rut)
      self.__nombre = nombre
      self.direccion_particular = ""
      self.__mis_celulares = []

   #GETTER-----
   @property
   def nombre(self):
      return self.__nombre

   #SETTER----
   @nombre.setter
   def nombre(self, nombre: str):
      self.__nombre = nombre


   #Asociación simple
   def agregar_celu(self, celular: CelularPrepago):
      self.__mis_celulares.append(celular)

   def eliminar_celu(self, imei) -> bool:
      for i in range(len(self.__mis_celulares)):
         if self.__mis_celulares[i].imei == imei:
            del self.__mis_celulares[i]
            return True

      return False

#CLASE TARJETA CRÉDITO-----------------------------------------------------------------------
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