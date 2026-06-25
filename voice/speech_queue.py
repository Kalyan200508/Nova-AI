from queue import Queue
import threading

from voice.speech_engine import speech


class SpeechQueue:

    def __init__(self):
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

            try:
                speech.speak(text)

            finally:
                self.queue.task_done()


speech_queue = SpeechQueue()