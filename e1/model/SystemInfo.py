import platform, psutil

class SystemInfo:
    def __init__(self):
        self.plataforma = platform.system()
        self.cpus = self._get_cpu_info()
        self.memoria = self._get_mem_info()
        self.discos = self._get_disk_info()
        self.disco_io = self._get_disk_io()
        self.red = self._get_net_info()

    def _get_cpu_info(self):
        info = {}
        info['numero'] = psutil.cpu_count(logical=True)
        freq = psutil.cpu_freq()
        info['frecuencias_mhz'] = [freq.current] * info['numero'] if freq else None
        info['uso_por_cpu'] = psutil.cpu_percent(percpu=True, interval=1)
        return info

    def _get_mem_info(self):
        mem = psutil.virtual_memory()
        return {
            'total_bytes': mem.total,
            'disponible_bytes': mem.available,
            'porcentaje_usado': mem.percent
        }

    def _get_disk_info(self):
        discos = []
        for part in psutil.disk_partitions():
            try:
                uso = psutil.disk_usage(part.mountpoint)
                discos.append({
                    'dispositivo': part.device,
                    'punto_montaje': part.mountpoint,
                    'total_bytes': uso.total,
                    'usado_bytes': uso.used,
                    'libre_bytes': uso.free,
                    'porcentaje_usado': uso.percent
                })
            except PermissionError:
                discos.append({
                    'dispositivo': part.device,
                    'punto_montaje': part.mountpoint,
                    'error': 'Permiso denegado'
                })
        return discos

    def _get_disk_io(self):
        dio = psutil.disk_io_counters()
        return {
            'operaciones_lectura': dio.read_count,
            'operaciones_escritura': dio.write_count,
            'bytes_leidos': dio.read_bytes,
            'bytes_escritos': dio.write_bytes
        }

    def _get_net_info(self):
        net = psutil.net_io_counters()
        return {
            'bytes_enviados': net.bytes_sent,
            'bytes_recibidos': net.bytes_recv,
            'paquetes_enviados': net.packets_sent,
            'paquetes_recibidos': net.packets_recv
        }

    def __str__(self):
        s = []
        s.append(f"- Plataforma: {self.plataforma}\n")

        s.append("- Información de CPUs:")
        s.append(f"  · Número de CPUs: {self.cpus['numero']}")
        if self.cpus['frecuencias_mhz']:
            for i, f in enumerate(self.cpus['frecuencias_mhz']):
                s.append(f"  --> Frecuencia CPU {i}: {f:.2f} MHz")
        else:
            s.append("  · Frecuencia no disponible")
        s.append("  · Uso de CPU por núcleo:")
        for i, uso in enumerate(self.cpus['uso_por_cpu']):
            s.append(f"    --> CPU {i}: {uso}%")
        s.append("")

        s.append("- Información de memoria:")
        s.append(f"  · Memoria total: {self.memoria['total_bytes'] / (1024**3):.2f} GB")
        s.append(f"  · Memoria disponible: {self.memoria['disponible_bytes'] / (1024**3):.2f} GB")
        s.append(f"  · Porcentaje usado: {self.memoria['porcentaje_usado']}%\n")

        s.append("- Información de discos:")
        for d in self.discos:
            if 'error' in d:
                s.append(f"  · No se pudo acceder a {d['dispositivo']} ({d['punto_montaje']}): {d['error']}")
            else:
                s.append(f"  · {d['dispositivo']} ({d['punto_montaje']}):")
                s.append(f"      --> Total: {d['total_bytes'] / (1024**3):.2f} GB")
                s.append(f"      --> Usado: {d['usado_bytes'] / (1024**3):.2f} GB")
                s.append(f"      --> Libre: {d['libre_bytes'] / (1024**3):.2f} GB")
                s.append(f"      --> Porcentaje: {d['porcentaje_usado']}%")
        s.append("")
        dio = self.disco_io
        s.append(f"  · Operaciones de lectura: {dio['operaciones_lectura']}")
        s.append(f"  · Operaciones de escritura: {dio['operaciones_escritura']}")
        s.append(f"  · Bytes leídos: {dio['bytes_leidos'] / (1024**2):.2f} MB")
        s.append(f"  · Bytes escritos: {dio['bytes_escritos'] / (1024**2):.2f} MB\n")

        s.append("- Estadísticas de red:")
        r = self.red
        s.append(f"  · Bytes enviados: {r['bytes_enviados'] / (1024**2):.2f} MB")
        s.append(f"  · Bytes recibidos: {r['bytes_recibidos'] / (1024**2):.2f} MB")
        s.append(f"  · Paquetes enviados: {r['paquetes_enviados']}")
        s.append(f"  · Paquetes recibidos: {r['paquetes_recibidos']}")

        return "\n".join(s)
    
    def to_json(self):
        return {
            'plataforma': self.plataforma,
            'cpus': self.cpus,
            'memoria': self.memoria,
            'discos': self.discos,
            'disco_io': self.disco_io,
            'red': self.red
        }