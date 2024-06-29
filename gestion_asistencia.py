class GestionAsistencia:
    def __init__(self, gestion_datos):
        self.gestion_datos = gestion_datos
        self.codigos_validados = set()

    def validar_boleto(self, codigo_unico, partidos):
        for partido in partidos:
            for entrada in partido.entradas:
                if entrada.codigo_unico == codigo_unico:
                    if codigo_unico in self.codigos_validados:
                        #Se revisa que el codigo unico no se haya utilizado previamente
                        print("El boleto ya ha sido utilizado.")
                        return False
                    else:
                        #Se valida el codigo y se confirma la asistencia.
                        entrada.asistio = True
                        partido.asistencia += 1
                        self.codigos_validados.add(codigo_unico)
                        print("Boleto válido. Asistencia registrada.")
                        return True
        #Si el codigo no coincide con ningun codigo generado se asume que es falso.
        print("Boleto falso.")
        return False
