class Dispositvo:
    def __init__(self,modelo, precio, chip):
        self.modelo=modelo
        self.precio=precio
        self.chip=chip

class Iphone(Dispositvo):
    def __init__(self, modelo, precio,chip, almacenamiento):
        super().__init__(modelo, precio,chip)
        self.almacenamiento=almacenamiento

    def show(self):
        return f"modelo: {self.modelo},precio: {self.precio}, chip: {self.chip}, almacenamiento: {self.almacenamiento} " 
     

class Watch(Dispositvo):
    def __init__(self, modelo, precio, chip, wifi=bool):
        super().__init__(modelo, precio, chip)
        self.wifi=wifi
        if self.wifi==True:
            self.celular=False
        else:
            self.celular=True

    def show(self):
         return f"modelo: {self.modelo},precio: {self.precio}, chip: {self.chip}, wifi: {self.wifi}, celular: {self.celular} " 

