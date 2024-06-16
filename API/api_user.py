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
        print(f"User created succesfuly!")
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        print(f"Error creating user")
        return jsonify({"error": str(e)}), 400

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_data = data_manager.get(user_id, 'User')
    if user_data:
        print(f"Here you have the user you searching for")
        return jsonify(user_data), 200
    else:
        print(f"User not found")
        return jsonify({"error": "User not found"}), 404

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = data_manager.get(user_id, 'User')
    if not user_data:
        print(f"User not found, you have nothing to change")
        return jsonify({"error": "User not found"}), 404

    data = request.json
    user = User(email=user_data.get('email'), first_name=user_data.get('first_name'), last_name=user_data.get('last_name'), password=user_data.get('password'))
    user.update(**data)
    data_manager.update(user)
    print(f"User information is now updated!")
    return jsonify(user.to_dict()), 200

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_data = data_manager.get(user_id, 'User')
    if not user_data:
        print(f"User not found, theres nothing to delete")
        return jsonify({"error": "User not found"}), 404

    data_manager.delete(user_id, 'User')
    print(f"User deleted correctly")
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)