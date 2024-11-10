#!/usr/bin/python3
""" State Module """
from api.v1.views import app_views
from flask import Flask
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_state():
    """ Method: Retrieve list of all State objects """


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def get_state_id():
    """ Method: Retrieve a State object """


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """ Method: Create a State """


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def update_state():
    """ Method: Updates a State object """