from random import randint

class PlanetsEstructures:
    _panelPlanetas = []

    def __init__(self):
        self.id = self._generateId()
        self.name = ""
        self.diameter = None
        self.rotation_period = None
        self.orbital_period = None
        self.gravity = ""
        self.population = None
        self.climate = ""
        self.terrain = ""
        PlanetsEstructures._panelPlanetas.append(self)

    def serialize(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "diameter" : self.diameter,
            "rotation_period" : self.diameter,
            "orbital_period" : self.orbital_period,
            "gravity" : self.gravity,
            "population" : self.population,
            "climate" : self.climate,
            "terrain" : self.terrain
        }

#mostrarPlanetas, mostrarPlaneta

    def _generateId(self):
        return randint(0, 99999999)
        

    def mostrarPlanetas():        
        return [planeta.serialize() for planeta in PlanetsEstructures._panelPlanetas]
    

    def mostrarPlaneta(id):
        for  planeta in PlanetsEstructures._panelPlanetas:
            if planeta.id == id:
                return planeta.serialize()
        return {"Error" : "NO se ha encontrado al planeta"}


tatooine = PlanetsEstructures()
tatooine.name = "Tatooine"
tatooine.diameter = 10465
tatooine.rotation_period = 23
tatooine.orbital_period = 304
tatooine.gravity = "1 standard"
tatooine.population = 200
tatooine.climate = "arid"
tatooine.terrain = "desert"


alderaan = PlanetsEstructures()
alderaan.name = "Alderaan"
alderaan.diameter = 12500
alderaan.rotation_period = 24
alderaan.orbital_period = 364
alderaan.gravity = "1 standard"
alderaan.population = 2000000000
alderaan.climate = "temperate"
alderaan.terrain = "grasslands, mountains"


hoth = PlanetsEstructures()
hoth.name = "Hoth"
hoth.diameter = 7200
hoth.rotation_period = 23
hoth.orbital_period = 549
hoth.gravity = "1.1 standard"
hoth.population = None
hoth.climate = "frozen"
hoth.terrain = "tundra, ice caves, mountain ranges"
