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
    
    #Función que devuelve toda la lisata de favoritos. 
    def favoritosUsuario():
        return [favorito.serialize() for favorito in FavouritesEstructures._contenidoFavoritos]
    
    
    # REcoge el id del personaje y el id del usuario (con el que se ha iniciado la sesión).
    # Recorre con un for la lista de personajes, creando "personaje como variable."
    # Si personaje.id (de los que está en la lista) coincide con el id del personaje que buscamos entonces
    # genera una instancia (esqueleto) auxilizar de favoritos y lo pasa a la variable "nuevo_favorito"
    # nuevo_favorito.characters_id = id: coge el id del personaje que queremos añadir y se lo asigna al atributo characters_id
    # propio de la estructura nuevo_favorito, los copia a la clase FavouritesEstructures.
    # Hace la misma operación con el id del usuario
    # Retorna la lista de favoritos que se ha creado en la clase. 
    def mostrarPersonajeFav (id, users_id):
        for personaje in CharactersEstructures._panelPersonajes:
            if personaje.id == id:
                nuevo_favorito = FavouritesEstructures()
                nuevo_favorito.characters_id = id
                nuevo_favorito.users_id = users_id
                return FavouritesEstructures.favoritosUsuario()
    

    def mostrarPlanetaFav (id, users_id):
        for planeta in PlanetsEstructures._panelPlanetas:
            if planeta.id == id:
                nuevo_favorito = FavouritesEstructures()
                nuevo_favorito.planets_id = id
                nuevo_favorito.users_id = users_id
                return FavouritesEstructures.favoritosUsuario()    

    def eliminarPersonajeFav(id):
        personajeAEliminar = None
        for personaje in FavouritesEstructures._contenidoFavoritos:
            if personaje.characters_id == id:
                personajeAEliminar = personaje
                break
        if personajeAEliminar:
            FavouritesEstructures._contenidoFavoritos.remove(personajeAEliminar)
        return FavouritesEstructures.favoritosUsuario()   



    def eliminarPlanetaFav(id):
        planetaAEliminar = None
        for planeta in FavouritesEstructures._contenidoFavoritos:
            if planeta.planets_id == id:
                planetaAEliminar = planeta
                break
        if planetaAEliminar:
            FavouritesEstructures._contenidoFavoritos.remove(planetaAEliminar)
        return FavouritesEstructures.favoritosUsuario() 





