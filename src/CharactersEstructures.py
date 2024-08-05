from random import randint


#Se define el nombre de la clase
class CharactersEstructures:
    _panelPersonajes = []

    ########################################
    #
    # FUNCION __INIT
    # Sirve para poder inicializar la clase, es indispensable al crear una clase. 
    # Recibe como parámetro a sí misma (self). Está generando unos parámetros concretos
    # a los que le podemos añadir más, se crea el esqueleto del objeto a tratar (en este caso)
    # de los caracteres. Cada parámetro se inicializa con algún valor o vacío. 
    def __init__(self):
        self.id = self._generateId()
        self.name = ""
        self.height = None
        self.mass = None
        self.hair_color = ""
        self.skin_color = ""
        self.birth_year = ""
        self.gender = "male"
        CharactersEstructures._panelPersonajes.append(self) #se usa para poder añadir algunos ejemplos preestablecidos. 


    # FUNCION SERIALIZE:
    # Se recibe también a sí misma como parámetro. 
    # Permite devolver un objeto con un formato concreto (en este caso Json)
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



    #Genera un id aleatorio, que será un número entero en 0 y 99999999
    def _generateId(self):
        return randint(0, 99999999)
    

    #DeEvuelve la lista con todos los personajes que se han guardado en la lista vacia creada arriba.
    # REturn: se hace un for que recorre la lista de personajes ("in CharactersEstructures._panelPersonajes")
    # en el for se genera una variable que es personaje, que será cada uno de los personajes que encuentre en la lista. 
    # en ese momento al personaje se le hace serialize para que nos lo devuelva en el formato que queremos (Json)
    def mostrarPersonajes():        
        return [personaje.serialize() for personaje in CharactersEstructures._panelPersonajes]
    

    #Recibe el id del persona que vayamos a mostrar. 
    #Recorre con un for la lista de personajes que se han ido añadiendo a _panelPersonajes
    # Si el personaje.id coincide con el que queremos mostrar, nos devuelve el personaje serializado con un formato concreto.
    # Si no, nos da un error. 
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