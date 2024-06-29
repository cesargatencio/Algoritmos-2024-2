class Equipo:
    def __init__(self, id, nombre, codigo_fifa, grupo):
        self.id = id
        self.nombre = nombre
        self.codigo_fifa = codigo_fifa
        self.grupo = grupo

    def __str__(self):
     
        return f"{self.id}, {self.nombre}, {self.codigo_fifa}, {self.grupo}"
    

        
