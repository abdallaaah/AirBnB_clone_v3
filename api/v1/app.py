#!/usr/bin/python3
"""entry point for the flask api program"""

from flask import Flask
import os
from .views import *
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """exception"""
    storage.close()


if __name__ == '__main__':
    """the entry point for the app"""

    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))

    app.run(host, port, debug=True, threaded=True)
