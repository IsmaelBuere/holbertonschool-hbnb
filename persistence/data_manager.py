#!/usr/bin/python3

import json, os
from persistence.ipersistence import IPersistenceManager
from persistence.storage.json_storage import serialize, deserialize

class DataManager(IPersistenceManager):
    def __init__(self, storage_file="persistence/storage/data.json"):
        self.storage_file = storage_file
        self.data_storage = deserialize(self.storage_file)
   
    def save(self, entity):
        entity_type = type(entity).__name__
        if entity_type not in self.data_storage:
            self.data_storage[entity_type] = []
        self.data_storage[entity_type].append(entity.to_dict())
        serialize(self.data_storage, self.storage_file)

    def get(self, entity_id, entity_type):
        for item in self.data_storage.get(entity_type, []):
            if item['id'] == entity_id:
                return item
        return None

    def update(self, entity):
        entity_type = type(entity).__name__
        entity_dict = entity.to_dict()
        entity_list = self.data_storage.get(entity_type, [])
        for item in entity_list:
            if item['id'] == entity.id:
                item.update(entity_dict)
            break
        else:
            entity_list.append(entity_dict)
            
        self.data_storage[entity_type] = entity_list
        serialize(self.data_storage, self.storage_file)

    def delete(self, entity_id, entity_type):
        self.data_storage[entity_type] = [
            item for item in self.data_storage.get(entity_type, [])
            if item['id'] != entity_id
        ]
        serialize(self.data_storage, self.storage_file)
