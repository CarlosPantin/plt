import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        translator = PigLatin("hello world")
        self.assertEqual(translator.get_phrase(), "hello world")

    def test_translate_empty_phrase(self):
        translator = PigLatin("")
        self.assertEqual(translator.translate(), "nil")

    def test_translate_word_starting_with_vowel(self):
        translator_any = PigLatin("any")
        self.assertEqual(translator_any.translate(), "anynay")

        translator_apple = PigLatin("apple")
        self.assertEqual(translator_apple.translate(), "appleyay")

        translator_ask = PigLatin("ask")
        self.assertEqual(translator_ask.translate(), "askay")



if __name__ == "__main__":
    unittest.main()
