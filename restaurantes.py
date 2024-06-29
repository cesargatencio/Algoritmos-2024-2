from producto import Producto


class Restaurante:
    def __init__(self, nombre: str, productos: list):
        self.nombre = nombre
        self.productos = productos
        

    def __str__(self):
        
        return f"{self.nombre}, {self.productos}"
