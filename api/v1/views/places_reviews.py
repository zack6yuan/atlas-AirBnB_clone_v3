#!/usr/bin/python3
""" Review Module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.review import Review
from models.place import Place
from models.user import User


@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def review_list():
    """ Method: Retrieve list of all review objects of a Place """


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def review_object(review_id):
    """ Method: Retrieve an review object """
    obj = storage.get(Review, review_id)
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)

@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def review_delete(review_id):
    """ Method: Delete a review object """
    obj = storage.get(Review, review_id)
    if obj is not None:
        storage.delete(obj)
        storage.save()
    if obj is None:
        abort(404)
    return jsonify({}), 200


@app_views.route('/places/<place_id>/reviews',
                 methods=['POST'], strict_slashes=False)
def review_create(place_id):
    """ Method: Create a review """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.is_json:
        abort(400, "Not a JSON")
    review_data = request.get_json()
    if 'user_id' not in review_data:
        abort(400, "Missing user_id")
    user = storage.get(User, review_data['user_id'])
    if user is None:
        abort(404)
    if 'text' not in review_data:
        abort(400, "Missing text")
    review_data['place_id'] = place_id
    new_review = Review(**review_data)
    storage.new(new_review)
    storage.save()
    return jsonify(new_review.to_dict()), 201
    
        


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def review_update(review_id):
    """ Method: Update a review object """
    obj = storage.get(Review, review_id)
    if review_id is not Review:
        abort(404)
    elif not request.is__json():
        abort(404, "Not a JSON")
    user_data = request.get__json()
    for key, value in user_data.items():
        # search dict for specific key
