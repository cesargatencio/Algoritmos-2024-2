from gestion_datos import GestionDatos
from gestion_partidos import GestionPartidos
from gestion_venta_entradas import GestionVentaEntradas
from gestion_asistencia import GestionAsistencia
from gestion_venta_restaurante import GestionVentaRestaurante
from estadistica import GestionEstadisticas 
from cliente import Cliente 
from producto import Producto
from partido import Partido
from equipo import Equipo
import os
import pickle
def menu(): 
    #muestra el menu principal y da para sellecionar opcion.
    print("\n----- Menú Principal -----")
    print("\t1. Buscar partidos")
    print("\t2. Comprar entrada")
    print("\t3. Validar boleto")
    print("\t4. Menú Restaurantes")
    print("\t5. Menú estadísticas")
    print("\t6. Salir\n")

    opcion = input("Seleccione una opción.\n--> ")
    while opcion!="1" and opcion!="2" and opcion!="3" and opcion!="4" and opcion!="5" and opcion!="6":
        #Validacion
        print("\nOpción inválida. Intente de nuevo.")
        opcion = input("Seleccione una opción.\n-->")
    
    return opcion

def cargar_modulos_git():
    # Crear instancia de Gestión de Datos y cargar datos
    gestion_datos = GestionDatos()
    equipos=gestion_datos.cargar_equipos()
    estadios=gestion_datos.cargar_estadios()
    partidos= gestion_datos.cargar_partidos()

    # Inicializar otros módulos
    gestion_partidos = GestionPartidos(gestion_datos)
    gestion_restaurante = GestionVentaRestaurante(gestion_datos)
    gestion_ventas = GestionVentaEntradas(gestion_datos, estadios)
    gestion_asistencia = GestionAsistencia(gestion_datos)
    estadisticas = GestionEstadisticas(gestion_datos)

    return equipos, estadios, partidos, gestion_partidos, gestion_restaurante, gestion_ventas, gestion_asistencia, estadisticas

def cargar_modulos_txt():
    # Load data from .txt files
    equipos = []
    estadios = []
    partidos = []

    # Cargar equipos del txt
    with open('datos_txt/equipos.txt', 'rb') as f:
        data = pickle.load(f)
        equipos=data
        # for equipo in data:
        #     equipos.append(equipo)

    # Cargar estadios del txt
    with open('datos_txt/estadios.txt', 'rb') as f:
        data = pickle.load(f)
        estadios=data
        # for equipo in data:
        #     estadios.append(equipo)

    # Cargar partidos del txt
    with open('datos_txt/partidos.txt', 'rb') as f:
        data = pickle.load(f)
        partidos=data
        # for partido in data:
        #     partidos.append(partido)

        # Create a GestionDatos instance
    gestion_datos = GestionDatos()

    # Inicializar otros módulos
    gestion_partidos = GestionPartidos(gestion_datos)
    gestion_restaurante = GestionVentaRestaurante(gestion_datos)
    gestion_ventas = GestionVentaEntradas(gestion_datos,estadios)
    gestion_asistencia = GestionAsistencia(gestion_datos)
    estadisticas = GestionEstadisticas(gestion_datos)

    return equipos, estadios, partidos, gestion_partidos, gestion_restaurante, gestion_ventas, gestion_asistencia, estadisticas



