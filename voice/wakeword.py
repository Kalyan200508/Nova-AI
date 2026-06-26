WAKE_WORDS = [

    "hey nova",

    "hello nova",

    "nova",

    "hey nuva",

    "nuva",

]


class WakeWord:

    def detect(self, text):

        if not text:
            return False

        text = text.lower()

        for word in WAKE_WORDS:

            if word in text:

                return True

        return False


wakeword = WakeWord()