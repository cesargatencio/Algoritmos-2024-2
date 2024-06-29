from gestion_datos import GestionDatos
from entrada import Entrada

class GestionVentaEntradas:
    def __init__(self, gestion_datos,estadios):
        self.gestion_datos = gestion_datos
        self.mapa_estadios = self.inicializar_mapa_estadios(estadios)

    def inicializar_mapa_estadios(self, estadios):
        #Se inicia la iteracion para crear los asientos de cada estadio. Retorna un diccionario con los asientos VIP y General de cada estadio.
        mapa_estadios = {}
        for estadio in estadios:
            general , vip =  self.crear_mapa_asientos(estadio)
            estadio.mapa_estadios[estadio.nombre] = {"general": general, "vip": vip}

        return mapa_estadios

    def crear_mapa_asientos(self, estadio):
        #Se crean todos los asientos posibles para cada uno de los estadios tomando en cuenta su capacidad.
        n_filas_general= estadio.capacidad[0]//10
        #Notar que se asume que la capacidad debe ser multiplo de 10 para facilitar su impresion y lectura.
        mapa_asientos_general = {f"{fila}{num}": False for fila in 'ABCDEFGHIJ' for num in range(1, n_filas_general+1)}
        n_filas_vip= estadio.capacidad[1]//10
        mapa_asientos_vip = {f"{fila}{num}": False for fila in 'KLMNOPQRST' for num in range(1, n_filas_vip+1)}
       
        return mapa_asientos_general, mapa_asientos_vip

    def seleccionar_asiento(self, partido):
        estadio_nombre = partido.estadio.nombre
        # if estadio_nombre not in self.mapa_estadios:
        #     print("Estadio invalido")
        #     exit(-1)
        estadio=partido.estadio
        n_filas_general= estadio.capacidad[0]//10    
        n_filas_vip= estadio.capacidad[1]//10  
        #Se imprimen los asientos posibles de General y VIP para cada estadio  
        print("\n   ----GENERAL----")
        print("  A B C D E F G H I J")
        for n in range(1, n_filas_general+1):
            print(n, end=" ")
            for l in ["A", "B", "C", "D", "E" ,"F", "G", "H", "I", "J"]:
                if estadio.mapa_estadios[estadio_nombre]["general"][f"{l}{n}"]:
                    #Se revisa si el asiento ya fue tomado.
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print("\n")
        print(''' 
  ___________________
 |__       |       __|
 |  |      |      |  |
[   |      O      |   ]
 |__|      |      |__|
 |_________|_________|
            
''')
        print("\n   -----VIP-----")
        print("  K L M N O P Q R S T")
        for n in range(1, n_filas_vip+1):
            print(n, end=" ")
            for l in ["K", "L", "M", "N", "O" ,"P", "Q", "R", "S", "T"]:
                if estadio.mapa_estadios[estadio_nombre]["vip"][f"{l}{n}"]:
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print("\n")    
        while True:
            columna=input("Ingrese la columna de su asiento\n-->")
            while not columna.upper() in "ABCDEFGHIJKLMNOPQRST":
                print("Ingreso Invalido")
                columna=input("Ingrese la columna de su asiento\n-->")
            if columna.upper() in "ABCDEFGHIJ":
                tipo_entrada="General"
            elif columna.upper() in "KLMNOPQRST":
                tipo_entrada="VIP"
            fila= input("Ingrese la fila de su asiento\n-->")
            while not fila.isnumeric():
                print("Ingreso Invalido")
                fila= input("Ingrese la fila de su asiento\n-->")
            asiento = columna.upper() + str(fila)
            if tipo_entrada=="General":
                try:
                    #Validacion de los asientos.
                    if not estadio.mapa_estadios[estadio_nombre]["general"][asiento]:
                        estadio.mapa_estadios[estadio_nombre]["general"][asiento] = True
                        return asiento , tipo_entrada
                except KeyError:
                    print("Ese asiento ya esta ocupado o no existe, elija otro.")
            elif tipo_entrada=="VIP":
                try:
                    if not estadio.mapa_estadios[estadio_nombre]["vip"][asiento]:
                        estadio.mapa_estadios[estadio_nombre]["vip"][asiento] = True
                        return asiento , tipo_entrada
                except KeyError:
                    print("Ese asiento ya esta ocupado o no existe, elija otro.")

    def vender_entrada(self, cliente, partido):
        #Se llama la funcion seleccionar_asiento la cual retorna el asiento.
        asiento, tipo_entrada = self.seleccionar_asiento(partido)
        #Se genera el codigo unico del asiento el cual es utilizado para validar la entrada y hacer compras en el restaurante.
        codigo = f"{partido.numero_partido}{asiento}"
        print(f"El codigo de su boleto es: {codigo}")
        #Se genera un objeto entrada de Clase entrada.
        entrada = Entrada(tipo_entrada, partido, asiento, cliente, codigo_unico=codigo)
        #Se acumula la entrada en su partido correspondiente.
        partido.entradas.append(entrada)
        return entrada




    
