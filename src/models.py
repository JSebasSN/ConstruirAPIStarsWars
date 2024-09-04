from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(250), nullable=False)
    first_name = db.Column(db.String(250), nullable=False)
    last_name = db.Column(db.String(250))
    email = db.Column(db.String(250), nullable=False)

    favourites = db.relationship("Favourites", back_populates="user")

    def __repr__(self):
        return '<User %r>' % self.username

    #Serialize: encripta los datos que queramos para hacerlos más seguros. Devuelve un objeto-diccionario
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "user_name" : self.user_name,
            "first_name" : self.first_name,
            "last_name" : self.last_name
            # do not serialize the password, its a security breach
        }
    
    
#Tabla de personajes
#En la columna gender le aporto un dato tipo Enum:
#Hace que solo se pueda elegir entre las 3 opciones proporcionadas,
#que en este caso son male, female y others
class Characters(db.Model):
    __tablename__ = 'Characters'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(250), nullable=False)
    height = db.Column(db.Integer)
    mass = db.Column(db.Integer)
    hair_color = db.Column(db.String(50))
    skin_color = db.Column(db.String(50))
    birth_year = db.Column(db.String(10))
    gender = db.Column(db.Enum('male', 'female', 'others', name='gender'))

    #RELACIÓN de la tabla characters con favourites
    favourites = db.relationship("Favourites", back_populates="characters")

#Tabla de planetas
class Planets(db.Model):
    __tablename__ = 'Planets'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.Integer)
    rotation_period = db.Column(db.Integer)
    orbital_period = db.Column(db.Integer)
    gravity = db.Column(db.String(50))
    population = db.Column(db.Integer)
    climate = db.Column(db.String(50))
    terrain = db.Column(db.String(50))

    #RELACIÓN de la tabla planets con favourites
    favourites = db.relationship("Favourites", back_populates="planets")

#Tabla de vehículos
class Starships(db.Model):
    __tablename__ = 'Starships'
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(150))
    starship_class = db.Column(db.String(150))
    manufacturer =  db.Column(db.String(150))
    cost_in_credits = db.Column(db.Integer)
    length = db.Column(db.Integer)
    crew = db.Column(db.Integer)
    passengers =db. Column(db.Integer)
    max_atmosphering_speed =db.Column(db.Integer)
    cargo_capacity = db.Column(db.Integer)

    #RELACIÓN de la tabla starhips con favourites
    favourites = db.relationship("Favourites", back_populates="starships")

#Tabla favoritos
#en esta tabla se añaden 4 columnas que hacen referencia al id de:
#planetas, vehiculos, personajes y usuarios
class Favourites(db.Model):
    __tablename__ = 'Favourites'
    id = db.Column(db.Integer, primary_key=True)
    starships_id = db.Column(db.Integer, db.ForeignKey('Starships.id'), nullable=True)
    planets_id = db.Column(db.Integer, db.ForeignKey('Planets.id'), nullable=True)
    characters_id = db.Column(db.Integer, db.ForeignKey('Characters.id'), nullable=True)
    users_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)

    #Con back_populates, se debe crear explícitamente la RELACIÓN tanto en la clase favourites como en la clases users, starships, planets y characters:
    #Creando las RELACIONES de la tabla favourites con users, starships, planets y characters
    user = db.relationship("User", back_populates="favourites")
    starships = db.relationship("Starships", back_populates="favourites")
    planets = db.relationship("Planets", back_populates="favourites")
    characters = db.relationship("Characters", back_populates="favourites")
