import asyncio
import os
import tempfile
import threading

import edge_tts
from playsound3 import playsound

VOICE = "en-IN-PrabhatNeural"


class SpeechEngine:

    def __init__(self):
        self.lock = threading.Lock()

    async def _generate(self, text, filename):
        communicate = edge_tts.Communicate(text=text, voice=VOICE)
        await communicate.save(filename)

    def speak(self, text):

        if not text:
            return

        with self.lock:

            print(f"Jarvis: {text}")

            fd, filename = tempfile.mkstemp(suffix=".mp3")
            os.close(fd)

            try:
                print("Generating speech...")
                asyncio.run(self._generate(text, filename))

                print("Playing...")
                playsound(filename)

                print("Finished playing.")

            finally:
                try:
                    os.remove(filename)
                except OSError:
                    pass


speech = SpeechEngine()