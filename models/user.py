#!/usr/bin/python3

from models.base_model import KeyModel
import json
import os


class User(KeyModel):
    def __init__(self, email, first_name, last_name):
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

    def save(self): 
        if not self.unique_email(): # validacion para email
            raise ValueError("Email already exists")
        super().save() # llama a save base para actualizar el updated_at

    def unique_email(self):
        # verificar email que sea unico
        file_path = "persistence/storage/user.json"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    all_data = json.load(file) # carga los datos del archivo JSON
                except json.JSONDecodeError:
                    all_data = []
            for user in all_data:
                if user['email'] == self.email and user['id'] != str(self.id):
                    return False # email duplicado
        return True # email unico

    def delete(self):
        super().delete() # llama a delete base para eliminar el usuario

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save() # llama a save base para actualizar updated at

    def to_dict(self): # dict de base_model, adaptado a user.
        data = super().to_dict()
        data.update({
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        return data

    def get_places(self):
        # Tendria que obtener los lugares del ususario (places-user)
        pass
