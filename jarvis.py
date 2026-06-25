from core.speech import speech
from config import USER_NAME


class Jarvis:
    def __init__(self):
        self.user = USER_NAME

    def boot(self):
        speech.speak(f"Hello {self.user}")
        speech.speak("Initializing systems")
        speech.speak("All systems online")
        speech.speak("Jarvis is ready")

    def reply(self, message):
        speech.speak(message)