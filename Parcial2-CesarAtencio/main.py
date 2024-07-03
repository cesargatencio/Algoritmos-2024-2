#Preguntas Venezuela:
#El 24 de julio se celebra el natalicio de Simon Bolivar.
#El goleador historico de la vinotinto es Salomon Rondon.
from dispositvo import Iphone, Watch
from usuario import Usuario
from compras import Compras
def main():
    dispositivos=[]
    dispositivos.append(Iphone("XS",150, "A16 Bionic", "18GB"))
    dispositivos.append(Watch("R12",50, "S5", True ))
    usuarios=[]
    usuarios.append(Usuario("Cesar",30820842))
    compras=[]
    compras_iphone=0
    compras_watch=0
    ingreso_iphone=0
    ingreso_watch=0
    total_wifi=0
    total_celular=0
    total=0
    print("Bienvenido")
    while True:
        aux=input("Seleccione una opcion:\n1. Registrar Dispositvo\n2. Registrar Usuario\n3. Realizar compra\n4. Cerrar Programa\n-->")
        if aux=="1":
            aux1=input("Ingrese tipo de dispositivo\n1. Iphone\n2. Apple watch\n-->")
            if aux1=="1":
                modelo=input("Ingrese el modelo:")
                precio=int(input("Ingrese el precio"))
                chip="A16 Bionic"
                almacenamiento=input("Ingrese su capacidad de almacenamiento: ")
                dispositivos.append(Iphone(modelo,precio, chip, almacenamiento))
            if aux1=="2":
                modelo=input("Ingrese el modelo:")
                precio=int(input("Ingrese el precio: "))
                chip="S5"
                wifi=input("Ingrese tipo\n1. Wifi\n2. Celular\n--> ")
                if wifi=="1":
                    wifi=True
                else:
                    wifi=False
                dispositivos.append(Watch(modelo,precio, chip, wifi))
        if aux=="2":
            nombre=input("Ingrese nombre del usuario: ")
            cedula=int(input("Ingrese cedula del usuario: "))
            usuarios.append(Usuario( nombre, cedula))

        if aux=="3":
            entrada=int(input("Ingrese la cedula del usuario a realizar la compra:"))
            usuario=None
            for x in usuarios:
                if entrada==x.cedula:
                    usuario=x
            if usuario==None:
                print("No se encontro al usuario no se puede proceder con la compra") 
            else:   
                for index ,x in enumerate(dispositivos):
                    print(index+1, x.show())
            
                aux2=int(input("Ingrese el index del producto a seleccionar\n-->"))
                seleccion=dispositivos[aux2-1]
                if seleccion.chip=="A16 Bionic":
                    compras_iphone+=1
                    ingreso_iphone+= seleccion.precio
                if seleccion.chip=="S5":
                    compras_watch +=1
                    ingreso_watch +=seleccion.precio
                    if seleccion.wifi==True:
                        total_wifi+=1
                    else:
                       total_celular+=1
                total+= seleccion.precio
                compras.append(Compras(seleccion, usuario))
                usuario.dispositivos.append(seleccion)
                #usuario.compras.append(Compras(seleccion, usuario))
            

        if aux=="4":
            print("ESTADISTICAS")
            print(f"numero de compras de iphone: {compras_iphone}")
            print(f"numero de compras de watch: {compras_watch}")
            print(f"numero de ingreso compras de iphone: {ingreso_iphone}")
            print(f"numero de ingreso compras de watch: {ingreso_watch}")
            print(f"numero de compras de watch wifi: {total_wifi}")
            print(f"numero de compras de watch celular: {total_celular}")
            print(f"Promedio de compra: {total/len(compras)}")

            break





main()