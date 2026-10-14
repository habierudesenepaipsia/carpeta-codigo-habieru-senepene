class Animal:
    def hablar(self):
        print("El animal hace un sonido.")

class Perro(Animal):
    def hablar(self):
        print("El perro dice: Guau!")

class Gato(Animal):
    def hablar(self):
        print("El gato dice: Miau!")


#Uso
animales = [Perro(), Gato(), Animal()]

for animal in animales:
    animal.hablar()




###TUPLA###

