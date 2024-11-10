#!/usr/bin/python3
""" Method: Start API """
from flask import Flask, Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/vi")

from api.v1.views.index import *
