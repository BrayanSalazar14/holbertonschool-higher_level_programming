# and, or, not

gas = False
encendido = True
edad = 18

# if gas and (encendido or edad > 17):
#   print("Puedes avanzar")

# if gas and encendido:
#     print("Puedes avanzar")

# if gas or encendido:
#     print("Puedes avanzar")

# if not gas or encendido:
#     print("Puedes avanzar")

# Operaciones de corto circuito
if not gas or encendido or edad > 17:
    print("Puedes avanzar")
