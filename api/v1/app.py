#!/usr/bin/python3
"""
App Module

This module sets up a Flask web application for the AirBnB clone project.
It registers the application blueprint,
configures the teardown context,
and sets up error handling
for 404 errors.

Functions:
    teardown(): Removes the current session.
    not_found(error): Returns a JSON-formatted 404 status code response.

Usage:
    The application can be run directly,
    and it will use the host and port specified
    in the environment variables HBNB_API_HOST and HBNB_API_PORT,
    or default to "0.0.0.0" and 5000 respectively.
"""

import os
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS


app = Flask(__name__)


app.register_blueprint(app_views)

""" Create CORS Instance: requests from /api/v1"""
CORS(app, resources={r"/api/v1/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown():
    """ Method: Remove the current session """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ Handler for 404 errors that returns a
        JSON-formatted 404 status code response """
    return (jsonify({"error": "Not found"}, 404))


if __name__ == "__main__":
    """ Method: Set host and port for usage """
    host = os.getenv("HBNB_API_HOST", default="0.0.0.0")
    port = os.getenv("HBNB_API_PORT", default=5000)
    app.run(host=host, port=port, threaded=True)
