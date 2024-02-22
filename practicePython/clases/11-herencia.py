class Animal:
    def comer(self):
        print("Comiendo")


class Perro(Animal):
    def pasear(self):
        print("Paseando")


perro = Perro()
perro.comer()


class Chanchito(Perro):
    def programar(self):
        print("Programando")


chanchito = Chanchito()
chanchito.comer()
