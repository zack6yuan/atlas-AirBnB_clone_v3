#!/usr/bin/python3
""" Place Module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.place import Place
from models.city import City
from models import storage


@app_views.route('/cities/<city_id>/places',
                 methods=['GET'], strict_slashes=False)
def place_list():
    """ Method: Retrieve list of all place objects of a City """


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def place_object():
    """ Method: Retrieve an place object """
    obj = storage.all(Place).values()
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)


@app_views.route('/places/<place_id>',
                 methods=['DELETE'], strict_slashes=False)
def place_delete(place_id):
    """ Method: Delete a place object """
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
    """ Method: Create an place object """
    city = storage.get(City, city_id)
    if city_id is not City:
        abort(404)
    if not request.is__json():
        abort(404, "Not a JSON")
    if 'user_id' not in Place:
        abort(400, "Missing name")
    else:
        places = request.get__json()
        place_data = places
        return (place_data)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def place_update(place_id):
    """ Method: Update an place object """
    obj = storage.get(Place, place_id)
    if place_id is not Place:
        abort(404)
    elif not request.is__json():
        abort(404, "Not a JSON")
    place_data = request.get__json()
    for key, value in place_data.items():
        # search dict for specific key
