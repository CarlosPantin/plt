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

    def test_translate_word_starting_with_consonant(self):
        translator_hello = PigLatin("hello")
        self.assertEqual(translator_hello.translate(), "ellohay")

        translator_yellow = PigLatin("yellow")
        self.assertEqual(translator_yellow.translate(), "ellowyay")

    def test_translate_word_starting_with_multiple_consonants(self):
        translator_known = PigLatin("known")
        self.assertEqual(translator_known.translate(), "ownknay")

    def test_translate_phrase_with_multiple_words(self):
        translator_phrase = PigLatin("hello world")
        self.assertEqual(translator_phrase.translate(), "ellohay orldway")

        translator_composite = PigLatin("well-being")
        self.assertEqual(translator_composite.translate(), "ellway-eingbay")



if __name__ == "__main__":
    unittest.main()
