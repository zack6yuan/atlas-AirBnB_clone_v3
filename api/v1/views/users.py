#!/usr/bin/python3
""" User Module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User
from models import storage


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def user_list():
    """ Method: Retrieve list of all user objects """
    users = list(storage.all(User).values())
    return jsonify([user.to_dict() for user in users])

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """ Method: Retrieve a user object """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """ Method: Create a new user """
    if not request.is_json:
        abort(400, "Not a JSON")
    user_data = request.get_json()
    if 'email' not in user_data:
        abort(400, "Missing email")
    if 'password' not in user_data:
        abort(400, "Missing password")
    new_user = User(**user_data)
    storage.new(new_user)
    storage.save()
    return jsonify(new_user.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """ Method: Update a user object """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if not request.is_json:
        abort(400, "Not a JSON")
    user_data = request.get_json()
    for key, value in user_data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    storage.save()
    return jsonify(user.to_dict()), 200
