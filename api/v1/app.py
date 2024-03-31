#!/usr/bin/python3
"""entry point for the flask api program"""
from flask import Flask
from .views import *
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown_db(exception):
    storage.close()

# @app_views.route('/status', strict_slashes=False)
# def status():
#     print('xxxxxxxxxxxxxxxxxxx')
#     return 'hello world'
#
# @app_views.route('/', strict_slashes=False)
# def index():
#     return 'index'

if __name__ == '__main__':
    """the entry point for the app"""

    app.run(host='0.0.0.0', port='5000', debug=True, threaded=True)

