import os, sys
import unittest

testdir = os.path.dirname(__file__)
srcdir = '../'
path_object = os.path.abspath(os.path.join(testdir, srcdir))
sys.path.insert(0, path_object)


from translator import french_to_english
from translator import english_to_french

class Testfrench_to_english(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertEqual(french_to_english('Bonjour, monde!'), 'Hello, world!')


class Testenglish_to_french(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
        self.assertEqual(english_to_french('Hello'), 'Bonjour') 
        self.assertEqual(english_to_french('Hello, world!'), 'Bonjour, le monde !') 


unittest.main()