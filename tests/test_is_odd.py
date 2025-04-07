import unittest
import sys
import os

# Add the parent directory to sys.path to import server
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from server import is_odd


class TestIsOdd(unittest.TestCase):
    def test_odd_numbers(self):
        """Test that odd numbers return True"""
        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(101))
        self.assertTrue(is_odd(-5))
        
    def test_even_numbers(self):
        """Test that even numbers return False"""
        self.assertFalse(is_odd(0))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(100))
        self.assertFalse(is_odd(-4))
    
    def test_type_error(self):
        """Test that non-integer inputs raise TypeError"""
        with self.assertRaises(TypeError):
            is_odd("not a number")
        
        with self.assertRaises(TypeError):
            is_odd(None)
    
    def test_large_numbers(self):
        """Test behavior with large numbers"""
        self.assertTrue(is_odd(999999999999999999))
        self.assertFalse(is_odd(1000000000000000000))


if __name__ == "__main__":
    unittest.main()

