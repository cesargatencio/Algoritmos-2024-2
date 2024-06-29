class Cliente:
    def __init__(self, nombre, cedula, edad):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.gasto_restaurante = 0

    def __str__(self):
        return f"{self.nombre}, {self.cedula}, {self.edad}, {self.gasto_restaurante}"
