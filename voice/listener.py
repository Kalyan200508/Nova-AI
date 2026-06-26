from faster_whisper import WhisperModel

from voice.microphone import microphone


class Listener:

    def __init__(self):

        print("Loading Faster Whisper...")

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8",
        )

        print("Whisper ready.")

    def listen(self):

        print("Listening...")

        microphone.start()

        while True:

            chunk = microphone.queue.get()

            yield chunk


listener = Listener()