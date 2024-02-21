numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
menos_numeros = numeros[:2]
print(menos_numeros)
print(punto)
primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)

# numeros[0] = 5 ---> No son mutables, no se pueden modificar
# Solo si
listaNumeros = list(numeros)
listaNumeros[0] = 10

for n in listaNumeros:
    print(n)
