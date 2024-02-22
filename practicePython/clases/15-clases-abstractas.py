from abc import ABC, abstractmethod


class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id}, en la tabla de {self.tabla}")


class Usuario(Model):
    tabla = "Usuarios"

    def guardar(self):
        print("Guardando usuarios")


usuario = Usuario()
usuario.guardar()
Usuario.buscar_por_id(23)
