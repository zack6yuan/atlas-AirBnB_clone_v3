#!/usr/bin/python3
""" Method: Return JSON """
from flask import Flask
from api.v1.views import app_views

@app.route('/status', strict_slashes=False)
def return_json():
    