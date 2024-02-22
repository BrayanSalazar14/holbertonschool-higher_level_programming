# from usuarios.acciones import guardar, pagar_impuestos
# PROHIBIDO from usuario_impuesto import *

# guardar()
# pagar_impuestos()

# Otra forma de importar, no tan recomendable como la anterior
# import usuarios.acciones
# usuarios.acciones.guardar()

# Otra forma de importar
# from usuarios import acciones
# acciones.guardar()
# acciones.pagar_impuestos()

# # SUB-PAQUETES
# from usuarios.acciones.utilidades import guardar, pagar_impuestos
# guardar()
# pagar_impuestos()

from usuarios.impuestos.utilidades import pagar_impuestos
# import usuarios
pagar_impuestos()
# print(usuarios.gestion.__name__)
# print(usuarios.impuestos.__package__)
# print(usuarios.gestion.__path__)
# print(usuarios.impuestos.__file__)
