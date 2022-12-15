import unittest

from translator import englishToFrench, englishToFrench

class TestEnglishToFrench(unittest.TestCase):
    def test1e(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # Tests Hello to Bonjour
        self.assertEqual(englishToFrench(None), None) #Tests null input

class TestFrenchToEnglish(unittest.TestCase):
    def test1f(self):
        self.assertEqual(englishToFrench('Bonjour'), 'Hello') #Tests Bonjour to Hello
        self.assertEqual(englishToFrench(None), None) #Tests null inpit

unittest.main()
