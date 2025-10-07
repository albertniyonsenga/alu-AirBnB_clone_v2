#!/usr/bin/python3
"""
Unit tests for the console
"""
import unittest
import sys
import os

# Adding parent directory to the path to import console
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from console import HBNBCommand
except ImportError:
    HBNBCommand = None


class TestConsole(unittest.TestCase):
    """Test cases for HBNBCommand class"""

    @unittest.skipIf(HBNBCommand is None, "Console module not implemented")
    def test_console_initialization(self):
        """Test console initialization"""
        console = HBNBCommand()
        self.assertIsInstance(console, HBNBCommand)


if __name__ == '__main__':
    unittest.main()
    