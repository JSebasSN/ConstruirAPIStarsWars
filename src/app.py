
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
from PlanetsEstructures import PlanetsEstructures
from CharactersEstructures import CharactersEstructures
from UserEstructures import UserEstructures
from FavouritesEstructures import FavouritesEstructures

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)


#Creamos las instancias para usar en los endpoints#
planetas = PlanetsEstructures()
personajes = CharactersEstructures()
usuarios = UserEstructures()
favoritos = FavouritesEstructures()

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

################################################################
# 
# RUTAS PARA MOSTRAR TODOS LOS PLANETAS, PERSONAJES O USUARIOS 
# 
# Función que recibe una url que es una variable (url) y validamos esa variable:
# Según llame a "personajes" o "planetas" recibirá un endpoint u otro. 
# Se crea una variable auxilidar ("personajes") y recibe la función creada para mostrar
# todos los personajes en su clase correspondiente (CharacteresEstructures)
# Se hace el response body a cada uno de los endpoints 

################################################################

@app.route('/<string:url>', methods=['GET'])
def handleShow(url):
    if (url == "personajes"):
        personajes = CharactersEstructures.mostrarPersonajes()
        response_body = {
            "Personajes" : personajes
        }
        return jsonify(response_body), 200
    
    elif (url == "planetas"):
        todosPlanetas = PlanetsEstructures.mostrarPlanetas()
        if (todosPlanetas):
            return jsonify ({"mensaje": todosPlanetas}), 200
        return jsonify ({"Error" : "error al mostrar los planetas"}), 400
    
    
    elif (url == "usuarios"):
        todosUsuarios = UserEstructures.get_all_members()
        response_body = {
            "lista de usuarios" : todosUsuarios
        }
        return jsonify (response_body), 200
    
    
    
################################################################
# 
# RUTAS PARA MOSTRAR UN PERSONAJE O PLANETA CONCRETOS 
#
#
# Recibe una variable url-tipo String y recibe otra variable id-tipo entero. 
# La función recibe igualmente estos 2 parámetros. Según lo que reciba irá a personajes y un personaje
# en concreto (id) o  a planetas y a un planeta en concreto(id) 
################################################################
@app.route ('/<string:url>/<int:id>', methods=['GET'])
def handleShowById(url, id):
    if (url == "personajes"):
        personaje = CharactersEstructures.mostrarPersonaje(id)
        response_body = {
            "Personaje" : personaje
        }
        return jsonify(response_body), 200
     
    elif (url == "planetas"):
        planeta = PlanetsEstructures.mostrarPlaneta(id)
        if (planeta):
            return jsonify ({"mensaje": planeta}), 200
        return jsonify ({"Error" : "error al mostrar el planeta"}), 400
    



################################################################
# 
# RUTAS PARA MOSTRAR LOS FAVORITOS DE UN USUARIO 
#
#
#Recibe un endopint fijo ya que no va entre <>. Obtiene los favoritos de un usuario. 
#  Llama a la función creada en FavouritesEstructures para mostrar la lista de favoritos. 
################################################################
@app.route('/users/favorites', methods=['GET'])
def handleFavoritos ():
    favoritos = FavouritesEstructures.favoritosUsuario()
    if (favoritos):
        return jsonify ({"favoritos":favoritos}), 200
    return ({"Error" : "no se han encontrado favoritos"}), 400


################################################################
# 
# RUTAS PARA AGREGAR UN PERSONAJE O PLANETA A FAVORITOS 
#
#
# Recibe un endpoint fijo (favorite) y hay una función si recibe people o si recibe planet
# Con el método POST agrega a través del id un personaje/planeta a la lista de favoritos. 
################################################################

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def handlePersonajeFav (people_id):
    id_miUsuario = 1
    favoritos = FavouritesEstructures.mostrarPersonajeFav(people_id, id_miUsuario)
    if (favoritos):
        return jsonify ({"Favorito" : favoritos}), 200
    return ({"error": "no se ha encontrado"})

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def handlePlanetaFav (planet_id):
    id_miUsuario = 1
    favoritos = FavouritesEstructures.mostrarPlanetaFav(planet_id, id_miUsuario)
    if (favoritos):
        return jsonify ({"Favorito" : favoritos}), 200
    return ({"error": "no se ha encontrado"})


################################################################
# 
# RUTAS PARA ELIMINAR UN PERSONAJE O PLANETA DE FAVORITOS 
# 
# Recibe "favorite", el endopoint de people o planets y un id, que será el que sea 
# eliminado. 
################################################################

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def deletePersonaje (people_id):
    personajeBorrado = FavouritesEstructures.eliminarPersonajeFav(people_id)
    if (personajeBorrado):
        return jsonify ({"mensaje" : "personaje borrado"}), 200
    return jsonify ({"Error":"no se ha encontrado al personaje"}), 400


@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def deletePlaneta (planet_id):
    planetaBorrado = FavouritesEstructures.eliminarPlanetaFav(planet_id)
    if (planetaBorrado):
        return jsonify ({"mensaje" : "planeta borrado"}), 200
    return jsonify ({"Error":"no se ha encontrado al planeta"}), 400





# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
