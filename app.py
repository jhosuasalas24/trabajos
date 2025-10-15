import os
import shutil
from datetime import datetime

fecha = datetime.now().strftime("%Y-%m-%d")
nueva_carpeta = f"{fecha}_Archivos"

if not os.path.exists(nueva_carpeta):
    os.makedirs(nueva_carpeta)
    print(f"Carpeta '{nueva_carpeta}' creada.")

carpeta_origen = "C:\\Users\\AMD\\Desktop\\sexto ciclo"

contador = 0

for archivo in os.listdir(carpeta_origen):
    origen = os.path.join(carpeta_origen, archivo)
    destino = os.path.join(nueva_carpeta, archivo)
    shutil.move(origen, destino)
    contador += 1

print(f"{contador} archivos movidos a '{nueva_carpeta}'.")