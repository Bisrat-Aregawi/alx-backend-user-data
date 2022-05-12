#!/usr/bin/env python3
"""Module defines `filter_datum` function
"""
import logging
import mysql.connector
from os import environ
import re
import sys
from typing import Any, List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str] = []):
        """Initialize"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Extended format function from parent class"""
        return filter_datum(
            self.fields, self.REDACTION,
            logging.Formatter.format(self, record), self.SEPARATOR,
        )


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
        re.sub(
            re.compile(r'|'.join(fld+"=.+" for fld in fields)),
            msg.split('=')[0]+"="+redaction, msg,
        ) for msg in message.split(separator)
    )


def get_logger() -> logging.Logger:
    """Return logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    sh = logging.StreamHandler()
    sh.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(sh)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Return a database connector object"""
    return mysql.connector.connect(
        user=environ.get("PERSONAL_DATA_DB_USERNAME"),
        password=environ.get("PERSONAL_DATA_DB_PASSWORD"),
        host=environ.get("PERSONAL_DATA_DB_HOST"),
        database=environ.get("PERSONAL_DATA_DB_NAME")
    )
