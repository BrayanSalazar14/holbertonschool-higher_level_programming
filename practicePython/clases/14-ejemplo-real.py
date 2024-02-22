class Model():
    tabla = False

    def __init__(self):
        if not self.tabla:
            print("Error, tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id}, en la tabla de {self.tabla}")


class Usuario(Model):
    tabla = "Usuarios"


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(23)
