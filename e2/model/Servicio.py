class Servicio:
    def __init__(self, nombre, pid, estado, tipo_inicio):
        self.nombre = nombre
        self.pid = pid
        self.estado = estado
        self.tipo_inicio = tipo_inicio

    def __str__(self):
        return f"--> Nombre: {self.nombre},PID: {self.pid if self.pid != None else 'None'},Estado: {self.estado},Tipo: {self.tipo_inicio}"