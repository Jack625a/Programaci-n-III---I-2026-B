class Animal:
    def __init__(self,color,especie,tamaño):
        self.color=color
        self.especie=especie
        self.tamaño=tamaño
    def hacerSonido(self):
        print("Esta haciendo un sonido...")

class Perro(Animal):
    def __init__(self,color,especie,tamaño,nombre):
        super().__init__(color,especie,tamaño)
        self.nombre=nombre
    def hacerSonido(self):
        print("Esta ladrando") 

perro=Perro("Blanco","Perro","mediano","Juanito")
perro.hacerSonido()