class Usuario:
    def guardar(self):
        print("Guardando en BBDD")


class Sesion:
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):  # Funciona si recibe una lista [] --> .guardar
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Sesion()
guardar([sesion, usuario])  # ---> Polimorfismo
