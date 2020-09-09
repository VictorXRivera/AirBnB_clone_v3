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


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def endpoint():
    """
    Method that retrieves the number of each objects by type
    """
    status = {
        "amenities": storage.count("Amenity"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
        "states": storage.count("State"),
        "users": storage.count("User")
    }

    return jsonify(status)
