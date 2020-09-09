#!/usr/bin/python3
"""Index.py file"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from datetime import datetime
import uuid


@app_views.route('/status/', methods=['GET'])
def list_of_states():
    """
    Retrieving a list of all state objects
    """
    list_of_states = [obj.to_dict() for obj in storage.all("State").values()]
    return jsonify(list_of_states)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """
    Getting state objects
    """
    stored_states = storage.all("State").values()
    states_object = [obj.to_dict() for obj in stored_states if obj.id == state_id]
    if states_object == []:
        abort(404)
    return jsonify(states_object[0])


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """
    Deleting state object
    """
    stored_states = storage.all("State").values()
    states_object = [obj.to_dict() for obj in stored_states if obj.id == state_id]
    if states_object == []:
        abort(404)
    states_object.remove(states_object[0])
    for obj in stored_states:
        if obj.id == state_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'])
def create_state():
    """
    Creating a State object
    """
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    states = []
    new_state = State(name=request.json['name'])
    storage.new(new_state)
    storage.save()
    states.append(new_state.to_dict())
    return jsonify(states[0]), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_states(state_id):
    """
    Updates State object
    """
    stored_states = storage.all("State").values()
    states_object = [obj.to_dict() for obj in stored_states if obj.id == state_id]
    if states_object == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    states_object[0]['name'] = request.json['name']
    for obj in stored_states:
        if obj.id == state_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(states_objects[0]), 200


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
