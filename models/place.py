#!/usr/bin/python3

from models.base_model import KeyModel
import json, os

class Place(KeyModel):
    def __init__(self, name, city_id, user_id, description, number_rooms, number_bathrooms, max_guest, price_by_night, latitude, longitude):
        super().__init__()
        self.name = name
        self.city_id = city_id
        self.user_id = user_id
        self.description = description
        self.number_rooms = number_rooms
        self.number_bathrooms = number_bathrooms
        self.max_guest = max_guest
        self.price_by_night = price_by_night
        self.latitude = latitude
        self.longitude = longitude
        self.amenities = []
        self.reviews = []
        
    def save(self):
        if not self.is_valid_host():
            raise ValueError("Invalid host")
        super().save()
        # Implementación específica para guardar un lugar

    def is_valid_host(self):
        file_path = "storage/User.json"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    all_data = json.load(file)
                except json.JSONDecodeError:
                    all_data = []
            for user in all_data:
                if user['id'] == self.user_id:
                    return True
        return False

    def delete(self):
        return super().delete()        
        # Implementación específica para eliminar un lugar

    def update(self, **kwargs):
        super().update(**kwargs)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name,
            'description': self.description,
            'number_rooms': self.number_rooms,
            'number_bathrooms': self.number_bathrooms,
            'max_guest': self.max_guest,
            'price_by_night': self.price_by_night,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'city_id': self.city_id,
            'user_id': self.user_id
        })
        return data

    def get_amenities(self):
        # Lógica para obtener las amenities del lugar
        return self.amenities

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
        self.save()

    def remove_amenity(self, amenity):
        if amenity in self.amenities:
            self.amenities.remove(amenity)
            self.save()

    def get_reviews(self):
        # Lógica para obtener las reviews del lugar
        return self.reviews

    def add_review(self, review):
        self.reviews.append(review)
        self.save()

    def remove_review(self, review):
        if review in self.reviews:
            self.reviews.remove(review)
            self.save()
