#!/usr/bin/python3
""" Method: Return JSON """
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

classes = {
    "users": User,
    "places": Place,
    "states": State,
    "cities": City,
    "amenities": Amenity,
    "reviews": Review
}


@app_views.route('/status')
def status():
    """
    Method:
        - Route to status page
    """
    return jsonify({'status': 'OK'})


@app_views.route('/stats')
def count():
    """
    Method:
        - Retrieve the number of each
        objects by type
    """
    count_dict = {}
    for cls in classes:
        count_dict[cls] = storage.count(classes[cls])
    return jsonify(count_dict)