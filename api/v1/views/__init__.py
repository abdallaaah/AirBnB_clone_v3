#!/usr/bin/python3
"""the init file of views"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')\


from . import index