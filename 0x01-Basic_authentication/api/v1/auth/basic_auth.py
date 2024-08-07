#!/usr/bin/env python3
"""handle basic auth"""
import base64
from typing import Tuple, TypeVar
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """- defines the attributes and methods for basic
    authorization
    - inherits from Auth
    Args:
        Auth (class): Parent authentication class
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Authentication.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
