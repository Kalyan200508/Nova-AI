from PySide6.QtCore import QObject, Signal, Slot

from voice.controller import controller


class VoiceWorker(QObject):

    finished = Signal(str, str)

    @Slot()
    def run(self):

        user_text, reply = controller.process_voice()

        self.finished.emit(user_text, reply)