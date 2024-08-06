#!/usr/bin/env python3

from typing import List, TypeVar
from flask import Flask, request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Public method that returns False.
        path and excluded_paths will be used later.
        """
        return False

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
