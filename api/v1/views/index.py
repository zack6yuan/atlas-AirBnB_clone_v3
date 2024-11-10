#!/usr/bin/python3
""" Method: Return JSON """
from flask import Flask, jsonify
from api.v1.views import app_views

@app_views.route('/status', strict_slashes=False)
def return_json():
    views = {"status": "OK"}
    return (jsonify(views))
