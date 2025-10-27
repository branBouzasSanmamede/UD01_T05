import psutil
import time

class ProcesoManager:

    def mostrar_procesos(self, procesos, campos=None):
        if campos is None:
            campos = ['pid', 'name', 'username']
        for p in procesos:
            try:
                info = p.info
                linea = ", ".join(
                    f"{c.capitalize()}: {info[c] if info[c] is not None else 'N/A'}"
                    if not isinstance(info[c], float)
                    else f"{c.capitalize()}: {info[c]:.2f}"
                    for c in campos
                )
                print(linea)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    def obtener_porcentaje(self, tipo_porcentaje="memoria"):
        while True:
            try:
                return float(input(f"Introduce el porcentaje mínimo de {tipo_porcentaje} (%): "))
            except ValueError:
                print("❌ Valor no válido.")

    def obtener_pid(self):
        while True:
            try:
                pid = int(input("Introduce el PID del proceso raíz: "))
                return psutil.Process(pid)
            except (ValueError, psutil.NoSuchProcess):
                print("❌ PID no válido o proceso no existe.")

    def obtener_todos(self):
        self.mostrar_procesos(psutil.process_iter(['pid', 'name', 'username']))

    def filtrar_memoria(self):
        porcentaje_min = self.obtener_porcentaje()
        self.mostrar_procesos((p for p in psutil.process_iter(['pid', 'name', 'memory_percent']) if p.info['memory_percent'] > porcentaje_min), ['pid', 'name', 'memory_percent'])
            
    def filtrar_cpu(self):
        porcentaje_min = self.obtener_porcentaje()
        
        for p in psutil.process_iter(['pid', 'name']):
            try:
                p.cpu_percent(None)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        time.sleep(0.5)
        procesos_filtrados = []
        for p in psutil.process_iter(['pid', 'name']):
            try:
                cpu = p.cpu_percent(None)
                if cpu > porcentaje_min:
                    p.info['cpu_percent'] = cpu
                    procesos_filtrados.append(p)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

        self.mostrar_procesos(procesos_filtrados, ['pid', 'name', 'cpu_percent'])
        
    def arbol_procesos(self):
        def imprimir_recursivo(proceso, nivel=0):
            try:
                print("└" + "-" * nivel + f"PID: {proceso.pid}, Nombre: {proceso.name()}")
                for hijo in proceso.children():
                    imprimir_recursivo(hijo, nivel + 1)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                return
        imprimir_recursivo(self.obtener_pid())