#!/usr/bin/python3

import json
import os
from persistence.persistence import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self, storage_dir="storage"):
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def _get_file_path(self, entity_type):
        # Obtiene la ruta del archivo de almacenamiento para un tipo de entidad específico.
        return os.path.join(self.storage_dir, f"{entity_type}.json")

    def save(self, entity):
        # Guarda una nueva entidad en el archivo JSON correspondiente.
        file_path = self._get_file_path(type(entity).__name__)
        data = []
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        entity_dict = entity.to_dict()
        data.append(entity_dict)
        with open(file_path, 'w') as file:
            json.dump(data, file, default=str, indent=4)

    def get(self, entity_id, entity_type):
        # Obtiene una entidad específica por su ID.
        file_path = self._get_file_path(entity_type)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                    for item in data:
                        if item['id'] == entity_id:
                            return item
                except json.JSONDecodeError:
                    return None
        return None

    def update(self, entity):
        # Actualiza una entidad existente.
        file_path = self._get_file_path(type(entity).__name__)
        data = []
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
        entity_dict = entity.to_dict()
        for i, item in enumerate(data):
            if item['id'] == entity.id:
                data[i] = entity_dict
                break
        else:
            data.append(entity_dict)
        with open(file_path, 'w') as file:
            json.dump(data, file, default=str, indent=4)

    def delete(self, entity_id, entity_type):
        # Elimina una entidad por su ID.
        file_path = self._get_file_path(entity_type)
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = []
            data = [item for item in data if item['id'] != entity_id]
            with open(file_path, 'w') as file:
                json.dump(data, file, default=str, indent=4)
