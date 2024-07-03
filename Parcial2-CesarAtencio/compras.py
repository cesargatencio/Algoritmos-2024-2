
def fibonacci(n, aux1= 0, aux2= 1):
    if aux1 > n:
        return False
    elif aux1 == n:
        return True
    else:
        return fibonacci(n, aux2, aux1 + aux2)



class Compras:
    def __init__(self, dispositivo, usuario):
        self.dispositivo=dispositivo
        self.usuario=usuario
        self.total=dispositivo.precio
        if fibonacci(self.total)==True:
            print("Su total era un numero de fibonacci, recibe un 15% de descuento-")
            self.total= self.total*0.85
        
        print(f"FACTURA: dispositivo: {self.dispositivo.modelo}, usuario: {self.usuario.nombre}, Total: {self.total} ")
