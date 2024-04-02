#!/usr/bin/python3
"""index if the views """

from . import app_views
from flask import jsonify
from models.engine.db_storage import *
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """status will be here"""
    return jsonify({'status': "OK"})


@app_views.route('/stats', methods=['GET'])
def stats():
    """stats will ber here"""
    count_dict = {}
    for cls_key in classes:
        count_dict[cls_key] = storage.count(classes[cls_key])
    return jsonify(count_dict)


@app_views.route('/', strict_slashes=False)
def index():
    return 'index'
