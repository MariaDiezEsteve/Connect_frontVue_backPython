from flask import Flask, request
from flask_cors import CORS

from src.weather_repository import *


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello, world. Everything ok"

@app.route("/cities", methods=["GET"])
def all_cities():
    return read_all()

@app.route("/cities/<city_id>", methods=["GET"])
def cities(city_id):
    return read(city_id)

@app.route("/cities", methods=["POST"])
def new_cities():
     data = request.get_json()
     create(data)
     return ""
 
@app.route("/cities/<id>", methods=["DELETE"])
def delete_city(id):
      remove_city(id) 
      return ""
  
@app.route("/cities/<city_id>", methods=["PUT"])
def update_city(city_id):
    data = request.get_json()
    update_city_data(city_id, data)
    return ""


if __name__ == "__main__":
    app.run(debug=True)