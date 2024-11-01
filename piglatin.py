import re
from error import PigLatinError


class PigLatin:
    ALLOWED_PUNCTUATION = ".,;:!?()'"

    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate_word(self, word: str) -> str:
        if any(c.islower() and c.isupper() for c in word):  # Mixed case check
            raise PigLatinError("Mixed case detected in word.")

        original_case = word.isupper()
        title_case = word.istitle()

        if word[0].lower() in "aeiou":
            if word[-1].lower() == "y":
                translated = word + "nay"
            elif word[-1].lower() in "aeiou":
                translated = word + "yay"
            else:
                translated = word + "ay"
        else:
            consonant_prefix = ""
            for char in word:
                if char.lower() not in "aeiou":
                    consonant_prefix += char
                else:
                    break
            translated = word[len(consonant_prefix):] + consonant_prefix + "ay"

        if original_case:
            return translated.upper()
        elif title_case:
            return translated.capitalize()
        else:
            return translated

    def translate(self) -> str:
        if self._phrase == "":
            return "nil"

        translated_words = []
        for part in self._phrase.split():
            match = re.match(r"^([a-zA-Z-]+)([.,;:!?()']*)$", part)
            if not match:
                raise PigLatinError("Unsupported punctuation detected.")

            word, punctuation = match.groups()
            translated_word = "-".join(self.translate_word(w) for w in word.split('-'))
            translated_words.append(translated_word + punctuation)

        return ' '.join(translated_words)
