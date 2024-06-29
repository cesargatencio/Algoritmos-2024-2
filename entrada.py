from itertools import permutations


class Entrada:
    def __init__(self, tipo, partido, asiento, cliente, codigo_unico):
        self.tipo = tipo
        self.partido = partido
        self.asiento = asiento
        self.cliente = cliente
        self.codigo_unico = codigo_unico
        self.asistio = False
        self.precio = 35 if tipo == 'General' else 75
        self.detalles_factura = {}
        self.calcular_precio_final()
        self.productos_comprados = [] 

    def calcular_precio_final(self):
        descuento = 0
        if self.es_numero_vampiro(self.cliente.cedula):
            print("Su cedula es un numero vampiro! Es elegido para un 50% de descuento sobre el precio de su entrada. ")
            descuento = self.precio * 0.50
        subtotal = self.precio - descuento
        iva = subtotal * 0.16
        total = subtotal + iva
        self.precio = total
        self.detalles_factura = {"subtotal": subtotal, "descuento": descuento, "IVA": iva, "total": total}
        print(f"subtotal: {subtotal:.2f}, descuento: {descuento:.2f}, IVA: {iva:.2f}, total: {total:.2f}")

    def es_numero_vampiro(self, cedula):
        n_str = str(cedula)
        if len(n_str) % 2 != 0:
            return False
        
        half_length = len(n_str) // 2
        perms = permutations(n_str, half_length)

        for perm in perms:
            fang1 = int("".join(perm))
            remaining_digits = list(n_str)
            for digit in perm:
                remaining_digits.remove(digit)    
            fang2 = int("".join(remaining_digits))
            if str(fang1)[-1] == '0' and str(fang2)[-1] == '0':
                continue
            
            if fang1 * fang2 == int(cedula):
                return True
        return False
    
    def __str__(self):
     
        return f"{self.tipo}, {self.partido}, {self.asiento}, {self.cliente.__str__()}, {self.codigo_unico},{self.asistio}, {self.precio},{self.detalles_factura},{self.productos_comprados}"
