class PigLatin:


    def __init__(self, phrase: str):
        self._phrase = phrase

    def get_phrase(self) -> str:
        return self._phrase

    def translate(self) -> str:
        if self._phrase == "":
            return "nil"

        word = self._phrase
        if word[0].lower() in "aeiou":
            if word[-1].lower() == "y":
                return word + "nay"
            elif word[-1].lower() in "aeiou":
                return word + "yay"
            else:
                return word + "ay"