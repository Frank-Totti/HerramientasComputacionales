"""
Elaborar un algoritmo para calcular el área de un triangulo cuya altura es de 30 cm y la base de 50
cm. Realizar una versión genérica de este algoritmo para calcular el area de un triangulo dada una
altura y una base cualquiera, ¿Qué cambio se debe hacer?
"""

### Modelo determinado ###

h = 30
b = 50

calcularArea = (h * b)//2

print(str(calcularArea)+"cm")

### Modelo Generico ###

def recibirParametros(h,b):

    calcularArea = (h * b)/2

    return calcularArea

def leerImprimir():
    altura = int(input("Ingrese valor para la altura del triángulo "))
    base = int(input("Ingese valor para la base del triángulo "))
    recibirParametros(altura,base)

#leerImprimir()

"""
Elaborar un algoritmo para calcular la nota final de un curso con la siguiente distribución de
evaluaciones: 2 parciales (25% cada uno), taller (20%) y proyecto (30%)
"""

# l1 = notas de los parciales
# l2 = nota del taller
# l3 = proyecto


def obtenerNotasCurso(l1,l2,l3,l4):

    cal = (l1 * 0.25) + (l2 * 0.25) + (l3 * 0.2) + (l4 * 0.3)
    return print("Su nota final de curso es " + str(cal))

def leerImprimirNota():
    gam = float(input("Ingrese nota del parcial uno  "))
    gom = float(input("Ingrese nota del parcial dos  "))
    tal = float(input("Ingrese nota del taller  "))
    proc = float(input("Ingrese nota del proyecto  "))
    obtenerNotasCurso(gam,gom,tal,proc)
    
#leerImprimirNota()


"""
Elaborar un algoritmo que realice la transformación de grados Celsius a Fahrenheit
"""
# v1 = valor de temperatura en grados Celcius

def celciusFaren(v1):

    fah = (1.8 * (v1))+32

    return print(fah)

def leerImprimircambio():
    com = float(input("Ingrese valor de la temperatura en Celcius "))
    celciusFaren(com)

leerImprimircambio()
























