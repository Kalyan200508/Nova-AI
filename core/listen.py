import os
import tempfile
import wave

import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel


class Listener:

    def __init__(self):

        print("Loading Whisper model...")

        # tiny is much faster for wake-word detection
        self.model = WhisperModel(
            "tiny",
            device="cpu",
            compute_type="int8",
        )

        # None = default microphone
        self.device = None

        print("Whisper loaded.")

    def listen(self, duration=2, sample_rate=16000):

        print("\n🎤 Listening...")

        recording = sd.rec(
            int(duration * sample_rate),
            samplerate=sample_rate,
            channels=1,
            dtype=np.int16,
            device=self.device,
        )

        sd.wait()

        temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav",
        )

        temp_name = temp.name

        temp.close()

        with wave.open(temp_name, "wb") as wf:

            wf.setnchannels(1)

            wf.setsampwidth(2)

            wf.setframerate(sample_rate)

            wf.writeframes(recording.tobytes())

        try:

            segments, info = self.model.transcribe(
                temp_name,
                beam_size=1,
                vad_filter=True,
                language="en",
            )

            text = ""

            for segment in segments:
                text += segment.text + " "

            text = text.strip()

            print("=" * 50)
            print("Language :", info.language)
            print("Text     :", repr(text))
            print("=" * 50)

            return text

        finally:

            try:
                os.remove(temp_name)
            except Exception:
                pass


listener = Listener()