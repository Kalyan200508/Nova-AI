import asyncio
import os
import tempfile

import edge_tts
import pygame


class SpeechEngine:

    def __init__(self):

        pygame.mixer.init()

        self.voice = "en-US-AriaNeural"
        self.rate = "+0%"
        self.pitch = "+0Hz"
        self.volume = 1.0

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

        try:

            asyncio.run(
                self._generate(text, filename)
            )

            pygame.mixer.music.load(filename)

            pygame.mixer.music.set_volume(self.volume)

            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)

            pygame.mixer.music.unload()

        finally:

            try:
                os.remove(filename)
            except OSError:
                pass

    def stop(self):

        pygame.mixer.music.stop()

    def set_voice(self, voice):

        self.voice = voice

    def set_rate(self, rate):

        self.rate = rate

    def set_pitch(self, pitch):

        self.pitch = pitch

    def set_volume(self, volume):

        self.volume = volume


speech = SpeechEngine()