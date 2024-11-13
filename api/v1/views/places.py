#!/usr/bin/python3
""" Place Module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.place import Place
from models.city import City
from models import storage

@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def place_object():
    """
    Method:
        - Retrieve an place object
    Raises:
        - 404 Error - if the place_id is
        not linked to any Place object
    Returns:
        - Place object
    """
    obj = storage.all(Place).values()
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def place_delete(place_id):
    """
    Method:
        - Delete a place object
    Raises:
        - 404 Error - if the place_id is
        not linked to any place object
    Returns:
        - Empty dictionary with status code 200
    """
    obj = storage.get(Place, place_id)
    if obj is not None:
        storage.delete(obj)
        storage.save()
    if obj is None:
        abort(404)
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places',
                 methods=['POST'], strict_slashes=False)
def place_create(city_id):
    """
    Method:
        - Create an place object
    Raises:
        - 404 Error - if the city_id is
        not linked to any City object
        - 400 Error - if the HTTP body
        request is not solid JSON
        - 400 Error - if the dictionary
        does not contain the key 'user_id'
    Returns:
        - New Place with status code 201
    """
    city = storage.get(City, city_id)
    if city_id is not City:
        abort(404)
    if not request.is_json():
        abort(400, "Not a JSON")
    if 'user_id' not in Place:
        abort(400, "Missing name")
    else:
        places = request.get_json()
        place_data = places
        return jsonify(place_data.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def place_update(place_id):
    """
    Method:
        - Update a place object
    Raises:
        - 400 Error - if the HTTP
        request is not valid JSON
    Returns:
        - Place object with status code 200
    """
    obj = storage.get(Place, place_id)
    if place_id is not Place:
        abort(404)
    elif not request.is_json():
        abort(404, "Not a JSON")
    place_data = request.get_json()
    for key, value in place_data.items():
            # search dict for specific key
            if key not in ['id', 'user_id', 'city_id', 'created_at', 'updated_at']:
                setattr(obj, key, value)
            storage.save()
            return jsonify(obj.to_dict()), 200
