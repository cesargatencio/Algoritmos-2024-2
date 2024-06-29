import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter

class GestionEstadisticas:
    def __init__(self, gestion_datos):
        self.gestion_datos = gestion_datos

    def promedio_gasto_vip(self, partidos):
        total_gasto = 0
        num_vips = 0

        for partido in partidos:
            for entrada in partido.entradas:
                if entrada.tipo == 'VIP':
                    total_gasto += entrada.precio + sum(producto.precio for producto in entrada.productos_comprados)
                    num_vips += 1

        if num_vips == 0:
            return 0

        return total_gasto / num_vips

    def tabla_asistencia_partidos(self,partidos):
        data = []
        p_ordenado=sorted(partidos,key=lambda x: len(x.entradas),reverse=True)
        for partido in p_ordenado:
            boletos_vendidos = len(partido.entradas)
            personas_asistieron = sum(1 for entrada in partido.entradas if entrada.asistio)
            relacion_asistencia_venta = personas_asistieron / boletos_vendidos if boletos_vendidos else 0
            data.append([
                f"{partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre}",
                partido.estadio.nombre,
                boletos_vendidos,
                personas_asistieron,
                relacion_asistencia_venta
            ])

        df = pd.DataFrame(data, columns=['Partido', 'Estadio', 'Boletos Vendidos', 'Asistencia', 'Relación Asistencia/Venta'],index=range(1,len(data)+1))
        
        
        return df

    def partido_mayor_asistencia(self,partidos):
        partido_max_asistencia = None
        max_asistencia = 0

        for partido in partidos:
            personas_asistieron = sum(1 for entrada in partido.entradas if entrada.asistio)
            if personas_asistieron > max_asistencia:
                max_asistencia = personas_asistieron
                partido_max_asistencia = partido

        return partido_max_asistencia

    def partido_mayor_boletos_vendidos(self,partidos):
        partido_max_boletos = None
        max_boletos = 0

        for partido in partidos:
            boletos_vendidos = len(partido.entradas)
            if boletos_vendidos > max_boletos:
                max_boletos = boletos_vendidos
                partido_max_boletos = partido

        return partido_max_boletos

    def top_productos_mas_vendidos(self,partidos):
        counter = Counter()

        for partido in partidos:
            for entrada in partido.entradas:
                for producto in entrada.productos_comprados:
                    counter[producto.nombre] += 1

        return counter.most_common(3)

    def top_clientes(self,partidos):
        counter = Counter()

        for partido in partidos:
            for entrada in partido.entradas:
                counter[entrada.cliente.nombre] += 1

        return counter.most_common(3)

    