class Producto:
    def __init__(self, name , quantity, price: float, stock: int, adicional):
        self.nombre = name
        self.cantidad = quantity
        self.precio = price
        self.stock = stock
        self.adicional = adicional
        self.alcoholic = False
        self.clasificacion = self.clasificar_adicional()

    def clasificar_adicional(self):
        
        if self.adicional == "plate":
            return "Alimento"
        elif self.adicional == "non-alcoholic" or self.adicional == "alcoholic":
            if self.adicional == "alcoholic":
                self.alcoholic = True
            return f"Bebida {self.adicional}"
        else:
            return "Paquete"
        
    def __str__(self):

        return f"{self.nombre},{self.cantidad}"
        
        
    
        
    

