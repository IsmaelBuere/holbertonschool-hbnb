#!/usr/bin/python3

from models.base_model import KeyModel

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