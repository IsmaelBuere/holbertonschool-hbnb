#!/usr/bin/python3

from models.base_model import KeyModel

class Review(KeyModel):
    def __init__(self, rating, comment, place_id, user_id):
        super().__init__()
        self.rating = rating
        self.comment = comment
        self.place_id = place_id
        self.user_id = user_id