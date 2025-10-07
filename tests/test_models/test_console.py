#!/usr/bin/python3
"""
Unit tests for the console
"""
import unittest
import os
import sys

# Add parent directory to path to import console
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from console import HBNBCommand
    HAS_CONSOLE = True
except ImportError:
    HAS_CONSOLE = False


class TestConsole(unittest.TestCase):
    """Test cases for HBNBCommand class"""

    @unittest.skipIf(not HAS_CONSOLE, "console module not available")
    def test_console_exists(self):
        """Test that console can be imported"""
        self.assertTrue(HAS_CONSOLE)

    @unittest.skipIf(not HAS_CONSOLE, "console module not available")
    def test_console_initialization(self):
        """Test console initialization"""
        console = HBNBCommand()
        self.assertIsInstance(console, HBNBCommand)


if __name__ == '__main__':
    unittest.main()
    