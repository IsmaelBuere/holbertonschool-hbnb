#!/usr/bin/python3

from abc import ABC
from datetime import datetime
import uuid


class KeyModel(ABC):
    def __init__(self):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
