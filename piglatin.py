import re
from error import PigLatinError


class PigLatin:
    ALLOWED_PUNCTUATION = ".,;:!?()'"

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate_word(self, word: str) -> str:
        if word[0].lower() in "aeiou":
            if word[-1].lower() == "y":
                return word + "nay"
            elif word[-1].lower() in "aeiou":
                return word + "yay"
            else:
                return word + "ay"
        else:
            consonant_prefix = ""
            for char in word:
                if char.lower() not in "aeiou":
                    consonant_prefix += char
                else:
                    break
            return word[len(consonant_prefix):] + consonant_prefix + "ay"

    def translate(self) -> str:
        if self._phrase == "":
            return "nil"

        translated_words = []
        for part in self._phrase.split():
            # Split word from punctuation
            match = re.match(r"^([a-zA-Z-]+)([.,;:!?()']*)$", part)
            if not match:
                raise PigLatinError("Unsupported punctuation detected.")

            word, punctuation = match.groups()

            # Translate the word and add the punctuation back
            translated_word = "-".join(self.translate_word(w) for w in word.split('-'))
            translated_words.append(translated_word + punctuation)

        return ' '.join(translated_words)
