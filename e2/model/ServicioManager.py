import wmi
from .Servicio import Servicio

class ServicioManager:
    def __init__(self):
        self.c = wmi.WMI()
        self.servicios = self.cargar_servicios()

    def cargar_servicios(self):
        servicios = []
        for servicio in self.c.Win32_Service():
            servicios.append(Servicio(servicio.Name, servicio.ProcessId if servicio.ProcessId != 0 else None, servicio.State, servicio.StartMode))
        return servicios
    
    def mostrar_servicios(self):
        print(*[s for s in self.servicios], sep="\n")

    def obtener_filtro(self):
        return input("Introduce el filtro: ")

    def mostrar_filtrados(self):

        while True:
            partes = self.obtener_filtro().strip().lower().split()

            partesLen = len(partes)

            if partesLen < 1 or partesLen > 2:
                print("Ingresa una o dos palabras separadas por espacio!")
                continue
            
            tipo = None
            estado = None

            if partesLen >= 1:
                if partes[0] == "iniciado":
                    estado = "Running"
                elif partes[0] == "parado":
                    estado = "Stopped"
                else:
                    print("1ª Palabra: Ingresa iniciado o parado!")
                    continue

            if partesLen == 2:
                if partes[1] == "manual":
                    tipo = "Manual"
                elif partes[1] == "auto":
                    tipo = "Auto"
                else:
                    print("2ª Palabra: Ingresa manual o auto!")
                    continue

            break
                    
        print(*[s for s in self.servicios if s.estado == estado and (tipo is None or s.tipo_inicio == tipo)], sep="\n")

    def mostrar_desc(self):
        print("To Do")
