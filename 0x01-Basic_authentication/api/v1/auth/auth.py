#!/usr/bin/env python3
"""Module defines `auth` class"""
from flask import request
from typing import List, TypeVar


class Auth():
    """Auth class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """`require_auth` function"""
        if path:
            if excluded_paths is not None and excluded_paths != []:
                if path in excluded_paths or path + '/' in excluded_paths:
                    return False
        return True


    def authorization_header(self, request=None) -> str:
        """`authorization_header` function"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """`current_user` function"""
        return None
    pass
