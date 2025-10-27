from e3.model.ProcesoManager import ProcesoManager
from utils.utilBran import ejecutar_menu

manager = ProcesoManager()

menu = [
    (1, "Mostrar todos los procesos", manager.obtener_todos),
    (2, "Procesos por memoria", manager.filtrar_memoria),
    (3, "Procesos por CPU", manager.filtrar_cpu),
    (4, "Arbol de procesos", manager.arbol_procesos)
]

def main():
    ejecutar_menu(menu)

if __name__ == "__main__":
    main()