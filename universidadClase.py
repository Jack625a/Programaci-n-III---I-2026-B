#Paso 1. Definir la clase
class Universidad:
    #Paso 2. definir los atributos de la clase
    def __init__(self,nombre,ciudad,carreras,tipo,rector):
        self.nombre=nombre
        self.ciudad=ciudad
        self.carreras=carreras
        self.tipo=tipo
        self.rector=rector
    #Paso 3. Definir las acciones
    def matricularAlumnos(self,codEstudiante):
        registrar="Registrado"
        return registrar,codEstudiante
    def registrarCarrera(self,nombreCarrera):
        return nombreCarrera
    def graduarEstudiantes(self,actaNotas):
        if actaNotas=="Completo":
            print("GRADUADO")
        else:
            print("DEBE COMPLETAR SUS MATERIAS")

#Paso 4.Crear los objetos de la clase
udabol=Universidad("Udabol","Oruro","Derecho,Medicina,Ingenieria de Sistemas","privado","Marcelo")
udabol.registrarCarrera("Robotica")
udabol.matricularAlumnos(745188)
udabol.graduarEstudiantes("Completo")
