from core.listen import listener
from core.router import router


class Controller:

    def process_voice(self):
        text = listener.listen()

        if not text:
            return "", "I didn't hear anything."

        reply = router.process(text)

        return text, reply


controller = Controller()