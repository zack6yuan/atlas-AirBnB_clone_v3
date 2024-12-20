#!/usr/bin/python3
""" Amenity Module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.amenity import Amenity
from models import storage


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def amenity_list():
    """ 
    Method: 
        - Retrieve list of all amenity objects """
    amenities = []
    for amenity in amenities:
        amenities.append(amenity.to_dict())
    return jsonify(amenities)


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def amenity_object(amenity_id):
    """ 
    Method:
        - Retrieve an amenity object
    Raises:
        - 404 Error - if the amenity_id is 
        not linked to any Amenity object
    Returns:
        - Amenity object
    """
    obj = storage.all(Amenity).values()
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def amenity_delete(amenity_id):
    """ 
    Method: 
        - Delete an amenity object
    Raises:
        - 404 Error - if amenity_id is not 
        linked to any Amenity object
    Returns:
        - Empty dictionary with the status code 200.
    """
    
    obj = storage.get(Amenity, amenity_id)
    if obj is not None:
        storage.delete(obj)
        storage.save()
    if obj is None:
        abort(404)
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def amenity_create():
    """ 
    Method:
        - Create an amenity object
    Raises:
        - 400 Error - if amenity_id is not
        linked to any Amentiy object
    Returns:
        - New Amenity with status code 201
    """
    obj = storage.get
    if not request.is_json:
        abort(400, "Not a JSON")
    elif 'name' not in amenities:
        abort(400, "Missing name")
    else:
        amenities = request.get_json()
        amenity_data = amenities.to_dict()
        return (amenity_data)


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def amenity_update(amenity_id):
    """ 
    Method:
        - Update an amenity object
    Raises:
        - 400 Error - if the HTTP request
        body is not valid JSON
    Returns:
        - Amentiy object with status code 200
    """
    obj = storage.get(Amenity, amenity_id)
    if obj is None:
        abort(404)
    elif not request.is_json():
        abort(400, "Not a JSON")
    amenity_data = request.get_json()
    for key, value in amenity_data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict()), 200
