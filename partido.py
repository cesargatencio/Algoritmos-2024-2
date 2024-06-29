from entrada import Entrada

class Partido:
    def __init__(self, equipo_local, equipo_visitante, fecha, estadio):
        self.equipo_local = equipo_local
        self.equipo_visitante = equipo_visitante
        self.fecha = fecha
        self.estadio = estadio
        self.entradas = []
        self.asistencia = 0
        self.numero_partido = None

    def registrar_entrada(self, entrada):
        self.entradas.append(entrada)

    def __str__(self):
        
        return f"{self.equipo_local}, {self.equipo_visitante}, {self.fecha}, {self.estadio}, {self.entradas}, {self.asistencia}, {self.numero_partido}"

