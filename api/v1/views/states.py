#!/usr/bin/python3
""" State Module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.state import State
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def state_list():
    """
    Method:
        - Retrieve list of all State objects
    Raises:
        - 404 Error - if the state_id is
        not linked to any State object
    Returns:
        - List of all state objects
    """
    states = storage.all(State).values()
    all_states = [state.to_dict() for state in states]
    return jsonify(all_states)


<<<<<<< HEAD
@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """
    Method:
        - Retrieves a State object
    Raises:
        - 404 Error - if the state_id is
        not linked to any State object
    Returns:
        - State object
    """
    all_states = storage.all("State").values()
    state_obj = [obj.to_dict() for obj in all_states if obj.id == state_id]
    if state_obj == []:
=======
@app_views.route('/states/<state_id>',
                 methods=['GET'], strict_slashes=False)
def state_get(state_id):
    """ Method: Retrieve a State object """
    obj = storage.get(State, state_id)
    if obj is not None:
        return jsonify(obj.to_list())
    else:
>>>>>>> ff66b348580417c4be7fad0014225e2b6a5fb5b3
        abort(404)


@app_views.route('/states/<state_id>',
                 methods=['DELETE'], strict_slashes=False)
def state_object(state_id):
    """
    Method:
        - Delete a State object
    Raises:
        - 404 Error - if the state_id is
        not linked to any State object
    Returns:
        - Empty dictionary with status code 200
    """
    obj = storage.get(State, state_id)
    if obj is not None:
        storage.delete(obj)
        storage.save()
    if obj is None:
        abort(404)
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def state_create(state_id):
    """
    Method:
        - Create a State
    Raises:
        - 400 Error - if the HTTP body
        request is not valid JSON
        400 Error - If the dictionary does
        not contain the key 'name'
    Returns:
        - New State with status code 201
    """
    if not request.is_json():
        abort(400, "Not a JSON")
    state_dict = request.get_json()
    if 'name' not in state_dict:
        abort(400, "Missing name")
    """ Create new state object """
    new_data = State(**state_dict)
    new_data.save()
    return jsonify(new_data.to_dict()), 201
    

@app_views.route('/states/<state_id>',
                 methods=['PUT'], strict_slashes=False)
def state_update(state_id):
    """
    Method:
        - Update State object
    Raises:
        - 404 Error - if the state_id is
        not linked to any State object
        - 400 Error - if the HTTP body
        request is not valid JSON
    Returns:
        - State object with status code 200
    """
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