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
    def extract_base64_authorization_header(
            self, authorization_header: str
            ) -> str:
        """
        Extracts the Base64 part of the Authorization
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str
            ) -> str:
        """returns the decoded value of a Base64 string
        Args:
            base64_authorization_header (str): base64 auth header
        Returns:
            str: decoded value of base64 string
        """
        if not (base64_authorization_header and
                isinstance(base64_authorization_header, str)):
            return None
        try:
            decoded_bytes = base64.b64decode(base64_authorization_header)
            return decoded_bytes.decode('utf-8')
        except BaseException:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str
            ) -> Tuple[str, str]:
        """extracts user email and password
        from the Base64 decoded value.
        Args:
            self (obj): Basic Auth instance
            decoded_base64_authorization_header (str): auth header
        """
        if not (decoded_base64_authorization_header and
                isinstance(decoded_base64_authorization_header, str) and
                ':' in decoded_base64_authorization_header):
            return None, None

        return tuple(decoded_base64_authorization_header.split(':', 1))
