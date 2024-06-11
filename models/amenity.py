#!/usr/bin/python3

from models.base_model import KeyModel

class Amenity(KeyModel):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def save(self):
        super().save()
        # Implementación específica para guardar una amenity

    def delete(self):
        super().delete()
        # Implementación específica para eliminar una amenity

    def update(self, **kwargs):
        super().update(**kwargs)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name
        })
        return data
