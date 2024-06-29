import requests
from cliente import Cliente
from producto import Producto
import math
from gestion_datos import GestionDatos

def es_numero_perfecto(n):
    if n < 2:
        return False
    suma = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            suma += i
            if i != n // i:
                suma += n // i
    return suma == n

class GestionVentaRestaurante:
    def __init__(self, gestion_datos):
        self.gestion_datos = gestion_datos
        self.estadios = {}
  
        
    def validar_cliente_vip(self, codigo_unico, partidos):
        for partido in partidos:
            for entrada in partido.entradas:
                if entrada.codigo_unico == codigo_unico and entrada.tipo == 'VIP':
                    return entrada, partido.estadio.nombre  # Devuelve el cliente y el nombre del estadio
                
        return None, None

            
        

    def mostrar_menu(self, estadio_nombre, estadios):
        #Se muestra el diccionario Menu creado por la funcion cargar menu
        print(f"\nRestaurantes en el Estadio {estadio_nombre}:")
        rest_dict = {}
        for i, restaurante_nombre in enumerate(estadios[estadio_nombre].items()):
            rest_dict[i+1] = restaurante_nombre
            print(f"\t{i+1}. {restaurante_nombre[0]}")
        prods = {}
        while True:
            rest = input("Seleccionar numero de restaurante.\n--> ")
            if not rest.isdigit():
                print("Numero de restaurante invalido. ")
                continue
            try:
                for i, producto in enumerate(rest_dict[int(rest)][1]):
                    prods[i+1] = producto
                    print(f"\t{i+1}. {producto.nombre} Precio:{producto.precio}")
            except KeyError:
                print("Numero de restaurante invalido. ")
                continue
            break
        while True:
            pd = input("Ingrese numero de productos deseados, separados por una coma y un espacio (, ).\n--> ").split(", ")
            try:
                productos_deseados = [prods[int(i)] for i in pd]
                break
            except KeyError:
                print("Ingreso un producto que no esta en el menu, vuelva a intentar.")
                continue
            except ValueError:
                print("Ingreso los numeros de los productos mal organizados. Recuerde dejar coma y espacio entre cada uno de ellos (, ).")
                continue
        return productos_deseados

    def buscar_producto_nombre(self, nombre_producto, estadios):
        #Se itera a traves de todos los estadios y restaurantes comparando el input con los productos que hay, en caso de encontrarlo retorna el nombre 
        #del estadio y restaurante donde se encuentra
        for estadio_nombre, restaurantes in estadios.items():
            for restaurante_nombre, productos in restaurantes.items():
                for producto in productos:
                    if producto.nombre == nombre_producto:
                        return estadio_nombre, restaurante_nombre
        return None, None  

    def buscar_producto_tipo(self, tipo_producto, estadios):
        #compara el input de usuario con
         #todos los productos de todos los restaurantes de todos los estadios.
        #En cada caso que consigue el producto retorna e imprime nombre de producto nombre del estadio
        #  y restaurante donde se encuentra.
        print(f"Productos de tipo: {tipo_producto}")
        for estadio_nombre, restaurantes in estadios.items():
            for restaurante_nombre, productos in restaurantes.items():
             for producto in productos:
                if producto.clasificacion == tipo_producto:
                    print(f"Producto: {producto.nombre},Restaurante: {restaurante_nombre}, Estadio: {estadio_nombre}")      

    def buscar_producto_precio(self, minimo, maximo, estadios):
        for estadio_nombre, restaurantes in estadios.items():
            for restaurante_nombre, productos in restaurantes.items():
                for producto in productos:
                    if float(minimo) <= producto.precio <= float(maximo):
                        print(f"Producto: {producto.nombre}, Precio: {producto.precio}, Restaurante: {restaurante_nombre}, Estadio: {estadio_nombre}")


    def seleccionar_productos(self, estadio_nombre, nombres_productos):
        productos_deseados = []
        for restaurante_nombre, productos in self.estadios[estadio_nombre].items():
            for producto in productos:
                if producto.nombre in nombres_productos:
                    productos_deseados.append(producto)
                    nombres_productos.remove(producto.nombre)  # Evitar duplicados
        
        if nombres_productos:  # Si quedan productos no encontrados
            print(f"Productos no encontrados: {', '.join(nombres_productos)}")
        
        return productos_deseados

    def procesar_venta(self, entrada_cliente, estadio_nombre, nombres_productos,partidos):
        total = 0
        detalles_productos = []
        for producto in nombres_productos:
            if producto.alcoholic and int(entrada_cliente.cliente.edad) < 18:
                print(f"Cliente {entrada_cliente.cliente.nombre} no puede comprar bebidas alcohólicas.")
                continue
            if producto.stock < 1:
                print(f"Producto {producto.nombre} no está disponible en stock.")
                continue
            total += producto.precio
            detalles_productos.append(producto)
            producto.stock -= 1

        if es_numero_perfecto(int(entrada_cliente.cliente.cedula)):
            descuento = total * 0.15
        else:
            descuento = 0

        subtotal = total
        total -= descuento

        for partido in partidos:
            for entrada in partido.entradas:
                if entrada.cliente.cedula == entrada_cliente.cliente.cedula and entrada.tipo == 'VIP':
                    entrada.productos_comprados.extend(detalles_productos)  # Agregar productos comprados a la entrada

        print("Resumen de la compra:")
        print(f"Cliente: {entrada_cliente.cliente.nombre}")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Descuento: ${descuento:.2f}")
        print(f"Total: ${total:.2f}")

        return detalles_productos
    

 
