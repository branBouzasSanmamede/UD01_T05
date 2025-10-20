from utils.utilBran import guardar_json
from utils.rutas import obtener_ruta
from model.SystemInfo import SystemInfo

info = SystemInfo()

def mostrar_info():
    print(info)

def guardar_info():
    guardar_json(info.to_json(), obtener_ruta())