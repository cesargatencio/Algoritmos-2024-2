class Estadio:
    def __init__(self, id ,nombre: str, ubicacion: str, restaurantes: list, capacidad: list):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.restaurantes = restaurantes
        self.capacidad = capacidad
        self.mapa_estadios= {}

    def __str__(self):
     
        return f"{self.id}, {self.nombre}, {self.ubicacion}, {self.restaurantes.__str__()}, {self.capacidad}"

