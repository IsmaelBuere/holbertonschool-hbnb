#!/usr/bin/python3

from abc import ABC, abstractmethod
from datetime import datetime
import uuid


class KeyModel(ABC):
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @abstractmethod
    def save(self):
        self.updated_at = datetime.now()
        # implementacion para guardar el objeto en base de datos

    @abstractmethod    
    def delete(self):
        # implementacion para eliminar el objeto en base de datos
        pass
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.updated_at = datetime.now()
        self.save()
    
    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }