#!/usr/bin/python3
""" Review Module """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.review import Review
from models.place import Place
from models.user import User


@app_views.route('/places/<place_id>/reviews', methods=['GET'], strict_slashes=False)
def review_list(place_id):
    """
    Method: 
        - Retrieve list of all review objects of a Place
    Raises:
        - 404 Error - if the place_id is
        not linked to any Place object
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    reviews = [review.to_dict() for review in place.reviews]
    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def review_object(review_id):
    """
    Method:
        - Retrieve an review object
    Raises:
        - 404 Error - if the review_id is
        not linked to any Review object
    """
    obj = storage.get(Review, review_id)
    if obj is not None:
        return jsonify(obj.to_dict())
    else:
        abort(404)

@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def review_delete(review_id):
    """
    Method:
        - Delete a review object
    Raises:
        - 404 Error - if the review_id is
        not linked to any Review object
    """
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
    """ 
    Method:
        - Create a review
    Raises:
        - 404 Error - if the place_id is
        not linked to any Place object
        - 400 Error - if the HTTP body
        request is not valid JSON
        - 400 Error - if the dictionary does
        not contain the key 'user_id'
        - 404 Error - if the user_id is
        not linked to any User object
        - 400 Error - if the dictionary does
        not contain the key 'text'
    Returns:
        - New Review with status code 201
    """
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    if not request.is_json:
        abort(400, "Not a JSON")
    review_data = request.get_json()
    if review_data is None:
        abort(400, "Not a JSON")
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
    """
    Method:
        - Update a review object
    Raises:
        - 404 Error - if the review_id is
        not linked to any Review object
        - 400 Error - if the HTTP body
        request is not valid JSON
    Returns:
        - Review object with status code 200
    """
    obj = storage.get(Review, review_id)
    if obj is None:
        abort(404)
    if not request.is_json:
        abort(400, "Not a JSON")
    review_data = request.get_json()
    ignore_keys = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']
    for key, value in review_data.items():
        if key not in ignore_keys:
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict()), 200
