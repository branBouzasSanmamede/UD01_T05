from utils.utilBran import ejecutar_menu
from controller.controller import mostrar_info
from controller.controller import guardar_info

menu_principal = [
    (1, "Mostrar información del sistema", mostrar_info),
    (2, "Guardar información del sistema", guardar_info)
]

def main():
    ejecutar_menu(menu_principal)

if __name__ == "__main__":
    main()