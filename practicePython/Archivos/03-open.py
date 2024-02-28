from io import open

# escritura
texto = "Hola mundo!"

# W write, si no existe lo crea
# archivo = open("Archivos/hola-mundo.txt", "w")
# archivo.write(texto)
# archivo.close()

# lectura
# archivo = open("Archivos/hola-mundo.txt", "r")
# texto = archivo.read()
# archivo.close()
# print(texto)

# # lectura como lista
# archivo = open("Archivos/hola-mundo.txt", "r")
# texto = archivo.readlines()
# archivo.close()
# print(texto)

# With y seek
# with open("Archivos/hola-mundo.txt", "r") as archivo:
#     print(archivo.readlines())
#     archivo.seek(0)
#     for linea in archivo:
#         print(linea)

# # Agregar
# archivo = open("Archivos/hola-mundo.txt", "a+")
# archivo.write("Chao mundo")
# archivo.close()

# Lectura y escritura
with open("Archivos/hola-mundo.txt", "r+") as archivo:
    texto = archivo.readlines()
    archivo.seek(0)
    texto[0] = "Chanchito feliz"
    archivo.writelines(texto)
