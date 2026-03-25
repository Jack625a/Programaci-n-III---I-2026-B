class JudadorFutbol:
    def __init__(self,nombre,edad,posicion,numero,equipo):
        self.nombre=nombre
        self.edad=edad
        self.posicion=posicion
        self.numero=numero
        self.equipo=equipo
    
    def correr(self):
        print("El jugador esta corriendo")
    def patear(self):
        print("El jugador pateo el balon")
    def entrenar(self):
        print("El jugador esta entrenando")

jugador1=JudadorFutbol("Juanito Quispe",15,"Delantero",69,"Real Barcelona")
jugador1.entrenar()
    
