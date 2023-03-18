#!/usr/bin/env python3

import bcrypt


def _hash_password(password: str) -> bytes:
    """Converts password string to bytes
    Return: bytes
    """
    encoded_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(encoded_password, salt)
    return hashed_password
    # return hashed_password
