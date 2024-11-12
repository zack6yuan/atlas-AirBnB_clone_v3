#!/usr/bin/python3
""" Review Module """
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.review import Review
from models.place import Place


@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def review_list():
    """ Method: Retrieve list of all review objects of a Place """


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def review_object():
    """ Method: Retrieve an review object """
    obj = storage.get(Review, review_id)
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)

@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def review_delete():
    """ Method: Delete a review object """
    obj = storage.get(Review, review_id)
    if obj is not None:
        storage.delete(obj)
        storage.save()
    if obj is None:
        abort(404)
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews', methods=['POST'], strict_slashes=False)
def review_create():
    """ Method: Create a review """


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def review_update():
    """ Method: Update a review object """