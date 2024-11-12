#!/usr/bin/python3
""" City Module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.city import City
from models.state import State
from models import storage


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def city_list(state_id):
    """ Method: Retrieve list of all city objects of a state """
    obj = storage.get(State, state_id)


@app_views.route('cities/<city_id>', methods=['GET'], strict_slashes=False)
def city_object(city_id):
    """ Method: Retrieve a city object """
    obj = storage.get(City, city_id)
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def city_delete(city_id):
    """ Method: Delete a city object """
    obj = storage.get(City, city_id)
    if obj is not None:
        storage.delete(obj)
        storage.save()
    if obj is None:
        abort(404)
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def city_create(state_id):
    """ Method: Create a city object """
    obj = storage.get(State, state_id)
    if state_id is not State:
        abort(404)
    elif not request.is__json():
        abort(404, "Not a JSON")
    elif 'name' not in cities:
        abort(404, "Missing name")


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def city_update(city_id):
    """ Method: Update a city object """
    obj = storage.get(City, city_id)
    if city_id is not City:
        abort(404)
    elif not request.is__json():
        abort(404, "Not a JSON")
    city_data = request.get__json()
    for key, value in city_data.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict()), 200
