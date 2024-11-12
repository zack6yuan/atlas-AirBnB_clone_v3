#!/usr/bin/python3
""" City Module """
from api.v1.views import app_views
from flask import jsonify, abort
from models.city import City
from models.state import State
from models import storage


@app_views.route('/states/<state_id>/cities', methods=['GET'], strict_slashes=False)
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


@app_views.route('/states/<state_id>/cities', methods=['POST'], strict_slashes=False)
def city_create():
    """ Method: Create a city object """


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def city_update():
    """ Method: Update a city object """