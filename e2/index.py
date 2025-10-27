from utils.utilBran import ejecutar_menu
from e2.model.ServicioManager import ServicioManager

manager = ServicioManager()

menu = [
    (1, "Mostrar todos los servicios", manager.mostrar_servicios),
    (2, "Mostrar servicios filtrados", manager.mostrar_filtrados),
    (3, "Mostrar descripción de un servicio", manager.mostrar_desc)
]

def main():
    ejecutar_menu(menu)

if __name__ == "__main__":
    main()