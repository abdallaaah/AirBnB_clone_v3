#!/usr/bin/python3
"""
Handles all RESTful API actions for `State` objects
"""
from flask import jsonify, abort, request
from models import storage
from models.state import State
from . import app_views


@app_views.route("/states", strict_slashes=False, methods=['GET'])
def states_now():
    """Retrieve the list of all `State` objects"""
    result = []
    for value in storage.all(State).values():
        result.append(value.to_dict())
    return jsonify(result)


@app_views.route("/states/<state_id>", strict_slashes=False)
def state_now(state_id: str):
    """Retrive one state object

    Args:
        state_id (string): state identifier

    Returns:
        Response: `State` object in json
    """
    result = storage.get(State, state_id)
    if result is None:
        abort(404)
    return jsonify(result.to_dict())


@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
def delete_state(state_id):
    """Delete a state object

    Args:
        state_id (str): state identifier

    Returns:
        Response: Empty dictionary - `{}`
    """
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return jsonify({})


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def create_state():
    """Create a `State` object"""
    if not request.get_json():
        abort(400, "Not a JSON")
    if "name" not in request.get_json():
        abort(400, "Missing name")
    state = State(**request.get_json())
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def update_state(state_id):
    """Update `State` object

    Args:
        state_id (str): state identifier

    Returns:
        Response: `State` object with status code 200
    """
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    if not request.get_json():
        abort(400, "Not a JSON")
    key = "name"
    setattr(state, key, request.get_json().get(key))
    state.save()
    return jsonify(state.to_dict())