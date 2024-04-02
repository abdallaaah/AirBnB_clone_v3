#!/usr/bin/python3
"""index if the views """

from . import app_views
from flask import jsonify
from models.engine.db_storage import *
from models import storage

@app_views.route('/status', methods=['GET'])
def status():
    return jsonify({'status': "OK"})

@app_views.route('/stats', methods=['GET'])
def stats():
    count_dict = {}
    for cls in classes:
        count_dict[cls] = storage.count(classes[cls])
    return jsonify(count_dict)


@app_views.route('/', strict_slashes=False)
def index():
    return 'index'
