import json
from pathlib import Path

# Escribir JSON
# productos = [
#     {"id": 1, "name": "Surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "Skate"}
# ]

# # Volver a JSON
# data = json.dumps(productos)

# Path("Archivos/productos.json").write_text(data)


# Leer JSON
data = Path("Archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)
print(productos)


# Modificar JSON
productos[0]["name"] = "Chanchito feliz"
Path("Archivos/productos.json").write_text(json.dumps(productos))
