numeros = [2, 4, 1, 45, 75, 22]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros)  # Reversa sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

# usuarios = [[4, "Chanchito"], [1, "Brayan"], [2, "Fer"]]
# usuarios.sort()

usuarios = [["Chanchito", 4], ["Brayan", 1], ["Fer", 2]]


def ordena(elemento):
    return elemento[1]


usuarios.sort(key=ordena)  # usuarios.sort(key=ordena, reverse=True)
print(usuarios)
