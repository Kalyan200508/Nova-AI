import asyncio
import os
import tempfile

import edge_tts
import pygame


class SpeechEngine:

    def __init__(self):

        pygame.mixer.init()

        # Change this voice anytime
        self.voice = "en-US-AriaNeural"

        self.rate = "+0%"

        self.pitch = "+0Hz"

    async def _generate(self, text, filename):

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice,
            rate=self.rate,
            pitch=self.pitch,
        )

        await communicate.save(filename)

    def speak(self, text):

        if not text:
            return

        filename = tempfile.mktemp(suffix=".mp3")

        asyncio.run(
            self._generate(text, filename)
        )

        pygame.mixer.music.load(filename)

        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        pygame.mixer.music.unload()

        try:
            os.remove(filename)
        except Exception:
            pass

    def stop(self):

        pygame.mixer.music.stop()

    def set_voice(self, voice):

        self.voice = voice


speech = SpeechEngine()