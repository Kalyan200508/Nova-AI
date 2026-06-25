from PySide6.QtCore import QObject, Signal, Slot

from core.controller import controller
from core.speech import speech


class VoiceWorker(QObject):

    finished = Signal(str, str)

    @Slot()
    def run(self):

        print("========== WORKER START ==========")

        user_text, reply = controller.process_voice()

        if reply and reply != "__EXIT__":
            speech.speak(reply)

        elif reply == "__EXIT__":
            speech.speak("Goodbye.")

        print("========== WORKER END ==========")

        self.finished.emit(user_text, reply)