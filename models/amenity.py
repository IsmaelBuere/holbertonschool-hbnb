#!/usr/bin/python3

from models.base_model import KeyModel

class Amenity(KeyModel):
    def __init__(self, name):
        super().__init__()
        self.name = name