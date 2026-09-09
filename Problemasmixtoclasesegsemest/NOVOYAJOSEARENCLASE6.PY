class Casa:
    def __init__(self, precio, metrosCuadrados, direccion):
        self.__precio = int
        self.__metrosCuadrados = float
        self.__direccion = "elpepeetesech"




####PERO ESTA WEA ES COMO UN REPASO NO_?
# 
#
        

####WEA DEL PROFE####


class Casa:

   def __init__(self, direccion: str, mt2: float, precio: int):
      self.__direccion = direccion
      self.__mt2 = mt2
      self.__precio = precio


   #Get
   @property
   def direccion(self):
      return self.__direccion

   @property
   def precio(self):
      return "$" + str(self.__precio)
      







casa_abdala = Casa("ate.barroso", 20.5, 100000)
casa_dario = Casa("pje.Uno", 100, 3000000)

print(f"La casa de abdala tiene la dirección {casa_abdala.direccion}, y el precio es {casa_abdala.precio}")
print(f"La casa de dario tiene la dirección {casa_dario.direccion}, y el precio es {casa_dario.precio}")

#casa_abdala.precio = -5000000
print(f"Se modifica el precio de la casa de abdala a {casa_abdala.precio}")class Casa:

   def __init__(self, direccion: str, mt2: float, precio: int):
      self.__direccion = direccion
      self.__mt2 = mt2
      self.__precio = precio


   #Get
   @property
   def direccion(self):
      return self.__direccion

   @property
   def precio(self):
      return "$" + str(self.__precio)
      







casa_abdala = Casa("ate.barroso", 20.5, 100000)
casa_dario = Casa("pje.Uno", 100, 3000000)

print(f"La casa de abdala tiene la dirección {casa_abdala.direccion}, y el precio es {casa_abdala.precio}")
print(f"La casa de dario tiene la dirección {casa_dario.direccion}, y el precio es {casa_dario.precio}")

#casa_abdala.precio = -5000000
print(f"Se modifica el precio de la casa de abdala a {casa_abdala.precio}")