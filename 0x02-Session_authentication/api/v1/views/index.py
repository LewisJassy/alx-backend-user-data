#!/usr/bin/env python3
"""
View module for the API
"""
from flask import Blueprint, abort

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized():
    """ Endpoint to test 401 error handler """
    abort(401)

@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden():
    """ Endpoint to test 403 error handler """
    abort(403)
