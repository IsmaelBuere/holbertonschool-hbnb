from flask_restx import Namespace, Resource
from models import country
from flask import jsonify

ns = Namespace('countries', description='Operaciones relacionadas con países')

# Simulando una base de datos de países pre-cargados
countries = [
    country(name='United States', code='US'),
    country(name='Canada', code='CA'),
    # Añadir más países según sea necesario
]

@ns.route('/')
class countryList(Resource):
    def get(self):
        """Recuperar todos los países pre-cargados"""
        return jsonify([country.to_dict() for country in countries])

@ns.route('/<string:country_code>')
class countryDetail(Resource):
    def get(self, country_code):
        """Recuperar los detalles de un país específico por su código"""
        country = next((country for country in countries if country.code == country_code), None)
        if country is None:
            return {'message': 'País no encontrado'}, 404
        return jsonify(country.to_dict())

@ns.route('/<string:country_code>/cities')
class countryCities(Resource):
    def get(self, country_code):
        """Recuperar todas las ciudades pertenecientes a un país específico"""
        country = next((country for country in countries if country.code == country_code), None)
        if country is None:
            return {'message': 'País no encontrado'}, 404
        cities = [city.to_dict() for city in City.query.filter_by(country_id=country.id)]
        return jsonify(cities)
