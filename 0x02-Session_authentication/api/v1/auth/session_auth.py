#!/usr/bin/env python3
"""Module defines `SessionAuth` class"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """SessionAuth class
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session id for user with id `user_id`

        Args:
            user_id: id attrib of a `User` instance

        Returns:
            new uuid4 session id, None if user_id is none or not a string
        """
        if user_id:
            if isinstance(user_id, str):
                sessid = str(uuid4())
                self.__class__.user_id_by_session_id[sessid] = user_id
                return sessid
        return None
    pass
