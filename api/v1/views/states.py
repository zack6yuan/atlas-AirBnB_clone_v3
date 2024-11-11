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


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
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
    
    


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def state_update(state_id):
    """ Method: Update State object """
    state_data = request.get_json()
