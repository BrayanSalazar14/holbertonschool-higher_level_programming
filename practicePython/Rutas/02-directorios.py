from pathlib import Path
path = Path("Rutas")
# path.exist()
# path.mkdir()
# path.rmdir()
# path.rename("Chanchito-feliz")

archivos = [p for p in path.iterdir() if not p.is_dir()]
print(archivos)
archivos = [p for p in path.glob("*.py")]
print(archivos)
archivos = [p for p in path.glob("**/*.py")]
print(archivos)
archivos = [p for p in path.rglob("*.py")]
print(archivos)
