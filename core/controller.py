from core.listen import listener
from core.router import router
from core.speech import speech


class Controller:
    def process_voice(self):
        text = listener.listen()

        if not text:
            return "", "I didn't hear anything."

        reply = router.process(text)

        if reply == "__EXIT__":
            speech.speak("Goodbye.")
            return text, "__EXIT__"

        speech.speak(reply)

        return text, reply


controller = Controller()
