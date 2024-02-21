def eliminarEspacios(texto):
    return [chars for chars in texto if chars != " "]


def countDiccionary(lista):
    chars_diccionary = {}
    for chars in lista:
        if chars in chars_diccionary:
            chars_diccionary[chars] += 1
        else:
            chars_diccionary[chars] = 1
    return chars_diccionary


def ordenarDiccionario(diccionario):
    return sorted(
        diccionario.items(),
        key=lambda key: key[1],
        reverse=True
    )


def mayores_tuplas(diccionario):
    maximo = diccionario[0][1]
    respuesta = {}
    for orden in diccionario:
        if maximo > orden[1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta


def crear_mensaje(diccionario):
    mensaje = "Los que mas se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con valor {valor} repeticiones \n"
    return mensaje


string = "Hola mundo este es mi string"
string = eliminarEspacios(string)
newDiccionary = countDiccionary(string)
newDiccionary = ordenarDiccionario(newDiccionary)
mayores = mayores_tuplas(newDiccionary)
mensaje1 = crear_mensaje(mayores)
print(string)
print("----")
print(newDiccionary)
print("----")
print(mayores)
print("----")
print(mensaje1)
