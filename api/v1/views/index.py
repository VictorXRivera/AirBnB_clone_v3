#!/usr/bin/python3
"""Index.py file"""
from api.v1.views import app_views
from flask import jsonify
import models


@app_views.route("/status")
def json_status():
    """
    Method to return a JSON
    """
    return jsonify({"status": OK})
