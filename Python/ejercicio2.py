import shutil

from pathlib import Path
print(Path("nuevo1.txt").exists())
print(Path("nuevo2.0.txt").exists())

print(Path("darian.txt").read_text())
print(Path("darian.txt").absolute())

p=Path("darian.txt")
print(p.stem)
print(p.suffix)

p=Path("/Users\Estudiante\Desktop\Python\darian.txt")
print(p.name)

Path("6/7/8").mkdir(parents=True, exist_ok=True)

shutil.rmtree(Path("6"))