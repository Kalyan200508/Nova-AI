WAKE_WORDS = [
    "hey nova",
    "hello nova",
    "nova",
]


class WakeWord:

    def detect(self, text):

        if not text:
            return False

        text = text.lower().strip()

        return any(word in text for word in WAKE_WORDS)


wakeword = WakeWord()