import unittest
from translator import french_to_english, english_to_french

class TestEnglishTranslator(unittest.TestCase):

  def test1(self):
    self.assertIsNone(english_to_french(''))

  def test2(self):
    self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchTranslator(unittest.TestCase):

  def test1(self):
    self.assertIsNone(french_to_english(''))

  def test2(self):
    self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()