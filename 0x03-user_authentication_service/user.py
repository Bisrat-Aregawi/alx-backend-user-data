#!/usr/bin/env python3
"""Module defines `User` class"""
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String


Base = declarative_base()


class User(Base):
    """`User` class that maps `users` table in DB

    Attributes:
        __tablename__: name of table in the database
        id: id column of table
        email: email column of table
        hashed_password: email column of table
        session_id: email column of table
        reset_token: email column of table
    """
    __tablename__ = "users"
    id: Column = Column(Integer, primary_key=True)
    email: Column = Column(String(250), nullable=False)
    hashed_password: Column = Column(String(250), nullable=False)
    session_id: Column = Column(String(250))
    reset_token: Column = Column(String(250))
    pass
