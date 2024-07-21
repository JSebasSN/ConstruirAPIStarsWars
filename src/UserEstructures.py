from random import randint

class UserEstructures:
    _panelUsuarios = []

    def __init__(self):
        self.id = self._generateId()
        self.user_name = ""
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        UserEstructures._panelUsuarios.append(self)

    def serialize (self):
        return{
            "id": self.id,
            "user_name": self.user_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email
        }



    #Genera el ID de manera aleatoria para el usuario 
    def _generateId(self):
        return randint(0, 99999999)
    


    #Coge los datos que tengan los atributos y los guarda en el objeto que se llama
    #usuario y nos lo devuelve fuera 
    def get_all_members():
        return [usuario.serialize() for usuario in UserEstructures._panelUsuarios]


user1 = UserEstructures()
user1.id=1 
user1.user_name="JohnDoe"
user1.first_name="John" 
user1.last_name="Doe" 
user1.email="john.doe@example.com"

user1 = UserEstructures()
user1.id=4 
user1.user_name="AnaPerez"
user1.first_name="Ana" 
user1.last_name="Perez" 
user1.email="ana.perez@example.com"

user1 = UserEstructures()
user1.id=9 
user1.user_name="LolaPuertos"
user1.first_name="Lola" 
user1.last_name="Puertos" 
user1.email="lola.puertos@example.com"

