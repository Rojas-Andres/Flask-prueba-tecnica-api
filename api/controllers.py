from flask import Flask, request, Response, Blueprint,abort,jsonify,make_response
from flask_restplus import Api, Resource,fields 
from api.functions import *
bp_api = Blueprint('Api',__name__,url_prefix="/Api")

api = Api(bp_api,version="1.0",title="Api",description="End Points")
ns_model = api.namespace('Methods', description='Metodos')
ns_model_venta = api.namespace('ApiVentas', description='Ventas')
ns_model_usuario = api.namespace('Usuario', description='Usuario')

@ns_model.route('/mascotas/')
@api.doc(description="Listar todas las mascotas")
class Mascotas(Resource):
    def get(self):
        auth = request.json
        mascotas = listar_mascotas()
        return make_response(jsonify(mascotas),200)


@ns_model.route('/mascotasNoAdoptadas/')
@api.doc(description="Listar las mascotas que no han sido adoptadas")
class MascotasNoAdoptadas(Resource):
    def get(self):
        auth = request.json
        mascotas = listar_mascotas_no_adoptadas()
        return make_response(jsonify(mascotas),200)
@ns_model.route('/NumeroMascotastipo/')
@api.doc(description="Listar el número de mascotas por cada tipo de mascota")
class NumeroMascotasTipo(Resource):
    def get(self):
        auth = request.json
        mascotas = cantidad_tipo_mascotas()
        return make_response(jsonify(mascotas),200)
@ns_model.route('/PropietarioMascota/')
@api.doc(description="Listar los propietarios que tengan más de una mascota.")
class PropietarioMascota(Resource):
    def get(self):
        auth = request.json
        mascotas = propietarios_mascotas()
        return make_response(jsonify(mascotas),200)

@ns_model.route('/CantidadMascotaPropietario/')
@api.doc(description="Listar el número de mascotas por cada tipo de mascota y por cada propietario.")
class PropietarioMascota(Resource):
    def get(self):
        auth = request.json
        mascotas = cant_mascotas_pro()
        return make_response(jsonify(mascotas),200)
@ns_model.route('/PropietarioNoMascota/')
@api.doc(description="Listas los propietarios que no tienen mascotas.")
class PropietarioNoMascota(Resource):
    def get(self):
        auth = request.json
        mascotas = propietario_no_mascota()
        return make_response(jsonify(mascotas),200)