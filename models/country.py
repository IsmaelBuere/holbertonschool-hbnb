#!/usr/bin/python3

from models.base_model import KeyModel

class Country(KeyModel):
    def __init__(self, name, code):
        super().__init__()
        self.name = name
        self.code = code

    def save(self):
        return super().save()
        #implementacion para guardar un pais

    def delete(self):
        return super().delete()
        #implementacion para guardar un pais

    def update(self, **kwargs):
        return super().update(**kwargs)
    
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'name': self.name,
            'code': self.code
        })
        return data
