# # lista = [1, 2, 3] --> Forma de crear lista
# lista = list([1, 2, 3]) ---> Forma de crear lista,
# lista.append(4) agregar un elemento al final de la lista
# lista.insert(0, 0) agregar elem al inicio de la lista
# print(lista) = [0, 1, 2, 3, 4]

# MEJOR FORMA, CODIGO UN POCO MAS INTUITIVO, EXTENDER TIPOS NATIVOS
class Lista(list):
    def prepend(self, item):  # Prepend: Agrega elementos al inicio
        self.insert(0, item)


lista = Lista([1, 2, 3])
lista.append(4)
lista.prepend(0)
print(lista)
