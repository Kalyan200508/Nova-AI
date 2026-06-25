from PySide6.QtCore import QObject, Signal, Slot

from core.controller import controller
from voice.speech_queue import speech_queue


class VoiceWorker(QObject):

    finished = Signal(str, str)

    @Slot()
    def run(self):

        print("========== WORKER START ==========")

        try:
            user_text, reply = controller.process_voice()

            if reply == "__EXIT__":
                speech_queue.speak("Goodbye.")
            elif reply:
                speech_queue.speak(reply)

            self.finished.emit(user_text, reply)

        except Exception as e:
            print(f"VoiceWorker Error: {e}")
            self.finished.emit("", "An error occurred.")

        finally:
            print("========== WORKER END ==========")