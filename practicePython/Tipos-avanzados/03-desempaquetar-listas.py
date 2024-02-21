numeros = [1, 2, 3]

# HORRIBLE
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

# primero, segundo, tercero = numeros

# solo necesita el primer elemento
# primero, *otros = numeros

# necesito el primero y el ultimo
primero, *otros, ultimo = numeros
print(primero, ultimo)
