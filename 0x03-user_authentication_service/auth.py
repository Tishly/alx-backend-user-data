#!/usr/bin/env python3

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Converts password string to bytes
    Return: bytes
    """
    encoded_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers new user to the database and hashes password.
        If user already exists, raises a ValueError.
        Return: User object
        """
        try:
            user_email = self._db.find_user_by(email=email)

        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)
            return user

        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """Validates user login
        Return: bool
        """
        user = self._db.find_user_by(email=email)
        if user is None:
            return NoResultFound

        if bcrypt.checkpw(password.encode(), user.hashed_password) == 1:
            return True

        else:
            return False
