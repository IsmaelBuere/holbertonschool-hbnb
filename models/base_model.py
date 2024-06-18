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

    @abstractmethod
    def delete(self):
        pass

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    def to_dict(self):
        return {
            'id': str(self.id), # convierte UUID a str
            'created_at': self.created_at.isoformat(), # convierten datetime a str
            'updated_at': self.updated_at.isoformat()
        }
