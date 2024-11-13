#!/usr/bin/python3
""" State Module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.state import State
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def state_list():
    """ Method: Retrieve list of all State objects """
    states = storage.all(State).values()
    all_states = [state.to_dict() for state in states]
    return jsonify(all_states)


@app_views.route('/states/<state_id>',
                 methods=['GET'], strict_slashes=False)
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
    if not request.is_json():
        abort(400, "Not a JSON")
    state_dict = request.get_json()
    if 'name' not in state_dict:
        abort(400, "Missing name")
    """ Create new state object """
    new_data = State(**state_dict)
    new_data.save()
    storage.save()
    return jsonify(new_data.to_dict()), 201
    

@app_views.route('/states/<state_id>',
                 methods=['PUT'], strict_slashes=False)
def state_update(state_id):
    """ Method: Update State object """
    obj = storage.get(State, state_id)
    if state_id is not State:
        abort(404)
    elif not request.is_json():
        abort(404, "Not a JSON")
    state_data = request.get_json()
    for key, value in state_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict()), 200