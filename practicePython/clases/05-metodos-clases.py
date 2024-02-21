class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("Guau!")

    @classmethod
    def factory(cls):
        return cls("Kycer", 4)


perro1 = Perro("Kycer", 2)
perro2 = Perro("Morocho", 8)
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)
