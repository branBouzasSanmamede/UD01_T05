from pathlib import Path
from datetime import datetime
import platform

BASE_JSON_PATH = Path(__file__).parent.parent / 'e1' / 'json'

RUTA_SYSTEM_INFO_W = BASE_JSON_PATH / 'systemInfo_w'
RUTA_SYSTEM_INFO_L = BASE_JSON_PATH / 'systemInfo_l'

def obtener_fecha():
    return f"-{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.json"

def obtener_ruta():
    sistema = platform.system().lower()
    if sistema == "windows":
        return f"{RUTA_SYSTEM_INFO_W}{obtener_fecha()}"
    elif sistema == "linux":
        return f"{RUTA_SYSTEM_INFO_L}{obtener_fecha()}"
    else:
        raise RuntimeError(f"Sistema operativo '{sistema}' no soportado")