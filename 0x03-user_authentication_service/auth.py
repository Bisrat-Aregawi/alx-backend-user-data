#!/usr/bin/env python3
"""Authentication relevant methods module"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
from uuid import uuid4


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


def _generate_uuid() -> str:
    """Return a uuid string"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self) -> None:
        self._db = DB()
        return None

    def register_user(self, email: str, password: str) -> User:
        """Register a new user to the database

        Args:
            email: email of new user
            password: password of new user

        Returns:
            a `User` instance

        Raises:
            ValueError: when user already exists
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            return self._db.add_user(
                email, _hash_password(password)
            )

    def valid_login(self, email: str, password: str) -> bool:
        """Validate a login request

        Args:
            email: email of user
            password: password of user

        Returns:
            True if email and password are in database, False otherwise
        """
        try:
            usr = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode("utf-8"),
                usr.hashed_password
            )
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Assign a and return new session id to user

        Find a user with email=`email` and assign it a session id using
        `_generate_uuid` function.

        Args:
            email: email of user

        Returns:
            New session id created for user with email `email`
        """
        try:
            usr = self._db.find_user_by(email=email)
            sessid = _generate_uuid()
            self._db.update_user(usr.id, session_id=sessid)
            return sessid
        except NoResultFound:
            pass

    def get_user_from_session_id(self, session_id: str) -> User | None:
        """Retrieve a user record by session id from database

        Args:
            session_id: stored session cookie

        Returns:
            Corresponding user if found, None otherwise
        """
        try:
            usr = self._db.find_user_by(session_id=session_id)
            return usr
        except NoResultFound:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Update corresponding user's session ID to None

        Args:
            user_id: user id

        Returns:
            None
        """
        self._db.update_user(user_id, session_id=None)
        return None
    pass
