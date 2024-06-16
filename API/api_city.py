from flask_restx import Namespace, Resource, fields
from models import City, Country
from flask import request, jsonify
from werkzeug.exceptions import BadRequest

ns = Namespace('cities', description='Operaciones relacionadas con ciudades')

city_model = ns.model('City', {
    'name': fields.String(required=True, description='El nombre de la ciudad'),
    'country_code': fields.String(required=True, description='El código ISO del país')
})

@ns.route('/')
class CityList(Resource):
    @ns.expect(city_model)
    def post(self):
        """Crear una nueva ciudad"""
        data = request.get_json()
        country = next((country for country in countries if country.code == data['country_code']), None)
        if country is None:
            return {'message': 'Código de país inválido'}, 400

        if any(city.name == data['name'] and city.country_id == country.id for city in City.query.all()):
            return {'message': 'El nombre de la ciudad debe ser único dentro del mismo país'}, 409

        new_city = City(name=data['name'], country_id=country.id)
        new_city.save()
        return jsonify(new_city.to_dict()), 201

    def get(self):
        """Recuperar todas las ciudades"""
        cities = City.query.all()
        return jsonify([city.to_dict() for city in cities])

@ns.route('/<int:city_id>')
class CityDetail(Resource):
    def get(self, city_id):
        """Recuperar detalles de una ciudad específica"""
        city = City.query.get(city_id)
        if city is None:
            return {'message': 'Ciudad no encontrada'}, 404
        return jsonify(city.to_dict())

    @ns.expect(city_model)
    def put(self, city_id):
        """Actualizar la información de una ciudad existente"""
        data = request.get_json()
        city = City.query.get(city_id)
        if city is None:
            return {'message': 'Ciudad no encontrada'}, 404

        country = next((country for country in countries if country.code == data['country_code']), None)
        if country is None:
            return {'message': 'Código de país inválido'}, 400

        if any(c.name == data['name'] and c.country_id == country.id for c in City.query.all()):
            return {'message': 'El nombre de la ciudad debe ser único dentro del mismo país'}, 409

        city.name = data['name']
        city.country_id = country.id
        city.save()
        return jsonify(city.to_dict()), 200

    def delete(self, city_id):
        """Eliminar una ciudad específica"""
        city = City.query.get(city_id)
        if city is None:
            return {'message': 'Ciudad no encontrada'}, 404
        city.delete()
        return '', 204
