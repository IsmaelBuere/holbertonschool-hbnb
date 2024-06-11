#!/usr/bin/python3

from models.base_model import KeyModel

class City(KeyModel):
    def __init__(self, name, country_id):
        super().__init__()
        self.name = name
        self.country_id = country_id