#!/usr/bin/env python3
""" Test file for authentication classes """
from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth

def test_session_auth_inheritance():
    """ Test if SessionAuth correctly inherits from Auth """
    assert issubclass(SessionAuth, Auth), "SessionAuth does not inherit from Auth"

if __name__ == "__main__":
    test_session_auth_inheritance()
    print("SessionAuth inheritance validated successfully.")
