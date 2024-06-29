import requests
from equipo import Equipo
from estadio import Estadio
from partido import Partido
from restaurantes import Restaurante


class GestionDatos:
    def __init__(self):
        self.equipos = []
        self.estadios = []
        self.partidos = []

    def cargar_equipos(self):
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for item in data:
                equipo = Equipo(item["id"], item['name'], item['code'], item['group'])
                # equipo.id = item['id']  # Asignar el ID del equipo
                self.equipos.append(equipo)
        return self.equipos
        

         

    def cargar_estadios(self):
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for item in data:
                rest_nombres = [i["name"] for i in item["restaurants"]]
                productos = [i["products"] for i in item["restaurants"]]
                restaurantes = [Restaurante(tup[0], tup[1]) for tup in (rest_nombres, productos)]
                estadio = Estadio(item['id'],item['name'], item['city'], restaurantes,item['capacity'])
                self.estadios.append(estadio)
        return self.estadios
        

        

    def cargar_partidos(self):
        url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            for item in data:
                equipo_local = next((equipo for equipo in self.equipos if equipo.id == item['home']['id']), None)
                equipo_visitante = next((equipo for equipo in self.equipos if equipo.id == item['away']['id']), None)
                estadio = next((estadio for estadio in self.estadios if estadio.id == item['stadium_id']), None)

                if equipo_local and equipo_visitante and estadio:
                    partido = Partido(equipo_local, equipo_visitante, item['date'], estadio)
                    self.partidos.append(partido)
        return self.partidos


      
