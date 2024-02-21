usuarios = [["Chanchito", 4], ["Brayan", 1], ["Fer", 2]]

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)
# Mismo
# nombres = [usuario[0] for usuario in usuarios]

# Filtrar
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)
