import unittest
from machinetranslation.translator import english_to_french, french_to_english


class TestMachineTranslation(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Today'), 'Aujourd\'hui')
        self.assertNotEqual(english_to_french('Hello'), 'Olá')

    def test_french_to_english(self):
        self.assertEqual(french_to_english('Aujourd\'hui'), 'Today')
        self.assertNotEqual(french_to_english('été'), 'Spring')


if __name__ == '__main__':
    unittest.main()
