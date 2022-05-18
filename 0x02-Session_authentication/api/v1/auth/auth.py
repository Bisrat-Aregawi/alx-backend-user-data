#!/usr/bin/env python3
"""Module defines `Auth` class"""
from os import getenv
import re
from typing import List, TypeVar, Union


class Auth():
    """Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Function checks request paths against excluded ones

        Args:
            path: path requested
            excluded_paths: list of paths internally deemed public

        Returns:
            True if path is not found in excluded_paths, False otheriwse
        """
        if path:
            if excluded_paths is not None and excluded_paths != []:
                if path in excluded_paths or path + '/' in excluded_paths:
                    return False
                for pth in excluded_paths:
                    if pth[-1] == '*' and re.compile(pth[:-1]).match(path):
                        return False
        return True

    def authorization_header(self, request=None) -> Union[str, None]:
        """Function returns value of the authorization header `Authorization

        Args:
            request: request object (imported from flask & passed by reference)

        Returns:
            Value of Authorization header if any, None if request is None
        """
        if not request:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """`current_user` function"""
        return None

    def session_cookie(self, request=None) -> str:
        """Return cookie value from a request

        Args:
            request: request object (imported from flask & passed by reference)

        Returns:
            Value of passed cookie if any, None if request is None
        """
        sess_name = getenv("SESSION_NAME")
        if request:
            return request.cookies.get(sess_name)
        return None
    pass
