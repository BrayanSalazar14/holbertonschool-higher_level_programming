usuarios = [["Chanchito", 4], ["Brayan", 1], ["Fer", 2]]


# nombres = list(map(lambda usuario: usuario[0], usuarios))
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
