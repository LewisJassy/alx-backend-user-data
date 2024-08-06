#!/usr/bin/env python3

from typing import List, TypeVar
from flask import Flask, request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method to determine if authentication is required
        """
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Ensure the path ends with a slash for comparison
        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            # Ensure the excluded path ends with a slash for comparison
            if not excluded_path.endswith('/'):
                excluded_path += '/'
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Public method that returns None.
        request will be the Flask request object.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Public method that returns None.
        request will be the Flask request object.
        """
        return None
