from queue import Queue
import threading

from PySide6.QtCore import QObject, Signal

from voice.speech_engine import speech


class SpeechQueue(QObject):

    speech_started = Signal()
    speech_finished = Signal()

    def __init__(self):
        super().__init__()

        self.queue = Queue()

        self.thread = threading.Thread(
            target=self._worker,
            daemon=True,
        )

        self.thread.start()

    def speak(self, text):

        if text:
            self.queue.put(text)

    def _worker(self):

        while True:

            text = self.queue.get()

            self.speech_started.emit()

            try:
                speech.speak(text)

            finally:
                self.speech_finished.emit()
                self.queue.task_done()


speech_queue = SpeechQueue()