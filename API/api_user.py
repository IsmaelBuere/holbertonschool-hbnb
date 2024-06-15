#!/usr/bin/python3

import sys, os

# Agrega la ruta del directorio principal al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from models.user import User
from persistence.data_manager import DataManager


app = Flask(__name__)
data_manager = DataManager()


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
    try:
        user.save()
        data_manager.save(user)
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_data = data_manager.get(user_id, 'User')
    if user_data:
        return jsonify(user_data), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = data_manager.get(user_id, 'User')
    if not user_data:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    user = User(**user_data)
    user.update(**data)
    data_manager.update(user)
    return jsonify(user.to_dict()), 200

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_data = data_manager.get(user_id, 'User')
    if not user_data:
        return jsonify({"error": "User not found"}), 404

    data_manager.delete(user_id, 'User')
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)