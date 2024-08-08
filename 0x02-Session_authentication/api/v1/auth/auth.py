#!/usr/bin/env python3
"""python module"""

from flask import request
from typing import List, TypeVar


class Auth:
    """authentication class"""
    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """Returns True if authentication is required for the path"""
        if any(path.startswith(p) for p in excluded_paths):
            return False
        return True


    def authorization_header(self, request=None) -> str:
        """
        Public method that returns None.
        request will be the Flask request object.
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Public method that returns None.
        request will be the Flask request object.
        """
        return None
