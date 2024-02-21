primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

# Union {1, 2, 3, 4, 5}
print(primer | segundo)
# Intersección {3, 4} --> Que se encuentre en los dos conjuntos
print(primer & segundo)
# Diferencia quita los elementos al primer set que se encuentren en el segundo {1, 2}
print(primer - segundo)
# Diferencia simetrica {1, 2, 5}
print(primer ^ segundo)

print("Soy Cristian")
