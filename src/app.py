
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


#Creamos las instancias para usar en los endpoints
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

#RUTAS PARA MOSTRAR TODOS LOS PLANETAS, PERSONAJES O USUARIOS
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
    
    
    
#RUTAS PARA MOSTRAR UN PERSONAJE O PLANETA CONCRETOS
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

@app.route('/users/favorites', methods=['GET'])
def handleFavoritos ():
    favoritos = FavouritesEstructures.favoritosUsuario()
    if (favoritos):
        return jsonify ({"favoritos":favoritos}), 200
    return ({"Error" : "no se han encontrado favoritos"}), 400



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
