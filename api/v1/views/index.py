# from . import app_views
from . import app_views
from flask import jsonify
@app_views.route('/status', methods=['GET'])
def status():
    print('xxxxxxxxxxxxxxxxxxx')
    return jsonify({'status': "OK"})

@app_views.route('/', strict_slashes=False)
def index():
    return 'index'