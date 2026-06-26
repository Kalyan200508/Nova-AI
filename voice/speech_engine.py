import asyncio
import os
import tempfile
import threading

import edge_tts
from playsound3 import playsound

from voice.personality import personality

# -----------------------------
# NOVA SETTINGS
# -----------------------------

ASSISTANT_NAME = "Nova"

VOICE = "en-US-JennyNeural"

RATE = "-8%"

PITCH = "+2Hz"


class SpeechEngine:

    def __init__(self):
        self.lock = threading.Lock()

    async def _generate(self, text, filename):

        communicate = edge_tts.Communicate(
            text=text,
            voice=VOICE,
            rate=RATE,
            pitch=PITCH,
        )

        await communicate.save(filename)

    def speak(self, text):

        if not text:
            return

        # -----------------------------
        # Apply Nova Personality
        # -----------------------------
        text = personality.format(text)

        with self.lock:

            print(f"{ASSISTANT_NAME}: {text}")

            fd, filename = tempfile.mkstemp(suffix=".mp3")
            os.close(fd)

            try:

                asyncio.run(
                    self._generate(
                        text,
                        filename,
                    )
                )

                playsound(filename)

            finally:

                try:
                    os.remove(filename)
                except OSError:
                    pass


speech = SpeechEngine()