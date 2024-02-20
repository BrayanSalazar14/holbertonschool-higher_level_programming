def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(1, 2, 3, 4)
suma(4, 5)
suma(5, 7, 8, 9)
