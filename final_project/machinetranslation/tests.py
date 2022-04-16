# pylint: disable=invalid-name
"""System Module"""
import unittest
from translator import englishToFrench
from translator import frenchToEnglish

class TestenglishToFrench(unittest.TestCase):
    """English to French tests"""
    def test1(self):
        """Test Cases for E2F"""
        # Test Hello returns Bonjour
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        # Test Hello does not return Hello
        self.assertNotEqual(englishToFrench('Hello'), 'Hello')
        # Test None returns empty string
        self.assertNotEqual(englishToFrench("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(englishToFrench(0), 0)

class TestfrenchToEnglish(unittest.TestCase):
    """French to English tests"""
    def test1(self):
        """Test Cases for F2E"""
        # Test Bonjour returns Hello
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        # Test Bonjour does not return Bonjour
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'Bonjour')
        # Test None returns empty string
        self.assertNotEqual(frenchToEnglish("None"), '')
        # Test empty string returns empty string
        self.assertNotEqual(frenchToEnglish(0),0)

unittest.main()
