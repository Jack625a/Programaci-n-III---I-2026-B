class Persona:
    def __init__(self,nombre,ci,genero,edad,fechaNacimiento):
        self.nombre=nombre
        self.ci=ci
        self.genero=genero
        self.edad=edad
        self.fechaNacimiento=fechaNacimiento
    
    #Definir las acciones
    def comer(self,comida):
        print(self.nombre, " Esta comiendo ",comida)
    
    def dormir(self):
        print(self.nombre, " esta durmiendo...")

class Estudiante(Persona):
    def __init__(self,nombre,ci,genero,edad,fechaNacimiento,codEstudiante,carrera,semestre):
        super().__init__(nombre,ci,genero,edad,fechaNacimiento)
        self.codEstudiante=codEstudiante
        self.carrera=carrera
        self.semestre=semestre
    
    def estudiar(self):
        print(self.nombre, " esta estudiando...")
    def rendirExamen(self):
        print(self.nombre, " esta dando su examen...")

estudiante1=Estudiante("Kevin Arroyo",452137,"Masculino",30,"15/12/1995",7451,"Ingenieria de Sistemas",3)
estudiante1.comer("Pan")
estudiante1.rendirExamen()
estudiante1.dormir()
estudiante1.estudiar()
