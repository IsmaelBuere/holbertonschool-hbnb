#!/usr/bin/python3

from models.base_model import KeyModel

class User(KeyModel):
    def __init__(self, first_name, last_name, password):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.password = password