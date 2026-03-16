#PASO 1. DEFINIR LA CLASE
class Persona:
    #PASO 2. Definir el constructor para los atributos
    def __init__(self,ci,nombre,edad,genero,estatura,peso):
        self.ci=ci
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.estatura=estatura
        self.peso=peso
    #PASO 3. DEFINIR LAS ACCIONES DE LA CLASE
    def comer(comida):
        print(" Esta comiendo ",comida)
    def dormir():
        print(" Esta durmiendo")

#Paso 4. Creacion de los objetos de la clase
persona1=Persona(1245157,"Kevin Arroyo",29,"Masculino",1.76,65)
persona2=Persona(5416545,"Juan",25,"Masculino",1.80,80)
persona3=Persona(741554,"Maria",22,"Femenino",1.65,50)

persona1.comer("Pan")
persona2.comer("Hamburguesa")
persona3.dormir()
persona3.comer()