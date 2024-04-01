#!/usr/bin/python3
"""index if the views """

from . import app_views
from flask import jsonify
from models.engine.db_storage import *


@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({'status': "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    storage = DBStorage()  # Ensure DBStorage is instantiated
    storage.reload()  # Make sure the session is loaded
    count_dict = {}
    for class_name in classes.keys():
        count_dict[class_name.lower()] = storage.count(class_name)
    return jsonify(count_dict)  # Convert the count_dict into a JSON response


@app_views.route('/', strict_slashes=False)
def index():
    return 'index'
