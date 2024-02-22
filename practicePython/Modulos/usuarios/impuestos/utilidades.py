if __name__ != "__ main":
    # ---> import relativo
    from ..gestion.crud import guardar
    # ---> import absoluto
    from usuarios.gestion.crud import guardar

    print(__name__)

    def pagar_impuestos():
        print("Pagar impuestos")
        guardar()

if __name__ == "__ main":
    print("Tarea de mantenimiento")
