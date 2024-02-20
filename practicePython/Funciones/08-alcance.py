# Ambito Global --- MALA PRACTICAAAAAAA!--- NO USAR
saludo = "Hola Global"

"""SI UTILIZAS AMBITO GLOBAL
def saludar():
    global saludo
    saludo = "Hola Mundo"
"""


def saludar():
    # Ambito Local
    saludo = "Hola Mundo"


def saludaChanchito():
    # Ambito Local
    saludo = "Hola Chanchito"
    print(saludo)


saludar()
print(saludo)
