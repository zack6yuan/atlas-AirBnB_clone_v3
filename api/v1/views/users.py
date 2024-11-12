#!/usr/bin/python3
""" User Module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User
from models import storage


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def user_list():
    """ Method: Retrieve list of all amenity objects """


@app_views.route('/user/<user_id>', methods=['GET'], strict_slashes=False)
def user_object():
    """ Method: Retrieve an user object """
    obj = storage.all(User).values()
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def user_create():
    """ Method: Create an user object """
    if not request.is__json:
        abort(404, "Not a JSON")
    elif 'email' not in users:
        abort(400, "Missing email")
    elif 'password' not in users:
        abort(400, "Missing password")
    else:
        users = request.get.__json()
        user_data = users
        return (user_data)
        


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def user_update(user_id):
    """ Method: Update an user object """
    obj = storage.get(User, user_id)
    if user_id is not User:
        abort(404)
    elif not request.is__json():
        abort(404, "Not a JSON")
    user_data = request.get__json()
    for key, value in user_data.items():
        