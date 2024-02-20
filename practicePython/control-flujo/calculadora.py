print("Bienvenidos a la calculadora")
input_user = print("Para salir escribe: \"Salir\" \n")
print("Las operaciones son:\nSuma\nResta\nMultiplicación\nDivisión")
result = ""
while True:
    if not result:
        result = input("Ingrese número: ")
        if result.lower() == "salir":
            break
        result = int(result)
    op = input("Ingresa la operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        result += n2
        print(f"El resultado es {result}")
    elif op.lower() == "resta":
        result -= n2
        print(f"El resultado es {result}")
    elif op.lower() == "multiplicacion":
        result *= n2
        print(f"El resultado es {result}")
    elif op.lower() == "division":
        result /= n2
        print(f"El resultado es {result}")
    else:
        print("No valido")
        break
