#!/usr/bin/python3

from models.base_model import KeyModel
import json
import os


class Review(KeyModel):
    def __init__(self, rating, comment, place_id, user_id):
        super().__init__()
        self.rating = rating
        self.comment = comment
        self.place_id = place_id
        self.user_id = user_id

    def save(self):
        if not self.is_valid_reviewer():
            raise ValueError("Reviewer cannot review their own place") # validacion de auto-review
        super().save()

    def is_valid_reviewer(self):
        place_file_path = "storage/Place.json"
        if os.path.exists(place_file_path):
            with open(place_file_path, 'r') as file:
                try:
                    all_data = json.load(file)
                except json.JSONDecodeError:
                    all_data = []
            for place in all_data:
                if place['id'] == self.place_id and place['user_id'] == self.user_id:
                    return False  # verifica si el user es dueno del place
        return True

    def delete(self):
        super().delete()

    def update(self, **kwargs):
        super().update(**kwargs)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'rating': self.rating,
            'comment': self.comment,
            'place_id': self.place_id,
            'user_id': self.user_id
        })
        return data
