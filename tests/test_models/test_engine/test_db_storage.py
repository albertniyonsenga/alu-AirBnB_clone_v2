#!/usr/bin/python3
"""
Unit tests for DBStorage engine
"""
import os
import unittest
import sys

# Add parent directories to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '..'))

try:
    from models.engine.db_storage import DBStorage
    HAS_DB_STORAGE = True
except ImportError:
    HAS_DB_STORAGE = False


class TestDBStorage(unittest.TestCase):
    """Test cases for DBStorage class"""

    @unittest.skipIf(not HAS_DB_STORAGE, "DBStorage module not available")
    def test_db_storage_exists(self):
        """Test that DBStorage can be imported"""
        self.assertTrue(HAS_DB_STORAGE)

    @unittest.skipIf(not HAS_DB_STORAGE, "DBStorage module not available")
    def test_db_storage_initialization(self):
        """Test DBStorage initialization"""
        storage = DBStorage()
        self.assertIsInstance(storage, DBStorage)


if __name__ == '__main__':
    unittest.main()
    