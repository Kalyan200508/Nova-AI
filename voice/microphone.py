import queue

import sounddevice as sd


class Microphone:

    def __init__(self, samplerate=16000):

        self.samplerate = samplerate
        self.channels = 1
        self.queue = queue.Queue()
        self.stream = None

    def callback(self, indata, frames, time, status):

        if status:
            print(status)

        self.queue.put(indata.copy())

    def start(self):

        self.stream = sd.InputStream(
            samplerate=self.samplerate,
            channels=self.channels,
            callback=self.callback,
        )

        self.stream.start()

        print("🎤 Microphone started.")

    def stop(self):

        if self.stream:

            self.stream.stop()
            self.stream.close()
            self.stream = None

            print("🎤 Microphone stopped.")


microphone = Microphone()