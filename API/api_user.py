#!/usr/bin/python3

import sys, os

# Agrega la ruta del directorio principal al sys.path
sys.path.api_userend(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from models.user import User
from persistence.data_manager import DataManager


api_user = Flask(__name__)
data_manager = DataManager()


@api_user.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'], password=data['password'])
    try:
        user.save()
        data_manager.save(user)
        print(f"User created succesfuly!")
        return jsonify(user.to_dict()), 201
    except ValueError as error:
        print(f"Error creating user")
        return jsonify({"error": str(error)}), 400

@api_user.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user_info = data_manager.get(user_id, 'User')
    if user_info:
        print(f"Here you have the user you searching for")
        return jsonify(user_info), 200
    else:
        print(f"User not found...")
        return jsonify({"error": "User not found"}), 404

@api_user.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    user_info = data_manager.get(user_id, 'User')
    if not user_info:
        print(f"User not found, you have nothing to change")
        return jsonify({"error": "User not found"}), 404

    data = request.json
    user = User(email=user_info.get('email'), first_name=user_info.get('first_name'), last_name=user_info.get('last_name'), password=user_info.get('password'))
    user.update(**data)
    data_manager.update(user)
    print(f"User information is now updated!")
    return jsonify(user.to_dict()), 200

@api_user.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    user_info = data_manager.get(user_id, 'User')
    if not user_info:
        print(f"User not found, theres nothing to delete")
        return jsonify({"error": "User not found"}), 404

    data_manager.delete(user_id, 'User')
    print(f"User deleted correctly")
    return '', 204

if __name__ == '__main__':
    api_user.run(debug=True)