#!/usr/bin/env python3
"""python module"""

from flask import request
from typing import List, TypeVar
import fnmatch


class Auth:
    """authentication class"""
    def require_auth(self, path: str, excluded_paths: list) -> bool:
        """check if a path need an authentication"""
        if path is None or excluded_paths is None:
            return True
        
        for excluded_path in excluded_paths:
            # Check if the excluded path ends with '*'
            if fnmatch.fnmatch(path, excluded_path):
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
