#!/usr/bin/env python3

import bcrypt
from db import DB
from user import User
from uuid import uuid4
from typing import Union
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Converts password string to bytes
    Return: bytes
    """
    encoded_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashed_password


def _generate_uuid() -> str:
    """Returns a uuid
    """
    UUID = uuid4()
    return str(UUID)


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
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        if bcrypt.checkpw(password.encode(), user.hashed_password):
            return True

        return False


    def create_session(self, email: str) -> str:
        """ Returns session ID for a user """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()

        self._db.update_user(user.id, session_id=session_id)

        return session_id

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """It takes a single session_id string argument
        Returns a string or None
        """
        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None

        return user

    def destroy_session(self, user_id: int) -> None:
        """Updates the corresponding user's session ID to None"""
        try:
            user = self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None

        self._db.update_user(user.id, session_id=None)

        return None

    def get_reset_password_token(self, email: str) -> str:
        """Generates a reset password token if user exists"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        reset_token = _generate_uuid()

        self._db.update_user(user.id, reset_token=reset_token)

        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Uses reset token to validate update of users password"""
        if reset_token is None or password is None:
            return None

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        hashed_password = _hash_password(password)
        self._db.update_user(user.id,
                             hashed_password=hashed_password,
                             reset_token=None)
