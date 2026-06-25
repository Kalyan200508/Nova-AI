class IntentEngine:

    def __init__(self):

        self.patterns = {

            "GREETING": [
                "hello",
                "hi",
                "hey",
                "good morning",
                "good afternoon",
                "good evening",
            ],

            "TIME": [
                "time",
                "current time",
                "what time",
            ],

            "DATE": [
                "date",
                "today",
                "today's date",
            ],

            "MEMORY_NAME": [
                "my name is",
                "what is my name",
            ],

            "WHO_ARE_YOU": [
                "who are you",
                "introduce yourself",
            ],

            "THANKS": [
                "thank",
                "thanks",
                "thank you",
            ],

            "SYSTEM_EXIT": [
                "exit",
                "quit",
                "close",
            ]
        }

    def detect(self, command):

        command = command.lower().strip()

        for intent, keywords in self.patterns.items():

            for keyword in keywords:

                if keyword in command:
                    return intent

        return "UNKNOWN"


intent_engine = IntentEngine()