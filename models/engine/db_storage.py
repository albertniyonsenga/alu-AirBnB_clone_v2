#!/usr/bin/python3
"""
DBStorage engine for our MYSQL database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """DBStorage engine class"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the DBStorage instance"""
        # To be implemented
        pass

    def all(self, cls=None):
        """Query all objects from database"""
        # To be implemented
        return {}

    def new(self, obj):
        """Add object to current database session"""
        # To be implemented
        pass

    def delete(self, obj=None):
        """Delete object from database"""
        # To be implemented
        pass

    def reload(self):
        """Creating all tables and sessions"""
        # To be implemented
        pass
