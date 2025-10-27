from utils.utilBran import ejecutar_menu
from e1.model.InfoManager import InfoManager

manager = InfoManager()

menu = [
    (1, "Mostrar información del sistema", manager.mostrar_info),
    (2, "Guardar información del sistema", manager.guardar_info),
    (3, "Recargar información", manager.recargar_info)
]

def main():
    ejecutar_menu(menu)

if __name__ == "__main__":
    main()