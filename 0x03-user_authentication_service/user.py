#!/usr/bin/env python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    """
    Represents a user in the system.

    Attributes:
        id (int): Unique identifier
        email (int): Email address (should be str)
        hashed_password (str): Hashed password
        session_id (str, optional): Session ID
        reset_token (str, optional): Reset token

    Returns a string representation of the user object.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __repr__(self):
        return f"<User(id={self.id}, email={self.email}, session_id={self.session_id}, reset_token={self.reset_token})>"