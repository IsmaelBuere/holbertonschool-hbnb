import json

def serialize(data, filename): # De dict a JSON
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def deserialize(filename): # De JSON a dict
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
