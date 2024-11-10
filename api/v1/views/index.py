#!/usr/bin/python3
""" Method: Return JSON """
from api.v1.views import app_views
from flask import Flask, jsonify

@app_views.route('/status', strict_slashes=False)
def return_json():
    return (jsonify({"status": "OK"}))
