#!/usr/bin/env python3
"""Authentication relevant methods module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Return hashed and salted password

    Args:
        password: password string

    Returns:
        hashed and salted byte string password
    """
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )
