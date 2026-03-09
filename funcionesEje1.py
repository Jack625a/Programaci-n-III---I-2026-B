#Crear una funcion para una calculadora simple
def calculadora(x,y):
    suma=x+y
    resta=x-y
    multiplicacion=x*y
    division=x/y
    return suma,resta,multiplicacion,division

print(calculadora(5,6))