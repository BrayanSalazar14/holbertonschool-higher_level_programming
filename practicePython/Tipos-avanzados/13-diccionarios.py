
# punto = {"x": 25, "y": 50}
# print(punto["x"])
# punto["z"] = 45
# print(punto)
# if "lala" in punto:
#     print("Encontre lala", punto["lala"])

# print(punto.get("x"))
# del punto["y"]
# print(punto)
# punto["x"] = 25

# for valor in punto:
#     print(valor, punto[valor])

# for valor in punto.items():
#     print(valor)

# for llave, valor in punto.items():
#     print(llave, valor)


# Uso real de los diccionarios

usuarios = [
    {"id": 1, "nombre": "Brayan"},
    {"id": 1, "nombre": "Fer"},
    {"id": 1, "nombre": "Samuel"},
    {"id": 1, "nombre": "Jefferson"}
]

# for usuario in usuarios:
#     print(usuario["nombre"])

# Con el operador de desempaquetamiento
usuariosNombres = [usuario["nombre"] for usuario in usuarios]
print(*usuariosNombres)

print(*[usuario["nombre"] for usuario in usuarios])
