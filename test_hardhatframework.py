# test_hardhatframework.py
"""
Tests for HardhatFramework module.
"""

import unittest
from hardhatframework import HardhatFramework

class TestHardhatFramework(unittest.TestCase):
    """Test cases for HardhatFramework class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HardhatFramework()
        self.assertIsInstance(instance, HardhatFramework)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HardhatFramework()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
