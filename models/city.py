#!/usr/bin/python3

from models.base_model import KeyModel


class City(KeyModel):
    def __init__(self, name, country_id):
        super().__init__()
        self.name = name
        self.country_id = country_id
        self.places = []

    def save(self):
        return super().save()

    def delete(self):
        return super().delete()

    def update(self, **kwargs):
        return super().update(**kwargs)

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name,
            'country_id': self.country_id
        })
        return data

    def get_places(self):
        # obtener lugares de una ciudad
        return self.places  # lista de lugares vinculados a la ciudad
