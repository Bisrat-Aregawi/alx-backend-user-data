#!/usr/bin/env python3
"""Module defines `BasicAuth` class"""
from api.v1.auth.auth import Auth
import base64
from typing import Union


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

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str,
    ) -> Union[str, None]:
        """Return decoded base64 string

        Args:
            base64_authorization_header: base64 encoded string

        Returns:
            decoded `base64_authorization_header` if string,
            None if can't be decoded or `base64_authorization_header`
            is not a string
        """
        if base64_authorization_header:
            if isinstance(base64_authorization_header, str):
                try:
                    return base64.b64decode(
                        base64_authorization_header
                    ).decode('utf-8')
                except Exception:
                    return None
    pass
