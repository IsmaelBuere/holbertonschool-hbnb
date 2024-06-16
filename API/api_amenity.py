#!/usr/bin/python3

import sys, os

# Agrega la ruta del directorio principal al sys.path para permitir importaciones desde otros directorios
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, jsonify, request, abort
from flask_restx import Api, Resource, fields
from werkzeug.exceptions import NotFound, BadRequest, Conflict

app = Flask(__name__)
api = Api(app)

# Definir el modelo para una Comodidad (Amenity)
amenity_model = api.model('Amenity', {
    'id': fields.Integer(readonly=True, description='El identificador único de una comodidad'),
    'name': fields.String(required=True, description='Nombre de la comodidad'),
    'created_at': fields.DateTime,
    'updated_at': fields.DateTime
})

# Almacenamiento en memoria para las comodidades
amenities = []
amenity_id_counter = 1

@api.route('/amenities')
class AmenityList(Resource):
    @api.doc('list_amenities')
    @api.marshal_list_with(amenity_model)
    def get(self):
        # Obtener una lista de todas las comodidades
        return amenities

    @api.doc('create_amenity')
    @api.expect(amenity_model)
    @api.marshal_with(amenity_model, code=201)
    def post(self):
        # Crear una nueva comodidad
        global amenity_id_counter
        amenity = request.json
        if not amenity.get('name'):
            raise BadRequest('El campo nombre es obligatorio.')
        if any(a['name'] == amenity['name'] for a in amenities):
            raise Conflict('Una comodidad con el nombre dado ya existe.')
        amenity['id'] = amenity_id_counter
        amenity_id_counter += 1
        amenities.append(amenity)
        return amenity, 201

@api.route('/amenities/<int:amenity_id>')
@api.response(404, 'Comodidad no encontrada')
@api.param('amenity_id', 'El identificador único de una comodidad')
class Amenity(Resource):
    @api.doc('get_amenity')
    @api.marshal_with(amenity_model)
    def get(self, amenity_id):
        # Obtener información detallada sobre una comodidad específica
        amenity = next((a for a in amenities if a['id'] == amenity_id), None)
        if not amenity:
            raise NotFound('Comodidad no encontrada')
        return amenity

    @api.doc('update_amenity')
    @api.expect(amenity_model)
    @api.marshal_with(amenity_model)
    def put(self, amenity_id):
        # Actualizar la información de una comodidad existente
        amenity = next((a for a in amenities if a['id'] == amenity_id), None)
        if not amenity:
            raise NotFound('Comodidad no encontrada')
        data = request.json
        if not data.get('name'):
            raise BadRequest('El campo nombre es obligatorio.')
        if any(a['id'] != amenity_id and a['name'] == data['name'] for a in amenities):
            raise Conflict('Una comodidad con el nombre dado ya existe.')
        amenity.update(data)
        return amenity

    @api.doc('delete_amenity')
    def delete(self, amenity_id):
        # Eliminar una comodidad específica
        global amenities
        amenities = [a for a in amenities if a['id'] != amenity_id]
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)