#!/usr/bin/env python3
"""Module defines `hash_password` function"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return hashed and salted password

    Args:
        password: a password string

    Returns:
        hashed and salted byte string password
    """
    return bcrypt.hashpw(
        password.encode('utf-8'),
        bcrypt.gensalt()
    )
