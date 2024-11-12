#!/usr/bin/python3
""" Amenity Module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.amenity import Amenity
from models import storage


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def amenity_list():
    """ Method: Retrieve list of all amenity objects """
    amenities = []
    for amenity in amenities:
        amenities.append(amenity.to_dict())
    return jsonify(amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def amenity_object(amenity_id):
    """ Method: Retrieve an amenity object """
    obj = storage.all(Amenity).values()
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def amenity_delete(amenity_id):
    """ Method: Delete an amenity object """
    obj = storage.get(Amenity, amenity_id)
    if obj is not None:
        storage.delete(obj)
        storage.save()
    if obj is None:
        abort(404)
    return jsonify({}), 200
    

@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def amenity_create():
    """ Method: Create an amenity object """
    if not request.is__json:
        abort(400, "Not a JSON")
    elif 'name' not in amenities:
        abort(400, "Missing name")
    else:
        amenities = request.get__json()
        amenity_data = amenities
        return (amenity_data)


@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def amenity_update(amenity_id):
    """ Method: Update an amenity  object """
    obj = storage.get(Amenity, amenity_id)
    if amenity_id is not Amenity:
        abort(404)
    elif not request.is__json():
        abort(400, "Not a JSON")
