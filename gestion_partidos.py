class GestionPartidos:
    def __init__(self, gestion_datos):
        self.gestion_datos = gestion_datos

    def buscar_partidos_por_pais(self, nombre_pais, partidos ):
        for partido in partidos:
            if partido.equipo_local and partido.equipo_visitante:  # Verifica que los equipos no sean None
              pass
        partidos_filtrados = [
            partido for partido in partidos 
            if partido.equipo_local and partido.equipo_visitante and
               (partido.equipo_local.nombre == nombre_pais or partido.equipo_visitante.nombre == nombre_pais)
        ]   #Se genera una lista con los partidos del pais seleccionado.
        return partidos_filtrados

    def buscar_partidos_por_estadio(self, nombre_estadio, partidos ):
        #Devuelve todos los partidos que coincidan con el nombre de estadio ingresado.
        return [partido for partido in partidos if partido.estadio.nombre == nombre_estadio]

    def buscar_partidos_por_fecha(self, fecha, partidos):
        ##Devuelve todos los partidos que coincidan con la fecha ingresada.
        return [partido for partido in partidos if partido.fecha.startswith(fecha)]
