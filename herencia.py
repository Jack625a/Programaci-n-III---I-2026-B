class Judador:
    #definir el constructor (atributos de la clase)
    def __init__(self,nombre,edad,equipo,numero,nacionalidad):
        self.nombre=nombre
        self.edad=edad
        self.equipo=equipo
        self.numero=numero
        self.nacionalidad=nacionalidad
    def entrenar(self):
        print("Esta entrenando...")

#Paso 1. Crear las subclase
class JugadorFutbol(Judador):
    #Paso 2. Definir el constructor (agregar los atributos de la clase padre mas los atributos de la subclase)
    def __init__(self,nombre,edad,equipo,numero,nacionalidad,posicion,velocidad,resistencia):
        super().__init__(nombre,edad,equipo,numero,nacionalidad)
        self.posicion=posicion
        self.velocidad=velocidad
        self.resistencia=resistencia
    def patear(self):
        print("Esta pateando el balon")
    def pasarBalon(self):
        print("Esta pasando el balon")

class JugadorBasquet(Judador):
    def __init__(self,nombre,edad,equipo,numero,nacionalidad,altura,posicion,puntosAnotados):
        super().__init__(nombre,edad,equipo,numero,nacionalidad)
        self.altura=altura
        self.posicion=posicion
        self.puntosAnotados=puntosAnotados
    
    def encestar(self):
        print("encesto....")
    def botarBalon(self):
        print("botando el balon...")


#CREAR OBJETOS
jugador1=JugadorFutbol("Juan",25,"Udabol",8,"Boliviana","Delantero","Alta","Media")
jugador1.entrenar()
jugador1.patear()

jugador2=JugadorBasquet("Kevin",25,"Udabol",9,"Boliviana",1.80,"defensa",150)
jugador2.encestar()