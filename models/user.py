#!/usr/bin/python3

from models.base_model import KeyModel
import json, os

class User(KeyModel):
    def __init__(self, email, first_name, last_name, password):
        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    
    def save_account(self):
        if not self.is_unique_email():
            raise ValueError("Email already exists")
        super().save()

    def is_unique_email(self):
        file_path = "storage/User.json"
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    all_data = json.load(file)
                except json.JSONDecodeError:
                    all_data = []
            for user in all_data:
                if user['email'] == self.email and user['id'] != str(self.id):
                    return False
        return True    

    def delete_account(self):
    #implementacion para borrar usuario
        return self.delete()

    def update_account(self, new_info):
        for key, value in new_info.items():
            setattr(self, key, value)
        self.save()
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name
        })
        return data

    def password_check(self, password):
        # Lógica para verificar la contraseña
        return self.password == password

    def get_places(self):
        # Lógica para obtener los lugares del usuario
        pass