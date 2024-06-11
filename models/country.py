#!/usr/bin/python3

from models.base_model import KeyModel

class Country(KeyModel):
    def __init__(self, name, code):
        super().__init__()
        self.name = name
        self.code = code
