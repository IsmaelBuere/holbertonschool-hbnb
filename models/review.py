#!/usr/bin/python3

from models.base_model import KeyModel

class Review(KeyModel):
    def __init__(self, rating, comment, place_id, user_id):
        super().__init__()
        self.rating = rating
        self.comment = comment
        self.place_id = place_id
        self.user_id = user_id

    def save(self):
        super().save()
        # Implementación específica para guardar una review

    def delete(self):
        super().delete()
        # Implementación específica para eliminar una review

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