def main():
    while True:
        #se permite elegir entre cargar los datos de git, es decir desde cero, o de archivos.txt que ya contiene datos acumulados.
        print("¿Desea cargar datos desde github o desde archivos?")
        print("\t1. Cargar desde github.")
        print("\t2. Cargar desde archivos.")
        aux = input("Seleccione una opción\n-->")
        while aux!="1" and aux!="2":
            print("Opción inválida, inten de nuevo.")
            aux = input("Seleccione una oción\n-->")
        if aux=="1":
           equipos, estadios, partidos, gestion_partidos, gestion_restaurante, gestion_ventas, gestion_asistencia, estadisticas= cargar_modulos_git()
           break
        elif aux=="2":
            try:
                equipos, estadios, partidos, gestion_partidos, gestion_restaurante, gestion_ventas, gestion_asistencia, estadisticas= cargar_modulos_txt()
                break
            except FileNotFoundError:
                print("No se encontraron los archivos de texto. Verifique que ya se encuentren cargados.")
          
    
    print("\nBienvenido a la EUROCOPA ALEMANIA 2024!!!")
   
    
    
    while True:
        opcion = menu()
        if opcion == '1':
            while True:
                #Se muestra el sub menu de la busqueda de partidos
                print("\n\t1. Buscar partidos por país.")
                print("\t2. Buscar partidos por estadio.")
                print("\t3. Buscar partidos por fecha.")
                print("\t4. Volver al Menú.")
                opcion1 = input("\nSeleccione una opción.\n--> ")
                while opcion1!="1" and opcion1!="2" and opcion1!="3" and opcion1!="4":
                    print("\nOpción inválida. Intente de nuevo.")
                    opcion1 = input("Seleccione una opción.\n--> ")
                
            

                if opcion1=="1":
                    print("\nLista de paises:") 
                    #Se le muestra al usuario una lista con indice de todos los  paises. 
                    for i, pais in enumerate(equipos):
                        print(f"\t{i+1}. {pais.nombre}")
                
                    #Usuario selecciona un pais
                    aux=input("\nIngrese el numero del pais a seleccionar.\n--> ")
                    while True:
                        #Validacion de input usuario
                        try:
                            aux=int(aux)
                            break
                        except ValueError:
                            print("Error, ingrese un número")
                            aux=input("Ingrese el número del pais a seleccionar.\n--> ")
                    while not int(aux) in range(len(equipos)+1):
                        print("Opción inválida. Intente de nuevo.")
                        aux=input("Ingrese el número del pais a seleccionar\n--> ")
                    #Se obtiene el nombre del pais en base al input del usuario.
                    nombre_pais = equipos[int(aux)-1].nombre
                    #Se llama la funcion buscar_partidos_por_pais la cual retorna la lista partidos_pais.
                    partidos_pais = gestion_partidos.buscar_partidos_por_pais(nombre_pais, partidos)
                    if partidos_pais:
                        print(f"\nPartidos por país ({nombre_pais}):")
                    for partido in partidos_pais:
                        #Se muestran los datos de los partidos del pais seleccionado.
                        print(f"\t{partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre} en {partido.estadio.nombre} el {partido.fecha}")
                

                if opcion1=="2": 
                    print("Lista Estadios:")
                    #Se muestra lista con indice de todos los estadios. 
                    for i, estadio in enumerate(estadios):
                     print(f"\t{i+1}. {estadio.nombre}")

                    #Usuario seleciona opcion.
                    aux=input("\nIngrese el número del estadio a seleccionar.\n--> ")
                    while True:
                        #Validacion de input
                        try:
                            aux=int(aux)
                            break
                        except ValueError:
                            print("Error, ingrese un número")
                            aux=input("Ingrese el número del estadio a seleccionar.\n--> ")
                    while  not int(aux) in range(len(estadios)+1):
                        print("Opción inválida. Intente de nuevo.")
                        aux=input("Ingrese el número del estadio a seleccionar\n--> ")

                    #Utilizando el input se obtiene el nombre de estadio deseado.
                    nombre_estadio=estadios[int(aux)-1].nombre
                    #Se llama la funcion buscar_partidos_por_estadio la cual retorna una lista partidos_estadio.
                    partidos_estadio=gestion_partidos.buscar_partidos_por_estadio(nombre_estadio, partidos)
                    if partidos_estadio:
                        print(f"\nPartidos por estadio ({nombre_estadio}):")
                    for partido in partidos_estadio:
                        #Se muestran los datos de cada partido dentro de la lista.
                        print(f"\t{partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre} el {partido.fecha}")
                
            
                if opcion1=="3": 
                    #Se genera un set organizado de las fechas posibles y luego se muestran con indice al usuario. 
                    fechas = sorted({partido.fecha for partido in partidos}, key= lambda x: x[4:])
                    print("Lista Fechas:")
                    for i, partido in enumerate(fechas):
                        print(f"\t{i+1}. {partido}")
                    #Usuario selecciona opcion.
                    aux=input("\nIngrese el número de la fecha a seleccionar\n--> ")
                    while True:
                        #Validacion
                        try:
                            aux=int(aux)
                            break
                        except ValueError:
                            print("Error, ingrese un número.")
                            aux=input("Ingrese el número de la fecha a seleccionar\n--> ")
                    while  not int(aux) in range(len(estadios)+4):
                        print("Opción inválida. Intente de nuevo.")
                        aux=input("Ingrese el número de la fecha a seleccionar\n--> ")
                    #Se obtiene la fecha desde fechas utilizando el input de usuario.
                    fecha=fechas[int(aux)-1]
                    #Se llama la funcion buscar_partidos_por_fecha la cual retorna una lista partidos_fecha.
                    partidos_fecha=gestion_partidos.buscar_partidos_por_fecha(fecha, partidos)
                    if partidos_fecha:
                     print(f"\nPartidos por la fecha ({fecha}):")
                    for partido in partidos_fecha:
                        #Se muestran los datos de cada partido dentro de la lista.
                        print(f"\t{partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre} el {partido.fecha}")

                if opcion1=="4":
                    #Cierra el sub-menu y se vuelve al menu principal.
                    break

                   

        
        elif opcion == '2':
            #Se le pide al cliente nombre, cedula y edad, todo con su validacion.
            while True:
                nombre_cliente = input("Ingrese el nombre del cliente\n--> ")
                if not nombre_cliente.isalpha():
                    print("Error, ingrese un nombre válido.")
                    continue
                break
            while True:
                cedula_cliente = input("Ingrese la cédula del cliente\n--> ")
                if not cedula_cliente.isnumeric():
                    print("La cédula debe ser un número. Intente de nuevo.")
                    continue
                break
            while True:
                edad_cliente = (input("Ingrese la edad del cliente\n--> "))
                if not edad_cliente.isnumeric():
                    print("Edad inválida. Intente de nuevo.")
                    continue
                break

            #Se crea un objeto cliente de la clase Cliente usando el input de usuario.          
            cliente = Cliente(nombre_cliente, cedula_cliente, edad_cliente)

            print("\nLista partidos:")
            #Se muestra al usuario una lista con indices de todos los partidos
            for i, partido in enumerate(partidos):
                partido.numero_partido = i + 1
                print(f"\t{i + 1}. {partido.equipo_local.nombre} vs {partido.equipo_visitante.nombre} en {partido.estadio.nombre} el {partido.fecha}")

            #Input de usuario.
            partido_seleccionado = (input("\nIngrese el número del partido.\n--> ")) 
            while True:
                #Validacion.
                try:
                    partido_seleccionado=int(partido_seleccionado)
                    break
                except ValueError:
                    print("Error, ingrese un número")
                    partido_seleccionado=input("Ingrese el número del partido.\n--> ") 
            while  not int(partido_seleccionado) in range(len(partidos)+1):
                print("Opción inválida. Intente de nuevo.")
                partido_seleccionado=input("Ingrese el el número del partido.\n--> ")             
            partido_seleccionado=int(partido_seleccionado)
            partido = partidos[partido_seleccionado-1]
            #Se llama la funcion vender_entrada la cual muestra el mapa de entradas dependiendo del estadio del partido,
            #y recibe los inputs del cliente para seleccionar su asiento.
            entrada = gestion_ventas.vender_entrada(cliente, partido)
            if entrada:
                print("Entrada comprada exitosamente.")
            else:
                print("Error al comprar la entrada.")
        
        elif opcion == '3':
            #Input usuario del codigo de formato--> num_estadio+columna+num_fila
            codigo_unico = input("Ingrese el código único del boleto.\n--> ")
            #Se llama la funcion validar_boleto la cual revisa si el codigo unico ingresado existe,
            #y en caso de existir valida su asistencia al partido.
            gestion_asistencia.validar_boleto(codigo_unico, partidos)
        
        elif opcion == '4':
           while True: 
                #Se muestra un sub-menu para la gestion de los restaurantes.
                print("\n\t1. Buscar producto por nombre")
                print("\t2. Buscar producto por tipo")
                print("\t3. Buscar producto por rango de precio")
                print("\t4. Comprar productos, solo VIP.")
                print("\t5. Volver al menú principal")
                opcion_producto = input("\nSeleccione una opción\n--> ")
                while opcion_producto!="1" and opcion_producto!="2" and opcion_producto!="3" and opcion_producto!="4" and  opcion_producto!="5":
                    #Validacion.
                    print("Opción inválida. Intente de nuevo.")
                    opcion_producto = input("Seleccione una opción\n--> ")

                if opcion_producto=="1":
                    nombre_producto = input("Ingrese el nombre del producto.\n--> ")
                    #Se llama la funcion buscar_producto_nombre la cual compara el input de usuario con
                    #todos los productos de todos los restaurantes de todos los estadios.
                    #Si consigue el producto retorna nombre del estadio y restaurante donde se encuentra.
                    estadio_nombre, restaurante_nombre =gestion_restaurante.buscar_producto_nombre(nombre_producto, estadios)
                    if estadio_nombre and restaurante_nombre :
                        print(f"\nEl producto: {nombre_producto} se encuentra en el restaurante: {restaurante_nombre} del estadio: {estadio_nombre}\n")
                    else:
                        print(f"\nNo se encontró el producto {nombre_producto}")
                    
                elif opcion_producto=="2":
                    #Se muestra sub-menu mostrando los posibles tipos de producto.
                    print("\nTipos de producto:")
                    print("\t1. Alimento servido.")
                    print("\t2. Bebida alcoholica.")
                    print("\t3. Bebida no alcoholica.")
                    print("\t4. Alimento de paquete.")
                    tipo_producto = input("\nIngrese el número del tipo de producto.\n--> ")
                    while tipo_producto!="1" and tipo_producto!="2" and tipo_producto!="3" and tipo_producto!="4":
                        #Validacion de input de usuario
                        print("Opción inválida. Intente de nuevo.")
                        tipo_producto = input("Ingrese el número del tipo de producto.\n--> ")
                    if tipo_producto=="1":
                        tipo_producto="Alimento"
                    elif tipo_producto=="2":
                        tipo_producto="Bebida alcoholic"
                    elif tipo_producto=="3":
                        tipo_producto="Bebida non-alcoholic"
                    elif tipo_producto=="4":
                        tipo_producto="Paquete"
                    #Se llama la funcion buscar_producto_tipo la cual compara el input de usuario con
                    #todos los productos de todos los restaurantes de todos los estadios.
                    #En cada caso que consigue el producto retorna e imprime nombre de producto nombre del estadio
                    #  y restaurante donde se encuentra.
                    gestion_restaurante.buscar_producto_tipo(tipo_producto,estadios)


                elif opcion_producto=="3":
                    #Se pide input de rango de precio al usuario con sus validaciones.
                    minimo =(input("Ingrese el precio mínimo.\n--> "))
                    while not minimo.isnumeric():
                        print("Opción inválida. Intente de nuevo.")
                        minimo =(input("Ingrese el precio mínimo.\n--> "))
                    maximo = (input("Ingrese el precio máximo.\n--> "))
                    while not maximo.isnumeric():
                        print("Opción inválida. Intente de nuevo.")
                        maximo = (input("Ingrese el precio máximo.\n--> "))
                    print(f"Lista de productos entre {minimo} y {maximo}")
                    #Se llama la funcion buscar_producto_rango la cual compara el input de usuario con
                    # todos los productos de todos los restaurantes de todos los estadios.
                    # Esta retorna e imprime nombre de producto, nombre de restaurante y nombre de estadio
                    #para todos los productos que se encuentren dentro del rango seleccionado.
                    gestion_restaurante.buscar_producto_precio( minimo, maximo, estadios)

                elif opcion_producto=='4':
                    #Input usuario del codigo de formato--> num_estadio+columna+num_fila  
                    codigo_unico = input("Ingrese el cogido unico de la entrada.\n--> ")
                    #Se llama la funcion validar_cliente_vip, la cual primero valida la existencia del codigo unico
                    #Luego valido que este codigo unico corresponda a una entrada VIP, y finalmente retorna
                    #La entrada a la que corresponde al codigo y el nombre del estadio donde se encuentra
                    entrada_cliente, estadio_nombre = gestion_restaurante.validar_cliente_vip(codigo_unico, partidos)
                    if entrada_cliente:
                        #Se llama la funcion mostrar menu, la cual muestra una lista con indice de los restaurantes del estadio al que 
                        #pertenece la entrada. Tras seleccionar el restaurante se muestra una lista con indice de los productos del mismo.
                        #El usuario selecciona los productos a comprar y esto retorna una lista llamada productos_deseados
                        productos_deseados = gestion_restaurante.mostrar_menu(estadio_nombre,estadios)
                        #Se llama la funcion procesar_venta, la cual recibe la lista de productos deseados, estadio y la entrada.
                        #Dentro de esta funcion se valida que si el cliente es menor de edad no 
                        #Esta retorna e imprime el total de la venta, posible descuento, IVA y  la lista de productos comprados.
                        resumen_venta = gestion_restaurante.procesar_venta(entrada_cliente, estadio_nombre, productos_deseados, partidos)
                        print(f"Productos:")
                        for producto in resumen_venta:
                            print(f"\t{producto.nombre}")
                    else:
                        print("Cliente no tiene una entrada VIP.")
                elif opcion_producto=="5":
                    break
        
        elif opcion == '5':
            while True:      
                #Se muestra sub-menu de estadisticas al usuario.
                print("\n\t1. Mostrar promedio de gastos VIP.")
                print("\t2. Mostrar tabla de asistencia.")
                print("\t3. Mostrar partido con mayor asistencia.")
                print("\t4. Mostrar partido con mayor cantidad de boletos vendidos.")
                print("\t5. Mostrar TOP 3 productos mas vendidos.")
                print("\t6. Mostrar TOP 3 clientes con mas compras.")
                print("\t7. Volver al menú principal.")
                opcion_estadistica=input("\nSeleccione una opcion.\n-->")
                while opcion_estadistica!="1" and opcion_estadistica!="2" and opcion_estadistica!="3" and opcion_estadistica!="4" and opcion_estadistica!="5" and opcion_estadistica!="6" and  opcion_estadistica!="7":
                    #Validacion de input de usuario
                    print("Opción inválida. Intente de nuevo.")
                    opcion_estadistica=input("Seleccione una opción.\n-->")
                    
                if opcion_estadistica=="1":
                    #Se llama la funcion promedio_gasto_vip la cual suma todos los gastos de clientes VIP y luego divide entre cantidad de clientes.
                    promedio_gasto_vip = estadisticas.promedio_gasto_vip(partidos)
                    print(f"Promedio de gasto VIP: {promedio_gasto_vip}")
                elif opcion_estadistica=="2":
                    #Se llama la funcion tabla_asistencia_partidos la cual genera una tabla que muestra todos los partidos organizados por boletos vendidos,
                    #con su numero de confirmados y su relacion confirmados/venta
                    tabla_asistencia = estadisticas.tabla_asistencia_partidos(partidos)
                    print(f"{tabla_asistencia}")
                elif opcion_estadistica=="3":
                    #Se llama la funcion partido_mayor_asistencia la cual itera por todos los partidos y devuelve el de mayor asistencia confirmada.
                    partido_max_asistencia = estadisticas.partido_mayor_asistencia(partidos)
                    if partido_max_asistencia:
                        print(f"Partido con mayor asistencia: {partido_max_asistencia.equipo_local.nombre} vs {partido_max_asistencia.equipo_visitante.nombre}")
                    else:
                        print(f"No se ha confirmado asistencia a ningún partido.")
                elif opcion_estadistica=="4":
                    #Se llama la funcion partido_mayor_boletos_vendidos la cual itera por todos los partidos y devuelve el de mayor numero de boletos vendidos.
                    partido_max_boletos_vendidos = estadisticas.partido_mayor_boletos_vendidos(partidos)
                    if partido_max_boletos_vendidos:
                        print(f"Partido con mayor boletos vendidos:  {partido_max_boletos_vendidos.equipo_local.nombre} vs {partido_max_boletos_vendidos.equipo_visitante.nombre}")
                    else:
                        print("No se han vendido boletos a ningún partido")
                elif opcion_estadistica=="5":
                    #Se llama la funcion top_productos_mas_vendidos la cual itera a traves de todas las entradas y sus compras. Esta devuelve los 3 productos 
                    #mas comprados.
                    top_productos = estadisticas.top_productos_mas_vendidos(partidos)
                    print(f"Top 3 productos más vendidos:")
                    for index, producto in enumerate(top_productos):
                        print(f"\t{index+1}. {producto[0]}")                              
                elif opcion_estadistica=="6":
                    top_clientes = estadisticas.top_clientes(partidos)
                    print(f"\tTop 3 clientes:")
                     #Se llama la funcion top_clientes la cual itera a traves de todas las entradas y sus clientes. Esta devuelve los 3 clientes
                    #con mas compras.
                    for index, cliente in enumerate(top_clientes):
                        print(f"\t{index+1}. {cliente[0]}")
                elif opcion_estadistica=="7":
                    break

                

                
        elif opcion == '6':
            print("Saliendo del programa.\nGracias por asistir a la EUROCOPA 2024.")
                            

               
            if not os.path.exists('datos_txt'):
                    os.makedirs('datos_txt')

                # Then, you can write to the file
            with open('datos_txt/equipos.txt', 'wb') as f:
                    # for equipo in equipos:
                    #     pickle.dump(equipo, f)
                    pickle.dump(equipos, f)

            with open('datos_txt/partidos.txt', 'wb') as f:
                    # for partido in partidos:
                    #     pickle.dump(partido, f)
                    pickle.dump(partidos, f)

            with open('datos_txt/estadios.txt', 'wb') as f:
                    # for estadio in estadios:
                    #     pickle.dump(estadio, f)
                    pickle.dump(estadios, f)
        
            break
                    
                    

main()


