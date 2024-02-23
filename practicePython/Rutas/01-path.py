from pathlib import Path

# Path(r"C:\Archivos de Programa\Minecraft")
# Path("/usr/bin")  # Linux, Mac, ruta absoluta
# Path()  # Nos crea ruta donde nos encontremos
# Path.home()  # Crea ruta en la carpeta home
# # Ruta relativa --->Archivo de programa ---> AP/one/__init__py
# Path("one/_init_.py")

path = Path("hola-mundo/mi-archivo.py")
path.is_file()
path.is_dir()
path.exists()

print(
    path.name,
    path.stem,
    path.suffix,
    path.absolute()
)
p = path.with_name("chanchito.py")
print(p)

p = path.with_suffix(".png")
print(p)

p = path.with_stem("Feliz")
print(p)
