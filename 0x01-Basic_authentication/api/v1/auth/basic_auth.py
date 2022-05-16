#!/usr/bin/env python3
"""Module defines `BasicAuth` class"""
from typing import Union
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class
    """

    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> Union[str, None]:
        """Return encoded part of `Authorization` header if any

        Args:
            authorization_header: Authorization header of request passed

        Returns:
            encoded part, None if passed header is not a string
        """
        if authorization_header and isinstance(authorization_header, str):
            auth_header = authorization_header.split(' ')
            if auth_header[0] == "Basic":
                return auth_header[1]
            return None
        return None
    pass
