import os 
import shutil

print (os.listdir("."))


print(os.path.exists("nuevo.txt"))
print(os.path.exists("nue.txt"))


with open("paka.txt","r") as f:
    print(f.read())

print(os.path.abspath("paka.txt"))
print(os.path.splitext("paka.txt"))

print(os.path.basename("/Users\Estudiante\Desktop\Python\paka.txt"))

os.makedirs("1/2/3", exist_ok=True)

shutil.rmtree("1")