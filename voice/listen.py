import os
import tempfile
import wave

import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel


SAMPLE_RATE = 16000
CHANNELS = 1
RECORD_SECONDS = 3


class Listener:

    def __init__(self):

        print("Loading Whisper model...")

        self.model = WhisperModel(
            "small",
            device="cpu",
            compute_type="int8",
        )

        self.device = None

        print("Whisper loaded.")

    def listen(self):

        print("\n🎤 Listening...")

        recording = sd.rec(
            int(RECORD_SECONDS * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype=np.int16,
            device=self.device,
        )

        sd.wait()

        temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav",
        )

        filename = temp.name
        temp.close()

        with wave.open(filename, "wb") as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(2)
            wf.setframerate(SAMPLE_RATE)
            wf.writeframes(recording.tobytes())

        try:

            segments, info = self.model.transcribe(
                filename,
                beam_size=1,
                vad_filter=True,
                language=None,
            )

            text = " ".join(
                segment.text.strip()
                for segment in segments
            ).strip()

            print("=" * 50)
            print("Language :", info.language)
            print("Confidence :", round(info.language_probability, 3))
            print("Text :", repr(text))
            print("=" * 50)

            return text

        except Exception as e:

            print(f"Speech Recognition Error: {e}")
            return ""

        finally:

            try:
                os.remove(filename)
            except OSError:
                pass


listener = Listener()