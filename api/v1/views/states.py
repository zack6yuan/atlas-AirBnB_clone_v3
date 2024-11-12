#!/usr/bin/python3
""" State Module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.state import State
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def state_list():
    """ Method: Retrieve list of all State objects """
    states = []
    for state in states:
        states.append(state.to_dict())
    return jsonify(states)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def state_get(state_id):
    """ Method: Retrieve a State object """
    obj = storage.get(State, state_id)
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def state_object(state_id):
    """ Method: Delete a State object """
    obj = storage.get(State, state_id)
    if obj is not None:
        storage.delete(obj)
        storage.save()
    if obj is None:
        abort(404)
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def state_create(state_id):
    """ Method: Create a State """
    if not request.is__json():
        abort(404, "Not a JSON")
    state_dict = request.get__json()
    if 'name' not in state_dict:
        abort(400, "Missing name")
    new_state = state


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def state_update(state_id):
    """ Method: Update State object """
    obj = storage.get(State, state_id)
    if state_id is not State:
        abort(404)
    elif not request.is__json():
        abort(404, "Not a JSON")
    state_data = request.get__json()
    for key, value in state_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict()), 200