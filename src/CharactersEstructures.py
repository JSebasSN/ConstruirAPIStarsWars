from random import randint

class CharactersEstructures:
    _panelPersonajes = []

    def __init__(self):
        self.id = self._generateId()
        self.name = ""
        self.height = None
        self.mass = None
        self.hair_color = ""
        self.skin_color = ""
        self.birth_year = ""
        self.gender = "male"
        CharactersEstructures._panelPersonajes.append(self)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "birth_year": self.birth_year,
            "gender": self.gender
        }

# mostrarPersonajes, mostrarPersonaje 

 
    def _generateId(self):
        return randint(0, 99999999)

    #DEvuelve la lista con los personajes que se han guardado en la lista vacia 
    def mostrarPersonajes():        
        return [personaje.serialize() for personaje in CharactersEstructures._panelPersonajes]
    

    
    def mostrarPersonaje(id):
        for personaje in CharactersEstructures._panelPersonajes:
            if personaje.id == id:
                return personaje.serialize()
        return {"Error" : "NO se ha encontrado al personaje"}
    

        

# Crear personajes predefinidos y agregarlos a la lista directamente
char1 = CharactersEstructures()
char1.name = "Luke Skywalker"
char1.height = 172
char1.mass = 77
char1.hair_color = "Blond"
char1.skin_color = "Fair"
char1.birth_year = "19BBY"
char1.gender = "male"

char2 = CharactersEstructures()
char2.name = "Darth Vader"
char2.height = 202
char2.mass = 136
char2.hair_color = "None"
char2.skin_color = "White"
char2.birth_year = "41.9BBY"
char2.gender = "male"

char3 = CharactersEstructures()
char3.name = "Leia Organa"
char3.height = 150
char3.mass = 49
char3.hair_color = "Brown"
char3.skin_color = "Light"
char3.birth_year = "19BBY"
char3.gender = "female"