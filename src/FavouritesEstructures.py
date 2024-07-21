from random import randint
from PlanetsEstructures import PlanetsEstructures
from CharactersEstructures import CharactersEstructures


class FavouritesEstructures:
    _contenidoFavoritos = []

    def __init__(self):
        self.id = None
        self.starships_id = None
        self.planets_id = None
        self.characters_id = None
        self.users_id = None
        FavouritesEstructures._contenidoFavoritos.append(self)
    
    def serialize(self):
        return{
            "id": self.id,
            "starships_id": self.starships_id,
            "planets_id": self.planets_id,
            "characters_id": self.characters_id,
            "users_id": self.users_id
        }
    
    def favoritosUsuario():
        return [favorito.serialize() for favorito in FavouritesEstructures._contenidoFavoritos]


tatooine = PlanetsEstructures()
tatooine.name = "Tatooine"
tatooine.diameter = 10465
tatooine.rotation_period = 23
tatooine.orbital_period = 304
tatooine.gravity = "1 standard"
tatooine.population = 200
tatooine.climate = "arid"
tatooine.terrain = "desert"

char1 = CharactersEstructures()
char1.name = "Luke Skywalker"
char1.height = 172
char1.mass = 77
char1.hair_color = "Blond"
char1.skin_color = "Fair"
char1.birth_year = "19BBY"
char1.gender = "male"

# Crear favoritos predefinidos
fav1 = FavouritesEstructures()
fav1.starships_id = None
fav1.planets_id = tatooine.id
fav1.characters_id = char1.id
fav1.users_id = 1  # Asumiendo que ya has creado un usuario con id = 1

fav_for_char1 = FavouritesEstructures()
fav_for_char1.id = 1  # Asignar un ID al favorito si es necesario (opcional)
fav_for_char1.starships_id = None
fav_for_char1.planets_id = None
fav_for_char1.characters_id = char1.id
fav_for_char1.users_id = 1  # Suponiendo que el usuario con id 1 ya existe

