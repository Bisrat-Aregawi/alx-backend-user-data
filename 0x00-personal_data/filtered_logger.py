#!/usr/bin/env python3
"""Module defines `filter_datum` function
"""
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    """Return log message obfuscated

    Args:
        fields: list of strings representing all fields to obfuscate
        redaction: string representing by what the field will be obfuscated
        message: string representing the log line
        separator: string representing by which character is separating all
        fields in the log line (message)

    Returns:
        obfuscated log message
    """
    return separator.join(
        re.compile(r'|'.join(fld+"=.+" for fld in fields)).sub(
            msg.split('=')[0]+"="+redaction, msg
        ) for msg in message.split(separator)
    )
