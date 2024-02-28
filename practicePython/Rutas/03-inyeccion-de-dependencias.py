# Ventajas de inyección de dependencias, nos permite reutilizar más el codigo
# Nos permite desacoplar nuestro codigo para que este sea mas facil de reutilizar
# Cuando realicemos test será mas sencillo

# def init_app(bbdd, api):
#     #inicialización de modulo
#     #Flask
from pathlib import Path
path = Path()
paths = [p for p in path.iterdir() if p.is_dir()]

dependencias = {
    "db": "base de datos",
    "api": "esta es la api",
    "graphql": "esto es graphql"
}


def load(p):
    # __import__ --> importa paquetes de manera dinamica
    paquete = __import__(str(p).replace("/", "."))
    try:
        paquete.init(**dependencias)
    except:
        print("El paquete no tiene función init")


list(map(load, paths))
