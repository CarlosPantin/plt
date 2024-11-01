import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        translator = PigLatin("hello world")
        self.assertEqual(translator.get_phrase(), "hello world")


if __name__ == "__main__":
    unittest.main()
