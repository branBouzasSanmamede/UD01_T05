from utils.rutas import obtener_ruta
from utils.utilBran import guardar_json
from .SystemInfo import SystemInfo

class InfoManager:
    def __init__(self):
        self.info = SystemInfo()

    def mostrar_info(self):
        print(self.info)

    def guardar_info(self):
        guardar_json(self.info.to_json(), obtener_ruta())

    def recargar_info(self):
        self.info = SystemInfo()