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
    """
    Method: 
        - Retrieve list of all 
        city objects of a state
    Raises:
        - 404 Error - if the state_id
        is not linked to any State object
    Returns:
        - List of all city objects of a state
    """
    obj = storage.get(State, state_id)
    if not obj:
        abort(404)
    else:
        return jsonify(obj.to_dict())


@app_views.route('cities/<city_id>', methods=['GET'], strict_slashes=False)
def city_object(city_id):
    """
    Method: 
        - Retrieve a city object
    Raises:
        - 404 Error - if the city_id
        is not linked to any City object
    Returns:
        - City object
    """
    obj = storage.get(City, city_id)
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def city_delete(city_id):
    """
    Method:
        - Delete a city object
    Raises:
        - 404 Error: If the city_id
        is not linked to any City object
    Returns:
        - Empty directory with the status 
        code 200
    """
    obj = storage.get(City, city_id)
    if obj:
        storage.delete(obj)
        storage.save()
    if not obj:
        abort(404)
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def city_create(state_id):
    """
    Method:
        - Create a city object
    Raises:
        - 404 Error - if the state_id
        is not lined to any State object
        - 400 Error - if the HTTP body
        request is not valid JSON
        - 400 Error - If the dictionary
        does not contain the key 'name'
    Returns:
        - New city with status code 201
    """
    obj = storage.get(State, state_id)
    if obj is None:
        abort(404)
    elif not request.is_json():
        abort(400, "Not a JSON")
    elif 'name' not in obj.to_dict():
        abort(400, "Missing name")


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def city_update(city_id):
    """
    Method: 
        - Update a city object
    Raises":
        - 400 Error - if the HTTP body
        request is not valid JSON
    Returns:
        - City object with the status code 200
    """
    obj = storage.get(City, city_id)
    if obj is None:
        abort(404)
    elif not request.is_json():
        abort(404, "Not a JSON")
    city_data = request.get_json()
    for key, value in city_data.items():
        if key not in ["id", "state_id", "created_at", "updated_at"]:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict()), 200
