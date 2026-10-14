class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        

    def hablar(self):
        print(f"{self.nombre} dijo algo...")

class Emilito(Persona):
    def __init__(self, nombre, apellido, edad, rut, altura):
        super().__init__(nombre)
        self.apellido = apellido
        self.edad = edad
        self.rut = rut
        self.altura = altura
    def hablar(self):    
        print(f"{self.nombre}, de apellido {self.apellido}, tiene una edad de {self.edad} años, y un RUT terminado en {self.rut}.{self.nombre} dijo sisime guta ya, y mide {self.altura}")            

persona1 = Emilito("emilio", "gatica", 27, "K",1.86)
persona2 = Persona("emilio")        

persona1.hablar()
persona2.hablar()