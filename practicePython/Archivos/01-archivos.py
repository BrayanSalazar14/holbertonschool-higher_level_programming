from pathlib import Path
from time import ctime
archivo = Path("Archivos/archivo-prueba.txt")
# archivo.exists()
# archivo.rename()
# archivo.unlink()
# print(archivo.stat())
# TimesTamp --> Fecha del archivo con respecto al 01/01/1970, UNIX
# print("acceso", archivo.stat().st_atime)
print("acceso", ctime(archivo.stat().st_atime))
print("creación", ctime(archivo.stat().st_ctime))
print("modificación", ctime(archivo.stat().st_mtime))
